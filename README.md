# Factores desencadenantes predominantes en registros de ideación suicida

**Autores:** Paola Yate Cuervo y Wilber Jonatan Plazas Murcia  
**Población:** adolescentes de 12 a 17 años en Bogotá  
**Periodo de análisis:** 2017–2025  

## 1. Planteamiento del caso 

La conducta suicida constituye un problema de salud pública que requiere sistemas de vigilancia capaces de recopilar, analizar e interpretar información para apoyar la identificación de factores y circunstancias asociadas.

Este proyecto tiene como propósito realizar un análisis estadístico de los registros de conducta suicida reportados para Bogotá D.C., utilizando información proveniente de los registros de vigilancia epidemiológica gestionados por la Secretaría Distrital de Salud mediante el Subsistema de Vigilancia Epidemiológica de la Conducta Suicida (SISVECOS).

El propósito es identificar cuáles de los siguientes nueve factores aparecen con mayor frecuencia en las notificaciones analizadas:
* Enfermedades dolorosas.
* Maltrato sexual.
* Muerte de un familiar.
* Conflictos de pareja.
* Problemas económicos.
* Problemas escolares o educativos.
* Problemas jurídicos.
* Problemas laborales.
* Suicidio de un amigo.

Los factores son variables binarias, donde 1 indica su presencia y 0 su ausencia.

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
   └── Factores_ideacion_suicida.pdf
   └── Diagrama_ideacion_suicida.drawio
   └── Diagrama_ideacion_suicida.jpg
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
-Descargar la carpeta del proyecto como ZIP.
-Descomprimir la carpeta.
-Abrir en Visual Studio Code la carpeta principal proyecto_analitica_datos.
-Abrir una terminal desde la raíz del proyecto.
-Instalar las dependencias con el siguiente comando:python -m pip install -r requirements.txt
-Abrir el Notebook analisis_factores_ideacion_suicida.ipynb
-Ejecutar todas las celdas con la opción Run All.

## 5. Ajustes a la propuesta

Se ajusta el modelo estadístico que se aplicará en el presente estudio, incorporando las pruebas de Cochran Q y McNemar, con el propósito de identificar las tres variables predominantes. Asimismo, se actualiza el flujograma, manteniendo la misma información y los ajustes realizados en el análisis estadístico.

## 6. Referencias

•	Secretaría Distrital de Salud de Bogotá. (s. f.). Conducta suicida en Bogotá D.C. Observatorio de Salud de Bogotá – SaluData. Conducta suicida en Bogotá D.C.

## 7. Declaración de uso de inteligencia artificial

Se utilizó asistencia de inteligencia artificial como apoyo para revisar, depurar y documentar el código. El contenido final fue revisado y adaptado por los autores.

