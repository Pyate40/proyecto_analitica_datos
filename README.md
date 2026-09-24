# Factores desencadenantes predominantes en registros de ideación suicida

**Autores:** Wilber Jonatan Plazas Murcia y Paola Yate Cuervo  
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

## 2. Pregunta de análisis
¿Qué factores desencadenantes predominan en los registros de ideación suicida notificados en adolescentes de 12 a 17 años en Bogotá entre 2017 y 2025?

## 3. Metodología

El proyecto desarrolla las siguientes etapas:

1. Carga de la base de datos completa.
2. Selección de las doce columnas necesarias.
3. Validación de columnas, valores faltantes, categorías de filtro y factores binarios.
4. Filtro de ideación suicida, adolescencia y periodo 2017–2025.
5. Cálculo de frecuencias y proporciones globales y anuales.
6. Aplicación de la prueba Q de Cochran a los nueve factores.
7. Elaboración del ranking y selección de los tres factores principales.
8. Comparación del top 3 mediante la prueba de McNemar con ajuste de Holm.
9. Presentación de tablas, gráficos y conclusiones.

## 4. Estructura del repositorio

```text
proyecto_analitica_datos/
├── README.md
├── requirements.txt
├── data/
│   └── osb_salud_mental_ideacion_e_intento.csv
├── figuras/
│   ├── figura_1_proporcion_global.png
│   ├── figura_2_mapa_calor_anual.png
│   └── figura_3_evolucion_top3.png
├── informe/
│   ├── Informe_factores_ideacion_suicida.pdf
│   ├── Diagrama_ideacion_suicida.drawio
│   └── Diagrama_ideacion_suicida.jpg
├── notebooks/
│   └── analisis_factores_ideacion_suicida.ipynb
└── src/
    ├── __init__.py
    ├── datos.py
    ├── indicadores.py
    ├── estadistica.py
    └── visualizacion.py
```
## 5. Instrucciones
1. Descargar la carpeta del proyecto como archivo ZIP.
2. Descomprimir la carpeta.
3. Abrir en Visual Studio Code la carpeta principal proyecto_analitica_datos.
4. Abrir una terminal desde la raíz del proyecto.
5. Instalar las dependencias abriendo una nueva terminal, validando que la ruta este en la carpeta del proyecto y ejecutar el siguiente comando: py -m pip install -r requirements.txt
6. Abrir el notebook analisis_factores_ideacion_suicida.ipynb.
7. Ejecutar todas las celdas con la opción Run All.

## 6. Ajustes a la propuesta

- Se incorporaron las pruebas Q de Cochran y McNemar como soporte estadístico para comparar las proporciones de los factores.
- Se definió una regla completa para el ranking: proporción global, persistencia anual y orden alfabético en caso de empate exacto.
- Se actualizó el diagrama de flujo para que represente el orden real de ejecución del notebook.

## 7. Referencias

- Secretaría Distrital de Salud de Bogotá. (s. f.). *Conducta suicida en Bogotá D. C.* Observatorio de Salud de Bogotá, SaluData.  
  https://saludata.saludcapital.gov.co/osb/indicadores/conducta-suicida/

- Secretaría de Educación del Distrito. (s. f.). *Conducta suicida*. Observatorio de Convivencia Escolar.  
  https://oce.educacionbogota.edu.co/conducta-suicida

- Secretaría de Educación del Distrito. (s. f.). *Protocolos de atención*. Oficina de Convivencia Escolar.  
  https://oce.educacionbogota.edu.co/protocolos-de-atencion

## 8. Declaración de uso de inteligencia artificial

Se utilizó asistencia de inteligencia artificial como apoyo para revisar, depurar y documentar el código. El contenido final fue revisado y adaptado por los autores.

