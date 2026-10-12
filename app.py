import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.simulacion import Escenario, clasificar_escenario
from src.busqueda import busqueda_anchura, NOMBRES_ESTADOS, GRAFO_ESTADOS
from src.modelo import generar_datos_sinteticos, entrenar_modelo

st.set_page_config(page_title="Minería de Asteroides | ML", page_icon="🚀", layout="wide")

st.markdown("""
<style>
.stApp { background: radial-gradient(circle at top right, #202b42 0, #0b1020 42%, #070a12 100%); color: #f7f7fb; }
h1, h2, h3 { color: #ffffff; }
[data-testid="stMetric"] { background: rgba(255,255,255,.06); border: 1px solid rgba(245,184,46,.35); padding: 14px; border-radius: 12px; }
div[data-testid="stTabs"] button { color: #f5b82e; }
.note { padding: 12px 16px; border-left: 4px solid #f5b82e; background: rgba(245,184,46,.09); border-radius: 6px; }
.small { color: #c4cada; font-size: .92rem; }
</style>
""", unsafe_allow_html=True)

st.title("🚀 Minería de Asteroides")
st.subheader("¿Oportunidad económica o riesgo financiero?")
st.markdown('<div class="note"><b>Enfoque:</b> explorar escenarios hipotéticos sin confundirlos con evidencia económica real. La información disponible no basta para demostrar la viabilidad ni la inviabilidad de una misión minera.</div>', unsafe_allow_html=True)
st.write("Panel académico interactivo · Machine Learning · UPCH · 2026-2")

tabs = st.tabs(["🪐 Introducción", "📊 Escenarios", "🧭 Espacio de estados", "🔎 Búsqueda", "🤖 Regresión", "🧾 Conclusiones"])

with tabs[0]:
    st.header("Lo que reporta la infografía")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Mercado 2026", "USD 2,49 mil M", help="Valor mostrado en la infografía.")
    c2.metric("Mercado 2030", "USD 5,42 mil M", help="Proyección mostrada en la infografía.")
    c3.metric("CAGR 2026–2030", "21,4 %", help="Tasa de crecimiento anual compuesta reportada.")
    c4.metric("Objetos espaciales (2023)", "3.143", help="La infografía reporta un aumento del 24 % respecto al año anterior.")
    st.markdown("### Datos, proyecciones y desconocidos")
    left, mid, right = st.columns(3)
    with left:
        st.success("**Reportado**\n\n3.143 objetos espaciales lanzados en 2023; aumento reportado del 24 %.")
    with mid:
        st.warning("**Proyección**\n\nMercado de USD 5,42 mil millones para 2030; CAGR de 21,4 %.")
    with right:
        st.error("**No cuantificado**\n\nCostos reales, rentabilidad de una misión, concentración de minerales y retorno de inversión.")
    st.markdown("### Flujo del proyecto")
    st.code("Caso → Problema → Espacio de estados → Búsqueda → Simulación → Regresión didáctica → Conclusiones", language="text")
    st.caption("El tamaño del mercado no equivale a ingresos netos de una misión minera.")

with tabs[1]:
    st.header("Explorador de escenarios económicos")
    st.caption("Todos los controles de esta sección son SUPUESTOS HIPOTÉTICOS. No son datos reales de la industria.")
    def restablecer_escenario():
        st.session_state["costo"] = 500
        st.session_state["ingresos"] = 800
        st.session_state["prob"] = 0.55
        st.session_state["tiempo"] = 8.0
    a, b = st.columns(2)
    with a:
        costo = st.slider("Costo hipotético de misión (unidades)", 0, 2000, 500, 25, key="costo")
        ingresos = st.slider("Ingresos potenciales hipotéticos (unidades)", 0, 2500, 800, 25, key="ingresos")
        prob = st.slider("Probabilidad hipotética de éxito", 0.0, 1.0, 0.55, 0.05, key="prob")
        tiempo = st.slider("Tiempo de recuperación hipotético (años)", 0.0, 30.0, 8.0, 0.5, key="tiempo")
        st.button("Restablecer valores iniciales", on_click=restablecer_escenario)
    escenario = Escenario(costo, ingresos, prob, tiempo)
    r = escenario.resultados()
    clas = clasificar_escenario(escenario)
    with b:
        st.subheader("Resultados de la simulación")
        st.metric("Beneficio si tiene éxito", f"{r['beneficio_si_exito']:,.1f} unidades")
        st.metric("Beneficio esperado simplificado", f"{r['beneficio_esperado']:,.1f} unidades")
        st.metric("ROI simplificado", "No calculable" if r["roi_simplificado_pct"] is None else f"{r['roi_simplificado_pct']:.1f}%")
        st.info(f"Clasificación del escenario: **{clas['estado']}**")
        st.write("Condiciones del modelo:")
        st.write(f"{'✅' if clas['cumple_probabilidad'] else '❌'} Probabilidad ≥ 50 % (umbral didáctico)")
        st.write(f"{'✅' if clas['cumple_tiempo'] else '❌'} Recuperación ≤ 10 años (umbral didáctico)")
        st.write(f"{'✅' if clas['beneficio_esperado_positivo'] else '❌'} Beneficio esperado positivo")
    fig, ax = plt.subplots()
    ax.bar(["Costo", "Ingresos × prob.", "Beneficio esperado"], [costo, ingresos * prob, r["beneficio_esperado"]])
    ax.axhline(0, linewidth=1)
    ax.set_ylabel("Unidades hipotéticas")
    ax.set_title("Componentes de la fórmula simplificada")
    fig.tight_layout()
    st.pyplot(fig)
    st.latex(r"E = p \\times I - C")
    st.write("Donde E = beneficio esperado simplificado, p = probabilidad hipotética de éxito, I = ingresos potenciales y C = costo de misión.")
    st.caption("La fórmula omite descuento temporal, financiación, impuestos y otros costos; no es una evaluación financiera completa.")

