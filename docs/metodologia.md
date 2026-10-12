# Metodología y límites

## 1. Fuentes y trazabilidad

La única fuente factual del caso es la infografía entregada en la actividad. No se incorporan datos externos sobre la industria. Los números de escenarios, umbrales y datos del experimento predictivo se identifican como hipotéticos o sintéticos.

## 2. Simulación económica

Se calcula:

- Beneficio si la misión tiene éxito = ingresos potenciales − costo de misión.
- Beneficio esperado simplificado = probabilidad de éxito × ingresos potenciales − costo de misión.
- ROI simplificado = (beneficio esperado / costo de misión) × 100, cuando el costo es mayor que cero.

Esta fórmula simplificada no incluye flujos de caja descontados, impuestos, financiación, costos de oportunidad, costos posteriores ni valor temporal del dinero. Por ello, el resultado es solo un indicador didáctico y no un análisis financiero real.

## 3. Búsqueda

Se utiliza búsqueda en anchura (BFS) para recorrer el grafo conceptual desde el estado inicial. En este grafo pequeño, BFS permite mostrar orden de visita y camino hasta un estado final. No optimiza la economía de la misión; únicamente encuentra una ruta según las transiciones definidas.

## 4. Experimento de regresión

Se generan datos sintéticos reproducibles. La variable objetivo representa un índice hipotético de resultado económico creado para enseñar el flujo de preparación, división de datos, entrenamiento, evaluación y visualización. No es una variable observada en misiones reales ni se debe interpretar como predicción de la industria.

Se usa regresión lineal porque permite inspeccionar la relación entre variables numéricas y explicar sus coeficientes de forma introductoria. Se reportan MAE y R² sobre una partición de prueba. Un buen resultado sobre datos sintéticos solo indica que el modelo recupera parcialmente el patrón artificial definido en la generación.

## 5. Limitaciones

- No existen datos reales de costos, concentración de recursos o ingresos de una misión en la fuente disponible.
- Los escenarios económicos no son pronósticos.
- Las reglas del espacio de estados son académicas.
- Las métricas del modelo sintético no validan hipótesis sobre la viabilidad de la minería de asteroides.
