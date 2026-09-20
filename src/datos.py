"""Carga, validación y filtro de la población de estudio."""

import pandas as pd


FACTORES = [
    "enfermedades_dolorosas",
    "maltrato_sexual",
    "muerte_familiar",
    "conflicto_pareja",
    "problemas_economicos",
    "esc_educ",
    "problemas_juridicos",
    "problemas_laborales",
    "suicidio_amigo",
]

ETIQUETAS_FACTORES = {
    "enfermedades_dolorosas": "Enfermedades dolorosas",
    "maltrato_sexual": "Maltrato sexual",
    "muerte_familiar": "Muerte de un familiar",
    "conflicto_pareja": "Conflicto de pareja",
    "problemas_economicos": "Problemas económicos",
    "esc_educ": "Problemas escolares",
    "problemas_juridicos": "Problemas jurídicos",
    "problemas_laborales": "Problemas laborales",
    "suicidio_amigo": "Suicidio de un amigo",
}

COLUMNAS_FILTRO = [
    "ano_notificacion",
    "clasificaciondelaconducta",
    "ciclovital",
]
COLUMNAS_REQUERIDAS = COLUMNAS_FILTRO + FACTORES


def cargar_datos(ruta):
    """Carga del CSV únicamente las doce columnas necesarias."""
    encabezados = pd.read_csv(ruta, sep=";", nrows=0).columns
    faltantes = [columna for columna in COLUMNAS_REQUERIDAS if columna not in encabezados]

    if faltantes:
        raise ValueError(f"Faltan columnas requeridas: {', '.join(faltantes)}")

    return pd.read_csv(ruta, sep=";", usecols=COLUMNAS_REQUERIDAS)


def filtrar_poblacion(datos, ano_inicial, ano_final):
    """Selecciona ideación suicida, adolescencia y el periodo definido."""
    if ano_inicial > ano_final:
        raise ValueError("El año inicial no puede ser mayor que el año final.")

    # Se comprueba que no existan espacios al inicio o al final que alteren
    # las comparaciones exactas utilizadas en el filtro.
    for columna in ["clasificaciondelaconducta", "ciclovital"]:
        con_espacios = datos[columna].dropna().ne(datos[columna].dropna().str.strip())
        if con_espacios.any():
            raise ValueError(f"La columna {columna} contiene espacios externos.")

    if "Ideación suicida" not in datos["clasificaciondelaconducta"].dropna().unique():
        raise ValueError("No se encontró la categoría 'Ideación suicida'.")

    categoria_adolescencia = "12 – 17 Adolescencia"
    if categoria_adolescencia not in datos["ciclovital"].dropna().unique():
        raise ValueError(f"No se encontró la categoría '{categoria_adolescencia}'.")

    filtro = (
        datos["clasificaciondelaconducta"].eq("Ideación suicida")
        & datos["ciclovital"].eq(categoria_adolescencia)
        & datos["ano_notificacion"].between(ano_inicial, ano_final)
    )

    datos_filtrados = datos.loc[filtro, ["ano_notificacion"] + FACTORES].copy()

    # Todos los años solicitados deben tener registros para evitar que la
    # persistencia se calcule sobre un periodo incompleto.
    anos_esperados = set(range(ano_inicial, ano_final + 1))
    anos_presentes = set(datos_filtrados["ano_notificacion"].unique())
    anos_sin_registros = sorted(anos_esperados - anos_presentes)
    if anos_sin_registros:
        raise ValueError(
            "No hay registros para los siguientes años del periodo: "
            f"{', '.join(map(str, anos_sin_registros))}"
        )

    return datos_filtrados


def validar_datos(datos):
    """Revisa columnas, valores faltantes y codificación binaria."""
    columnas_analisis = ["ano_notificacion"] + FACTORES
    faltantes = [columna for columna in columnas_analisis if columna not in datos.columns]

    if faltantes:
        raise ValueError(f"Faltan columnas requeridas: {', '.join(faltantes)}")
    if datos.empty:
        raise ValueError("El filtro definido no produjo registros.")

    reporte_faltantes = (
        datos[columnas_analisis].isna().sum().rename("Valores faltantes").to_frame()
    )
    columnas_con_nulos = reporte_faltantes.loc[
        reporte_faltantes["Valores faltantes"] > 0, "Valores faltantes"
    ].to_dict()
    if columnas_con_nulos:
        raise ValueError(
            "Se encontraron valores faltantes en las variables analizadas: "
            f"{columnas_con_nulos}. El análisis se detiene para no alterar "
            "los denominadores."
        )

    valores_invalidos = {}
    for factor in FACTORES:
        invalidos = sorted(set(datos[factor].unique()) - {0, 1})
        if invalidos:
            valores_invalidos[factor] = invalidos

    if valores_invalidos:
        raise ValueError(
            "Los factores deben contener únicamente 0 o 1. "
            "Se encontraron valores fuera del dominio binario: "
            f"{valores_invalidos}"
        )

    return reporte_faltantes
