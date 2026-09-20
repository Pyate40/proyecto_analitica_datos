# Proyecto de Programación para Analítica de Datos

## Factores desencadenantes predominantes en registros de ideación suicida en adolescentes de Bogotá, 2017-2025

**Autores:** Paola Yate Cuervo y Wilber Jonatan Plazas Murcia.

## Pregunta principal

¿Qué factores desencadenantes predominan en los registros de ideación suicida notificados en adolescentes de 12 a 17 años en Bogotá entre 2017 y 2025?

## Alcance

- Unidad de análisis: registro de notificación.
- Conducta: ideación suicida.
- Ciclo vital: 12 a 17 años.
- Periodo: 2017-2025.
- Variables analizadas: nueve factores binarios.
- Un registro puede presentar varios factores simultáneamente, por eso sus proporciones no tienen que sumar 100 %.

- ## Flujo del proyecto

1. Cargar las doce columnas necesarias del CSV.
2. Filtrar ideación suicida, ciclo vital de adolescencia y años 2017-2025.
3. Validar valores faltantes y la codificación 0/1 de los factores.
4. Calcular frecuencias y proporciones globales y anuales.
5. Identificar el top 3 de cada año y calcular su persistencia.
6. Generar el ranking final y la prioridad analítica.
7. Aplicar la Q de Cochran y comparaciones de McNemar con ajuste de Holm.
8. Mostrar gráficos
9. Ejecutar escenario  de vertificación

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

proyecto_analitica_datos/
│
├── README.md
├── requirements.txt
│
├── data/
│   ├── osb_salud_mental_ideacion_e_intento.csv/
│
├── Informe/
│   ├── Aqui va el pdf/
│
│
├── notebooks/
│   ├── analisis_factores_ideacion_suicida.ipynb 
│   
│
├── src/
│   ├── __init__
│   ├── estadistica.py
│   └── datos.py
│   └── indicadores.py
│   └── visualizacion.py

## 4. 

## ajustes a la propuesta

Se ajusta el modelo estadístico que se aplicará en el presente estudio, incorporando las pruebas de Cochran Q y McNemar, con el propósito de identificar las tres variables predominantes. Asimismo, se actualiza el flujograma, manteniendo la misma información y los ajustes realizados en el análisis estadístico.