with tabs[2]:
    st.header("Espacio de estados")
    st.write("Selecciona un estado para consultar su significado y sus transiciones.")
    estado = st.selectbox("Estado", list(NOMBRES_ESTADOS.keys()), format_func=lambda x: f"{x} · {NOMBRES_ESTADOS[x]}")
    st.info(f"**{estado}: {NOMBRES_ESTADOS[estado]}**")
    st.write("Posibles estados siguientes:", ", ".join([f"{x} · {NOMBRES_ESTADOS[x]}" for x in GRAFO_ESTADOS[estado]]) or "No hay transiciones posteriores.")
    descriptions = {
        "S0": "La misión todavía no se ha evaluado.",
        "S1": "Se revisa la preparación tecnológica mediante un criterio hipotético.",
        "S2": "Se calculan indicadores económicos con parámetros supuestos.",
        "S3": "Se comprueban las restricciones seleccionadas para el escenario.",
        "S4": "Se cumplen los criterios didácticos configurados; no es una validación real.",
        "S5": "No se cumple alguna condición o falta evidencia para la evaluación conceptual.",
    }
    st.write(descriptions[estado])
    st.graphviz_chart("""digraph G { rankdir=LR; bgcolor="transparent"; node [shape=box, style="rounded,filled", fillcolor="#18243a", color="#f5b82e", fontcolor="white"]; edge [color="#f5b82e"]; S0 -> S1 -> S2 -> S3; S3 -> S4 [label="cumple"]; S3 -> S5 [label="no cumple"]; }""")

with tabs[3]:
    st.header("Simulador de búsqueda en anchura (BFS)")
    st.write("BFS recorre primero los estados más cercanos al inicio. En este grafo, encuentra una ruta por número de transiciones; no optimiza el valor económico.")
    objetivo = st.radio("Estado objetivo", ["S4", "S5"], format_func=lambda x: f"{x} · {NOMBRES_ESTADOS[x]}", horizontal=True)
    if st.button("Ejecutar búsqueda", type="primary"):
        resultado = busqueda_anchura("S0", objetivo)
        st.success("Objetivo encontrado en el grafo conceptual." if resultado["encontrado"] else "No se encontró una ruta.")
        st.write("**Orden visitado:**", " → ".join(resultado["visitados"]))
        st.write("**Camino:**", " → ".join(resultado["camino"]) if resultado["camino"] else "Sin camino")
        st.dataframe(pd.DataFrame({"Estado": resultado["visitados"], "Descripción": resultado["nombres_visitados"]}), use_container_width=True)
        st.caption("El camino refleja solo las transiciones programadas en este modelo académico.")

with tabs[4]:
    st.header("Experimento didáctico de regresión")
    st.warning("El conjunto de datos es sintético. Las métricas no describen ni predicen el desempeño de misiones reales.")
    df = generar_datos_sinteticos()
    modelo, metricas, pred, columnas = entrenar_modelo(df)
    c1, c2, c3 = st.columns(3)
    c1.metric("Filas sintéticas", len(df))
    c2.metric("MAE de prueba", f"{metricas['MAE']:.2f}")
    c3.metric("R² de prueba", f"{metricas['R2']:.3f}")
    st.write("La regresión lineal aprende una relación artificial entre costo, ingresos, probabilidad, tiempo y un índice de resultado creado por fórmula.")
    fig, ax = plt.subplots()
    ax.scatter(pred["real_sintetico"], pred["prediccion"], alpha=.7)
    minimo = min(pred.min())
    maximo = max(pred.max())
    ax.plot([minimo, maximo], [minimo, maximo], linestyle="--")
    ax.set_xlabel("Índice real sintético")
    ax.set_ylabel("Predicción del modelo")
    ax.set_title("Predicciones vs. valores sintéticos de prueba")
    fig.tight_layout()
    st.pyplot(fig)
    st.dataframe(df.head(10), use_container_width=True)
    st.caption("MAE mide el error absoluto medio; R² compara el ajuste con una referencia basada en la media. En datos sintéticos, estas métricas solo evalúan este ejercicio artificial.")

with tabs[5]:
    st.header("Conclusiones")
    st.markdown("""
- La infografía describe expectativas de crecimiento y avances tecnológicos.
- El crecimiento proyectado del mercado no demuestra la rentabilidad de una misión individual.
- Los costos reales, la cantidad recuperable de minerales, el éxito técnico y el retorno de inversión permanecen sin cuantificar en la fuente.
- La búsqueda demuestra cómo recorrer estados definidos, no cómo certificar una misión.
- La regresión sintética enseña el flujo de ML, pero no permite predecir la viabilidad económica real.
- Con la evidencia disponible, la viabilidad económica actual **no está demostrada**; tampoco queda demostrada la inviabilidad.
""")
    st.caption("Para una conclusión económica real harían falta datos verificables y comparables que no están incluidos en la infografía.")
