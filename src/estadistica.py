"""Pruebas estadísticas para los nueve factores binarios."""

from itertools import combinations

import pandas as pd
from statsmodels.stats.contingency_tables import cochrans_q, mcnemar
from statsmodels.stats.multitest import multipletests

from .datos import ETIQUETAS_FACTORES


def prueba_cochran(datos, factores, alfa=0.05):
    """Evalúa si los factores presentan la misma proporción de valores 1.

    H0: los factores tienen la misma proporción registrada.
    H1: al menos un factor tiene una proporción diferente.
    """
    casos_completos = datos[factores].dropna()
    resultado = cochrans_q(casos_completos.to_numpy())

    return pd.DataFrame({
        "Estadístico Q": [resultado.statistic],
        "Grados de libertad": [len(factores) - 1],
        "p-valor": [resultado.pvalue],
        "N utilizado": [len(casos_completos)],
        "Decisión": [
            "Rechazar H0" if resultado.pvalue < alfa else "No rechazar H0"
        ],
    })


def comparar_mcnemar(datos, factores, alfa=0.05):
    """Compara por parejas los factores del top 3 después de Cochran.

    H0 por pareja: ambos factores tienen la misma proporción registrada.
    Los p-valores se ajustan con Holm para controlar las comparaciones múltiples.
    """
    resultados = []

    for factor_a, factor_b in combinations(factores, 2):
        pares = datos[[factor_a, factor_b]].dropna()
        tabla = pd.crosstab(pares[factor_a], pares[factor_b]).reindex(
            index=[0, 1], columns=[0, 1], fill_value=0
        )
        prueba = mcnemar(tabla, exact=False, correction=True)

        resultados.append({
            "Factor A": ETIQUETAS_FACTORES[factor_a],
            "Factor B": ETIQUETAS_FACTORES[factor_b],
            "Estadístico": prueba.statistic,
            "p-valor": prueba.pvalue,
            "N utilizado": len(pares),
        })

    resultados = pd.DataFrame(resultados)
    rechazar, p_ajustados, _, _ = multipletests(
        resultados["p-valor"], alpha=alfa, method="holm"
    )
    resultados["p-valor ajustado (Holm)"] = p_ajustados
    resultados["Decisión"] = [
        "Rechazar H0" if valor else "No rechazar H0" for valor in rechazar
    ]

    return resultados
