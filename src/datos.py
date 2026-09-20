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
    """Carga todas las columnas disponibles en el archivo CSV."""
    return pd.read_csv(ruta, sep=";")


def seleccionar_columnas(datos):
    """Conserva las tres variables de filtro y los nueve factores analizados."""
    faltantes = [
        columna for columna in COLUMNAS_REQUERIDAS if columna not in datos.columns
    ]

    if faltantes:
        raise ValueError(f"Faltan columnas requeridas: {', '.join(faltantes)}")

    return datos[COLUMNAS_REQUERIDAS].copy()


def filtrar_poblacion(datos, ano_inicial, ano_final):
    """Selecciona ideación suicida, adolescencia y el periodo definido."""
    if ano_inicial > ano_final:
        raise ValueError("El año inicial no puede ser mayor que el año final.")

    categoria_adolescencia = "12 – 17 Adolescencia"
    filtro = (
        datos["clasificaciondelaconducta"].eq("Ideación suicida")
        & datos["ciclovital"].eq(categoria_adolescencia)
        & datos["ano_notificacion"].between(ano_inicial, ano_final)
    )

    return datos.loc[filtro, ["ano_notificacion"] + FACTORES].copy()


def validar_datos(datos):
    """Revisa columnas, nulos, categorías de filtro y valores binarios."""
    faltantes = [
        columna for columna in COLUMNAS_REQUERIDAS if columna not in datos.columns
    ]

    if faltantes:
        raise ValueError(f"Faltan columnas requeridas: {', '.join(faltantes)}")
    if datos.empty:
        raise ValueError("La base de datos no contiene registros.")

    # Las categorías utilizadas en el filtro deben aparecer con la escritura exacta.
    categorias = {
        "clasificaciondelaconducta": "Ideación suicida",
        "ciclovital": "12 – 17 Adolescencia",
    }
    for columna, categoria in categorias.items():
        valores = datos[columna].dropna().astype(str)
        variantes = valores[valores.str.strip().eq(categoria) & valores.ne(categoria)]

        if not variantes.empty:
            raise ValueError(
                f"La categoría '{categoria}' contiene espacios externos en {columna}."
            )
        if categoria not in valores.unique():
            raise ValueError(
                f"No se encontró la categoría escrita exactamente como '{categoria}'."
            )

    valores_invalidos = {}
    for factor in FACTORES:
        invalidos = sorted(set(datos[factor].dropna().unique()) - {0, 1})
        if invalidos:
            valores_invalidos[factor] = invalidos

    if valores_invalidos:
        raise ValueError(
            "Los factores deben contener únicamente 0, 1 o valores faltantes: "
            f"{valores_invalidos}"
        )

    return (
        datos[COLUMNAS_REQUERIDAS]
        .isna()
        .sum()
        .rename("Valores faltantes")
        .to_frame()
    )
