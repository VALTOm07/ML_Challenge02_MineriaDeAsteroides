<div align="center">

  <img
    src="https://capsule-render.vercel.app/api?type=soft&color=0:0D1B2A,50:3C096C,100:0077B6&height=120&section=header&text=MINERIA%20DE%20ASTEROIDES&fontSize=30&fontColor=FFFFFF&animation=fadeIn"
    width="100%"
    alt="Encabezado espacial"
  />

  <p>
    <strong>Exploración de soluciones mediante Inteligencia Artificial</strong>
  </p>

  <img src="https://img.shields.io/badge/Machine-Learning-7B2CBF?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Algoritmo-BFS-0077B6?style=for-the-badge">
  <img src="https://img.shields.io/badge/Modelo-Regresión%20Lineal-2D6A4F?style=for-the-badge">

  <p>
    <em>¿Es viable la minería de asteroides? Exploremos el problema mediante búsqueda y predicción.</em>
  </p>

</div>

<div align="center">

  <img
    src="https://readme-typing-svg.demolab.com?font=Orbitron&size=24&duration=3000&pause=1000&color=FFBF00&center=true&vCenter=true&width=600&lines=Explorando+el+espacio;Buscando+soluciones+con+BFS;Prediciendo+con+Machine+Learning"
    alt="Texto animado del proyecto"
  />

</div>

<p align="center">
  <img
src="https://github.com/VALTOm07/ML_Challenge02_MineriaDeAsteroides/blob/main/assets/imagenes/infografia.png"
    alt="infografia_minAst"
    width="1000"
    >
</p>

Este repositorio explora cómo representar y analizar el problema de evaluar una misión hipotética de minería de asteroides mediante un espacio de estados, algoritmos de búsqueda y un experimento didáctico de regresión.

> **Postura del proyecto:** la información disponible no es suficiente para demostrar la viabilidad económica de una misión minera real. Esto no demuestra que sea inviable.

## 🧭 Navegación

- [Presentación del problema](problema.md)
- [Espacio de estados](espacio_estados.md)
- [Metodología](docs/metodologia.md)
- [Pipeline de búsqueda](pipeline_razonamiento.ipynb)
- [Pipeline de predicción](pipeline_prediccion.ipynb)
- [Aplicación interactiva](app.py)


<table>
  <tr>
    <td align="center" width="33%">
      <h3>🌌 Problema</h3>
      <p>Definición del escenario</p>
      <a href="problema.md">Explorar →</a>
    </td>
    <td align="center" width="33%">
      <h3>🔍 Búsqueda</h3>
      <p>Exploración mediante BFS</p>
      <a href="pipeline_razonamiento.ipynb">Explorar →</a>
    </td>
    <td align="center" width="33%">
      <h3>📈 Predicción</h3>
      <p>Modelo de regresión lineal</p>
      <a href="pipeline_prediccion.ipynb">Explorar →</a>
    </td>
  </tr>
</table>



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
├── problema.md
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
│       └── GIF_ESPACIAL.gif
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

- [Abrir pipeline de búsqueda en Colab](https://colab.research.google.com/github/VALTOm07/ML_Challenge02_MineriaDeAsteroides/blob/main/pipeline_razonamiento.ipynb)
- [Abrir pipeline de predicción en Colab](https://colab.research.google.com/github/VALTOm07/ML_Challenge02_MineriaDeAsteroides/blob/main/pipeline_prediccion.ipynb)

## ⚠️ Alcance y limitaciones

- La infografía es la única fuente factual externa sobre el caso utilizada en este proyecto.
- Los escenarios económicos son hipotéticos y sirven para explorar relaciones entre variables.
- La búsqueda encuentra rutas dentro de un modelo conceptual definido por el proyecto; no demuestra que una misión real sea viable.
- El modelo predictivo utiliza datos sintéticos. Sus métricas describen ese experimento artificial y no deben interpretarse como evidencia sobre la industria.
- Una evaluación económica real requeriría datos verificables de costos, recuperación de recursos, ingresos, riesgos técnicos, regulación e impacto ambiental.

## 🎓 Entregables académicos

| Entregable | Archivo |
|---|---|
| Presentación del caso y problema | `problema.md` |
| Espacio de estados | `espacio_estados.md` |
| Razonamiento, búsqueda y resultados | `pipeline_razonamiento.ipynb` |
| Modelo de regresión y visualización | `pipeline_prediccion.ipynb` |
| Experiencia interactiva | `app.py` |


<div align="center">
  <img
    src="https://github.com/VALTOm07/ML_Challenge02_MineriaDeAsteroides/blob/main/assets/imagenes/GIF_ESPACIAL.gif"
    width="100%"
    alt="Animación del espacio"
  />
</div>

