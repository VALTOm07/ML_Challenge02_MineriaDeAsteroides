# 🚀 Minería de Asteroides: ¿Oportunidad económica o riesgo financiero?

Proyecto académico de Machine Learning — UPCH, 2026-2.

Este repositorio explora cómo representar y analizar el problema de evaluar una misión hipotética de minería de asteroides mediante un espacio de estados, algoritmos de búsqueda y un experimento didáctico de regresión.

> **Postura del proyecto:** la información disponible no es suficiente para demostrar la viabilidad económica de una misión minera real. Esto no demuestra que sea inviable.

## 🧭 Navegación

- [Presentación del problema](problema.txt)
- [Espacio de estados](espacio_estados.md)
- [Metodología](docs/metodologia.md)
- [Pipeline de búsqueda](pipeline_razonamiento.ipynb)
- [Pipeline de predicción](pipeline_prediccion.ipynb)
- [Aplicación interactiva](app.py)

## 📌 Datos del caso

Los valores siguientes proceden únicamente de la infografía proporcionada para la actividad:

| Indicador | Valor | Tipo |
|---|---:|---|
| Mercado en 2026 | USD 2,49 mil millones | Reportado en la infografía |
| Mercado en 2030 | USD 5,42 mil millones | Proyección |
| CAGR 2026–2030 | 21,4 % | Proyección |
| Objetos espaciales lanzados en 2023 | 3.143 | Reportado |
| Variación respecto al año anterior | +24 % | Reportado |

El crecimiento del mercado y la cantidad de objetos espaciales no miden directamente la rentabilidad de una misión minera. Los costos, ingresos de una misión, probabilidad de éxito y plazo de recuperación se tratarán como **supuestos de simulación**, no como datos reales.

## 🧪 ¿Qué incluye?

1. **Problema:** definición y motivación del análisis.
2. **Espacio de estados:** estados, operadores, restricciones y transiciones.
3. **Búsqueda:** búsqueda en anchura (BFS) sobre estados de evaluación de una misión hipotética.
4. **Predicción:** regresión lineal sobre datos sintéticos para enseñar el pipeline, no para predecir la rentabilidad real de la industria.
5. **Aplicación Streamlit:** panel visual con explorador económico, espacio de estados, búsqueda y experimento predictivo.

## 🗂️ Estructura

```text
mineria-asteroides-ml/
├── README.md
├── problema.txt
├── espacio_estados.md
├── pipeline_razonamiento.ipynb
├── pipeline_prediccion.ipynb
├── app.py
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── busqueda.py
│   ├── simulacion.py
│   └── modelo.py
├── assets/
│   └── imagenes/
│       └── infografia.png
└── docs/
    └── metodologia.md
```

## ▶️ Ejecutar la aplicación

Requiere Python 3.10 o superior recomendado.

```bash
python -m venv .venv
```

En Windows:

```bash
.venv\Scripts\activate
```

En macOS/Linux:

```bash
source .venv/bin/activate
```

Instala dependencias y ejecuta:

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 📓 Google Colab

Sube cada notebook a tu repositorio de GitHub y ábrelo desde Google Colab con **Archivo → Abrir cuaderno → GitHub**, pegando la URL real del repositorio. Los enlaces directos de Colab se añadirán cuando el repositorio esté publicado; no se incluyen enlaces ficticios.

## ⚠️ Alcance y limitaciones

- La infografía es la única fuente factual externa sobre el caso utilizada en este proyecto.
- Los escenarios económicos son hipotéticos y sirven para explorar relaciones entre variables.
- La búsqueda encuentra rutas dentro de un modelo conceptual definido por el proyecto; no demuestra que una misión real sea viable.
- El modelo predictivo utiliza datos sintéticos. Sus métricas describen ese experimento artificial y no deben interpretarse como evidencia sobre la industria.
- Una evaluación económica real requeriría datos verificables de costos, recuperación de recursos, ingresos, riesgos técnicos, regulación e impacto ambiental.

## 🎓 Entregables académicos

| Entregable | Archivo |
|---|---|
| Presentación del caso y problema | `problema.txt` |
| Espacio de estados | `espacio_estados.md` |
| Razonamiento, búsqueda y resultados | `pipeline_razonamiento.ipynb` |
| Modelo de regresión y visualización | `pipeline_prediccion.ipynb` |
| Experiencia interactiva | `app.py` |
