# Minería de asteroides: pipeline de Machine Learning

Challenge 1 (individual) — Machine Learning, Universidad Peruana Cayetano Heredia (UPCH). Caso asignado: **Tipo A, minería de asteroides**.

## Objetivo

Evaluar, con la información de una infografía (única fuente), qué condiciones tendrían que cumplirse para que la minería de asteroides sea económicamente viable y si esa información permite verificar que hoy se cumplen.

**Postura (hipótesis crítica):** no se considera demostrada la viabilidad económica actual. La infografía reporta avances tecnológicos y crecimiento *proyectado* del mercado, pero no costos, ingresos, riesgos ni plazos de retorno. Los resultados de este repositorio **no demuestran inviabilidad**; muestran qué falta para evaluarla con rigor.

## Entregables

| # | Entregable | Archivo |
|---|---|---|
| 1 | Presentación del caso y problema | [problema.txt](problema.txt) |
| 2 | Espacio de estados (con imagen) | [espacio_estados.md](espacio_estados.md), [imagenes/espacio_estados.png](imagenes/espacio_estados.png) |
| 3 | Pipeline de razonamiento y búsqueda | [pipeline_razonamiento.ipynb](pipeline_razonamiento.ipynb) |
| 4 | Pipeline de modelo predictivo (regresión) | [pipeline_prediccion.ipynb](pipeline_prediccion.ipynb) |

Abrir en Colab (reemplaza `TU_USUARIO` y `mineria-asteroides-ml` por los tuyos):

- [Notebook 3](https://colab.research.google.com/github/TU_USUARIO/mineria-asteroides-ml/blob/main/pipeline_razonamiento.ipynb)
- [Notebook 4](https://colab.research.google.com/github/TU_USUARIO/mineria-asteroides-ml/blob/main/pipeline_prediccion.ipynb)

## Resumen metodológico

1. **Problema:** distinguir crecimiento de mercado proyectado de rentabilidad real; listar variables conocidas y no reportadas.
2. **Espacio de estados:** 5 variables discretas (costo, recurso, éxito técnico, retorno, marco regulatorio), con estado inicial totalmente desconocido, operador `asignar(variable, nivel)` y restricciones.
3. **Búsqueda:** búsqueda en anchura (BFS) y en profundidad (DFS), con y sin poda, para hallar escenarios hipotéticos viables y las condiciones necesarias.
4. **Regresión:** experimento didáctico con **datos sintéticos** (supuestos explícitos), modelo lineal frente a Random Forest, y análisis de sensibilidad a los supuestos.

## Qué es dato y qué es supuesto

- **De la infografía:** mercado 2026 y 2030, CAGR, lanzamientos 2023, lista de incertidumbres.
- **Abstracciones/supuestos propios:** niveles de las variables, restricciones, fórmula de generación de datos sintéticos.
- **Simulado:** todo dato del notebook 4. Sus predicciones no representan la realidad.

## Estructura

```text
mineria-asteroides-ml/
├── README.md
├── problema.txt
├── espacio_estados.md
├── pipeline_razonamiento.ipynb
├── pipeline_prediccion.ipynb
├── requirements.txt
└── imagenes/
    ├── espacio_estados.png
    ├── busqueda_resultados.png
    └── prediccion_resultados.png
```

## Limitaciones

Variables discretas y supuestos didácticos; sin datos reales de costos o ingresos; los resultados dependen de los supuestos y no son pruebas científicas.
