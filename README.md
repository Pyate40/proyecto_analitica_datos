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

## Flujo del proyecto

1. Cargar las doce columnas necesarias del CSV.
2. Filtrar ideación suicida, ciclo vital de adolescencia y años 2017-2025.
3. Validar valores faltantes y la codificación 0/1 de los factores.
4. Calcular frecuencias y proporciones globales y anuales.
5. Identificar el top 3 de cada año y calcular su persistencia.
6. Generar el ranking final y la prioridad analítica.
7. Aplicar la Q de Cochran y comparaciones de McNemar con ajuste de Holm.
8. Mostrar gráficos
9. Ejecutar escenario  de vertificación
