"""Carga, selección, validación y filtro de los datos del proyecto."""

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
    """Carga el archivo CSV completo."""
    return pd.read_csv(ruta, sep=";")


def seleccionar_columnas(datos):
    """Conserva las tres variables de filtro y los nueve factores."""
    faltantes = [
        columna for columna in COLUMNAS_REQUERIDAS if columna not in datos.columns
    ]
    if faltantes:
        raise ValueError(f"Faltan columnas requeridas: {', '.join(faltantes)}")

    return datos[COLUMNAS_REQUERIDAS].copy()


def validar_datos(datos):
    """Valida columnas, nulos, categorías de filtro y factores binarios."""
    faltantes = [
        columna for columna in COLUMNAS_REQUERIDAS if columna not in datos.columns
    ]
    if faltantes:
        raise ValueError(f"Faltan columnas requeridas: {', '.join(faltantes)}")
    if datos.empty:
        raise ValueError("La base de datos no contiene registros.")

    # Las categorías usadas en el filtro deben existir con escritura exacta.
    categorias = {
        "clasificaciondelaconducta": "Ideación suicida",
        "ciclovital": "12 – 17 Adolescencia",
    }
    for columna, categoria in categorias.items():
        valores = datos[columna].astype(str)
        con_espacios = valores.str.strip().eq(categoria) & valores.ne(categoria)

        if con_espacios.any():
            raise ValueError(
                f"La categoría '{categoria}' contiene espacios externos en {columna}."
            )
        if categoria not in valores.unique():
            raise ValueError(
                f"No se encontró la categoría escrita exactamente como '{categoria}'."
            )

    # Los nulos se reportan y detienen el proceso para no alterar denominadores.
    reporte_faltantes = (
        datos[COLUMNAS_REQUERIDAS]
        .isna()
        .sum()
        .rename("Valores faltantes")
        .to_frame()
    )
    columnas_con_nulos = reporte_faltantes.loc[
        reporte_faltantes["Valores faltantes"] > 0, "Valores faltantes"
    ].to_dict()
    if columnas_con_nulos:
        raise ValueError(
            "Se encontraron valores faltantes: "
            f"{columnas_con_nulos}. El análisis se detiene para no alterar "
            "los denominadores."
        )

    # Cada factor debe contener exclusivamente 0 o 1.
    valores_invalidos = {}
    for factor in FACTORES:
        invalidos = sorted(set(datos[factor].unique()) - {0, 1})
        if invalidos:
            valores_invalidos[factor] = invalidos

    if valores_invalidos:
        raise ValueError(
            "Los factores deben contener únicamente 0 o 1. "
            "Valores fuera del dominio binario: "
            f"{valores_invalidos}"
        )

    return reporte_faltantes


def filtrar_poblacion(datos, ano_inicial, ano_final):
    """Selecciona ideación suicida, adolescencia y el periodo definido."""
    if ano_inicial > ano_final:
        raise ValueError("El año inicial no puede ser mayor que el año final.")

    filtro = (
        datos["clasificaciondelaconducta"].eq("Ideación suicida")
        & datos["ciclovital"].eq("12 – 17 Adolescencia")
        & datos["ano_notificacion"].between(ano_inicial, ano_final)
    )
    datos_filtrados = datos.loc[
        filtro, ["ano_notificacion"] + FACTORES
    ].copy()

    # Se exige información para todos los años solicitados.
    anos_esperados = set(range(ano_inicial, ano_final + 1))
    anos_presentes = set(datos_filtrados["ano_notificacion"].unique())
    anos_sin_registros = sorted(anos_esperados - anos_presentes)
    if anos_sin_registros:
        raise ValueError(
            "No hay registros para los siguientes años del periodo: "
            f"{', '.join(map(str, anos_sin_registros))}"
        )

    return datos_filtrados
