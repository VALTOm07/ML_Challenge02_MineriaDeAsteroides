
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from src.simulacion import Escenario, clasificar_escenario
from src.busqueda import busqueda_anchura, NOMBRES_ESTADOS, GRAFO_ESTADOS
from src.modelo import generar_datos_sinteticos, entrenar_modelo


# --------------------------------------------------
# Configuración
# --------------------------------------------------

st.set_page_config(
    page_title="Minería de Asteroides | Machine Learning",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Minería de Asteroides")
st.caption(
    "Exploración de escenarios mediante búsqueda en espacios de estados "
    "y un modelo predictivo de regresión."
)

st.info(
    "Este proyecto es educativo. Los escenarios y datos sintéticos "
    "no demuestran la rentabilidad real de una misión minera."
)


# --------------------------------------------------
# Pestañas principales
# --------------------------------------------------

tab_inicio, tab_escenarios, tab_estados, tab_busqueda, tab_modelo, tab_conclusiones = (
    st.tabs([
        "Inicio",
        "Escenarios",
        "Espacio de estados",
        "Búsqueda BFS",
        "Modelo predictivo",
        "Conclusiones"
    ])
)


# --------------------------------------------------
# 1. Inicio
# --------------------------------------------------

with tab_inicio:
    st.header("Contexto del problema")

    st.write(
        "La minería de asteroides plantea la posibilidad de obtener recursos "
        "de cuerpos celestes. Sin embargo, evaluar una misión requiere "
        "considerar costos, ingresos potenciales, probabilidad de éxito, "
        "tiempo de recuperación y restricciones tecnológicas."
    )

    st.subheader("Datos de referencia")

    col1, col2, col3 = st.columns(3)

    col1.metric("Mercado en 2026", "USD 2.49 mil millones")
    col2.metric("Estimación para 2030", "USD 5.42 mil millones")
    col3.metric("Crecimiento estimado", "21.4 %")

    st.caption(
        "Cifras de referencia de la infografía utilizada en el proyecto. "
        "El crecimiento del mercado no implica que una misión específica "
        "sea rentable."
    )

    st.subheader("¿Por qué utilizar IA y Machine Learning?")

    st.write(
        "- **Búsqueda:** permite explorar rutas posibles entre estados "
        "de evaluación de una misión.\n"
        "- **Regresión:** permite estudiar relaciones entre variables "
        "y un índice de resultado hipotético.\n"
        "- **Limitación:** los resultados dependen de los criterios "
        "y los datos utilizados."
    )


# --------------------------------------------------
# 2. Evaluación de escenarios
# --------------------------------------------------

with tab_escenarios:
    st.header("Evaluación de un escenario hipotético")

    st.write(
        "Modifica las variables para observar cómo se evalúa un escenario. "
        "Los valores no representan una misión real."
    )

    col1, col2 = st.columns(2)

    with col1:
        costo = st.slider(
            "Costo de misión (unidades hipotéticas)",
            min_value=100,
            max_value=1000,
            value=500,
            step=50
        )

        ingreso = st.slider(
            "Ingreso potencial (unidades hipotéticas)",
            min_value=150,
            max_value=1500,
            value=800,
            step=50
        )

    with col2:
        prob_exito = st.slider(
            "Probabilidad de éxito",
            min_value=0.15,
            max_value=0.95,
            value=0.55,
            step=0.05
        )

        tiempo = st.slider(
            "Tiempo de recuperación (años hipotéticos)",
            min_value=2,
            max_value=20,
            value=8,
            step=1
        )

    escenario = Escenario(
        costo=costo,
        ingresos=ingreso,
        prob_exito=prob_exito,
        tiempo=tiempo
    )

    resultados = escenario.resultados()
    clasificacion = clasificar_escenario(escenario)

    st.subheader("Resultados")

    st.write(resultados)
    st.write("**Clasificación del escenario:**", clasificacion)

    st.latex(r"E = p \times I - C")

    st.caption(
        "E representa el beneficio esperado simplificado, p la probabilidad "
        "de éxito, I el ingreso potencial y C el costo. La fórmula no "
        "incluye todos los costos, riesgos ni el valor del dinero en el tiempo."
    )


# --------------------------------------------------
# 3. Espacio de estados
# --------------------------------------------------

with tab_estados:
    st.header("Representación del espacio de estados")

    st.write(
        "Cada estado representa una etapa de evaluación. Las transiciones "
        "hacia S5 permiten representar situaciones en las que la evidencia "
        "es insuficiente o no se cumplen los criterios."
    )

    estado_seleccionado = st.selectbox(
        "Selecciona un estado",
        options=list(NOMBRES_ESTADOS.keys()),
        format_func=lambda estado: (
            f"{estado}: {NOMBRES_ESTADOS[estado]}"
        )
    )

    st.subheader("Estado seleccionado")
    st.write(f"**{estado_seleccionado}:** {NOMBRES_ESTADOS[estado_seleccionado]}")

    sucesores = GRAFO_ESTADOS.get(estado_seleccionado, [])

    if sucesores:
        st.write("**Estados siguientes posibles:**")
        for sucesor in sucesores:
            st.write(f"- {sucesor}: {NOMBRES_ESTADOS[sucesor]}")
    else:
        st.write("Este estado no tiene transiciones posteriores.")

    st.subheader("Grafo de transiciones")

    st.graphviz_chart(
        """
        digraph G {
            rankdir=LR;
            bgcolor="transparent";

            node [
                shape=box,
                style="rounded,filled",
                fillcolor="#18243a",
                color="#f5b82e",
                fontcolor="white"
            ];

            edge [
                color="#f5b82e",
                fontcolor="white"
            ];

            S0 [label="S0: Inicio"];
            S1 [label="S1: Tecnología revisada"];
            S2 [label="S2: Economía calculada"];
            S3 [label="S3: Restricciones revisadas"];
            S4 [label="S4: Evaluación favorable"];
            S5 [label="S5: Más evidencia"];

            S0 -> S1 [label="continúa"];
            S0 -> S5 [label="evidencia insuficiente"];

            S1 -> S2 [label="datos suficientes"];
            S1 -> S5 [label="revisar"];

            S2 -> S3 [label="continúa"];
            S2 -> S5 [label="revisar"];

            S3 -> S4 [label="cumple"];
            S3 -> S5 [label="no cumple"];
        }
        """
    )

    st.caption(
        "El grafo representa alternativas conceptuales. Las transiciones "
        "no se deciden automáticamente a partir de datos reales."
    )


# --------------------------------------------------
# 4. Búsqueda BFS
# --------------------------------------------------

with tab_busqueda:
    st.header("Exploración mediante búsqueda en anchura")

    st.write(
        "BFS (Breadth-First Search) explora primero los estados más cercanos "
        "al estado inicial. En este proyecto se utiliza para recorrer "
        "el grafo conceptual."
    )

    estado_inicial = st.selectbox(
        "Estado inicial",
        options=list(NOMBRES_ESTADOS.keys()),
        index=0,
        key="estado_inicial_bfs"
    )

    if st.button("Ejecutar búsqueda BFS"):
        resultado_busqueda = busqueda_anchura(
            inicio=estado_inicial,
            objetivo="S4",
            grafo=GRAFO_ESTADOS
        )

        st.subheader("Resultado de la búsqueda")
        st.write(resultado_busqueda)

        st.caption(
            "BFS encuentra una ruta según las conexiones del grafo; "
            "no determina por sí solo la viabilidad económica o tecnológica "
            "de una misión."
        )


# --------------------------------------------------
# 5. Modelo predictivo
# --------------------------------------------------

with tab_modelo:
    st.header("Modelo predictivo de regresión")

    st.write(
        "Se utiliza regresión lineal para estudiar la relación entre "
        "variables hipotéticas de una misión y un índice de resultado "
        "generado mediante una fórmula sintética."
    )

    if st.button("Entrenar modelo de regresión"):
        df = generar_datos_sinteticos()
        modelo, metricas, pred, columnas = entrenar_modelo(df)

        st.subheader("Datos sintéticos")
        st.dataframe(df.head(10), use_container_width=True)

        st.caption(
            f"Variables utilizadas por el modelo: {', '.join(columnas)}"
        )

        st.subheader("Métricas de evaluación")

        if isinstance(metricas, dict):
            col_metricas = st.columns(len(metricas))

            for columna, (nombre, valor) in zip(col_metricas, metricas.items()):
                columna.metric(nombre, f"{valor:.3f}")
        else:
            st.write(metricas)

        st.subheader("Valores reales frente a predicciones")

        if {"real_sintetico", "prediccion"}.issubset(pred.columns):
            fig, ax = plt.subplots()

            ax.scatter(
                pred["real_sintetico"],
                pred["prediccion"],
                alpha=0.7
            )

            minimo = min(
                pred["real_sintetico"].min(),
                pred["prediccion"].min()
            )

            maximo = max(
                pred["real_sintetico"].max(),
                pred["prediccion"].max()
            )

            ax.plot(
                [minimo, maximo],
                [minimo, maximo],
                linestyle="--"
            )

            ax.set_xlabel("Valor real sintético")
            ax.set_ylabel("Predicción del modelo")
            ax.set_title("Valores reales frente a predicciones")
            ax.grid(True, alpha=0.3)

            st.pyplot(fig)
            plt.close(fig)

            st.caption(
                "Cuanto más cerca estén los puntos de la línea discontinua, "
                "más próximas serán las predicciones a los valores sintéticos."
            )
        else:
            st.warning(
                "No se encontraron las columnas esperadas para graficar. "
                "Verifica que src/modelo.py devuelva las columnas "
                "'real_sintetico' y 'prediccion'."
            )

        st.subheader("Interpretación")

        st.write(
            "El modelo aprende patrones presentes en los datos sintéticos. "
            "Las métricas evalúan su desempeño sobre esos datos, pero no "
            "validan predicciones sobre misiones reales de minería espacial."
        )


# --------------------------------------------------
# 6. Conclusiones
# --------------------------------------------------

with tab_conclusiones:
    st.header("Conclusiones")

    st.write(
        "- El espacio de estados permite representar las etapas y "
        "alternativas de evaluación de una misión.\n"
        "- BFS permite explorar las rutas disponibles en el grafo, "
        "sin evaluar por sí mismo los criterios de viabilidad.\n"
        "- La regresión lineal permite analizar relaciones en un conjunto "
        "de datos sintéticos.\n"
        "- Los resultados son demostrativos: para evaluar una misión real "
        "se necesitarían datos técnicos, económicos y científicos "
        "verificados."
    )

    st.warning(
        "No se puede concluir que la minería de asteroides sea rentable "
        "o no rentable a partir de esta simulación."
    )
