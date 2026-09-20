"""Tres gráficos del proyecto elaborados con Seaborn."""

import matplotlib.pyplot as plt
import seaborn as sns


def grafico_ranking_global(ranking):
    """Muestra la proporción global de los nueve factores."""
    datos = ranking.sort_values("Proporción")

    plt.figure(figsize=(10, 6))
    sns.barplot(data=datos, x="Proporción", y="Factor", color="#0B6E99")
    plt.title("Proporción global de factores desencadenantes")
    plt.xlabel("Proporción de notificaciones")
    plt.ylabel("")
    plt.tight_layout()
    plt.show()


def grafico_evolucion_top3(resumen_anual, factores_top3):
    """Muestra la evolución anual de los tres factores principales."""
    datos = resumen_anual.loc[resumen_anual["factor"].isin(factores_top3)]

    plt.figure(figsize=(10, 6))
    sns.lineplot(
        data=datos,
        x="Año",
        y="Proporción",
        hue="Factor",
        marker="o",
    )
    plt.title("Evolución anual de los tres factores principales")
    plt.xlabel("Año de notificación")
    plt.ylabel("Proporción")
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()


def grafico_mapa_calor_anual(resumen_anual):
    """Muestra las proporciones anuales de los nueve factores."""
    tabla = resumen_anual.pivot(index="Factor", columns="Año", values="Proporción")
    tabla = tabla.loc[tabla.mean(axis=1).sort_values(ascending=False).index]

    plt.figure(figsize=(11, 7))
    sns.heatmap(
        tabla,
        cmap="YlGnBu",
        annot=True,
        fmt=".1%",
        cbar_kws={"label": "Proporción"},
    )
    plt.title("Proporción anual de los nueve factores desencadenantes")
    plt.xlabel("Año de notificación")
    plt.ylabel("")
    plt.tight_layout()
    plt.show()
