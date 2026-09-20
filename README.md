## 1. Planteamiento del caso 

La conducta suicida constituye un problema de salud pública que requiere sistemas de vigilancia capaces de recopilar, analizar e interpretar información para apoyar la identificación de factores y circunstancias asociadas.

Este proyecto tiene como propósito realizar un análisis estadístico de los registros de conducta suicida reportados para Bogotá D.C., utilizando información proveniente de los registros de vigilancia epidemiológica gestionados por la Secretaría Distrital de Salud mediante el Subsistema de Vigilancia Epidemiológica de la Conducta Suicida (SISVECOS).
El análisis busca identificar las variables que mas imfluyen en el comportamiento de idealización suicida a través del tiempo para adolecentes entre 12 y 17 años tales como:

* Maltrato sexual.
* Muerte de un familiar.
* Conflictos de pareja.
* Problemas económicos.
* Problemas escolares o educativos.
* Problemas jurídicos.
* Problemas laborales.
* Suicidio de un amigo.

## 2. Pregunta de analisis
¿Qué factores desencadenantes predominan en los registros de ideación suicida notificados en adolescentes de 12 a 17 años en Bogotá entre 2017 y 2025?

## 3. Estructura del repositorio

```text
proyecto_analitica_datos/
├── README.md
├── requirements.txt
├── data/
│   └── osb_salud_mental_ideacion_e_intento.csv
├── Informe/
│   └── Aqui_va_el_pdf.pdf
├── notebooks/
│   └── analisis_factores_ideacion_suicida.ipynb
└── src/
   ├── __init__.py
   ├── estadistica.py
   ├── datos.py
   ├── indicadores.py
   └── visualizacion.py
```
## 4. Instruccionnes

## 5. Ajustes a la propuesta

Se ajusta el modelo estadístico que se aplicará en el presente estudio, incorporando las pruebas de Cochran Q y McNemar, con el propósito de identificar las tres variables predominantes. Asimismo, se actualiza el flujograma, manteniendo la misma información y los ajustes realizados en el análisis estadístico.
