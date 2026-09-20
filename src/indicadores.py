"""Indicadores descriptivos y ranking de los factores."""

import pandas as pd

from .datos import ETIQUETAS_FACTORES, FACTORES


def calcular_indicadores(datos):
    """Calcula las frecuencias y proporciones globales y anuales."""
    total_registros = len(datos)
    resumen_global = pd.DataFrame({
        "factor": FACTORES,
        "Factor": [ETIQUETAS_FACTORES[factor] for factor in FACTORES],
        "Frecuencia": [int(datos[factor].sum()) for factor in FACTORES],
    })
    resumen_global["Proporción"] = resumen_global["Frecuencia"] / total_registros
    resumen_global = resumen_global.sort_values(
        ["Proporción", "Factor"], ascending=[False, True], ignore_index=True
    )

    frecuencias = datos.groupby("ano_notificacion")[FACTORES].sum()
    totales_anuales = datos.groupby("ano_notificacion").size()
    proporciones = frecuencias.div(totales_anuales, axis=0)

    resumen_anual = (
        frecuencias.stack()
        .rename("Frecuencia")
        .to_frame()
        .join(proporciones.stack().rename("Proporción"))
        .reset_index()
        .rename(columns={"ano_notificacion": "Año", "level_1": "factor"})
    )
    resumen_anual["Factor"] = resumen_anual["factor"].map(ETIQUETAS_FACTORES)

    return resumen_global, resumen_anual


def obtener_top3_anual(resumen_anual):
    """Selecciona exactamente tres factores por año.

    Se ordena primero por proporción anual descendente. Los empates exactos
    se resuelven alfabéticamente por el nombre del factor.
    """
    top3_anual = resumen_anual.sort_values(
        ["Año", "Proporción", "Factor"], ascending=[True, False, True]
    ).copy()
    top3_anual["Posición anual"] = top3_anual.groupby("Año").cumcount() + 1

    return top3_anual.loc[
        top3_anual["Posición anual"] <= 3
    ].reset_index(drop=True)


def generar_ranking(resumen_global, top3_anual, numero_anos):
    """Ordena los factores por proporción, persistencia y nombre.

    El criterio principal es la proporción global descendente; el secundario
    es el número de años en el top 3 descendente; y un empate exacto se
    resuelve alfabéticamente.
    """
    persistencia = (
        top3_anual.groupby("factor")
        .size()
        .rename("Años en top 3")
        .reset_index()
    )

    ranking = resumen_global.merge(persistencia, on="factor", how="left")
    ranking["Años en top 3"] = ranking["Años en top 3"].fillna(0).astype(int)
    ranking["Persistencia"] = ranking["Años en top 3"] / numero_anos
    ranking = ranking.sort_values(
        ["Proporción", "Años en top 3", "Factor"],
        ascending=[False, False, True],
        ignore_index=True,
    )
    ranking.insert(0, "Posición", range(1, len(ranking) + 1))
    ranking["Prioridad analítica"] = pd.cut(
        ranking["Posición"],
        bins=[0, 3, 6, 9],
        labels=["Alta", "Media", "Baja"],
    )

    return ranking
