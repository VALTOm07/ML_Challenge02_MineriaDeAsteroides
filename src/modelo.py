"""Experimento de regresión lineal con datos sintéticos."""
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

def generar_datos_sinteticos(n=240, random_state=42):
    """Datos inventados con fines didácticos; no representan misiones reales."""
    rng = np.random.default_rng(random_state)
    costo = rng.uniform(100, 1000, n)                 # unidades monetarias hipotéticas
    ingresos = rng.uniform(150, 1500, n)              # unidades monetarias hipotéticas
    prob_exito = rng.uniform(0.15, 0.95, n)
    tiempo = rng.uniform(2, 20, n)                    # años hipotéticos
    ruido = rng.normal(0, 70, n)
    # Índice objetivo artificial, creado solo para probar un pipeline de regresión.
    resultado = prob_exito * ingresos - costo - 8 * tiempo + ruido
    return pd.DataFrame({
        "costo_mision_hipotetico": costo,
        "ingresos_potenciales_hipoteticos": ingresos,
        "probabilidad_exito_hipotetica": prob_exito,
        "tiempo_recuperacion_hipotetico": tiempo,
        "indice_resultado_sintetico": resultado,
    })

def entrenar_modelo(df=None, random_state=42):
    df = df.copy() if df is not None else generar_datos_sinteticos(random_state=random_state)
    X = df.drop(columns=["indice_resultado_sintetico"])
    y = df["indice_resultado_sintetico"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=random_state
    )
    modelo = LinearRegression()
    modelo.fit(X_train, y_train)
    pred = modelo.predict(X_test)
    metricas = {
        "MAE": float(mean_absolute_error(y_test, pred)),
        "R2": float(r2_score(y_test, pred)),
        "n_entrenamiento": int(len(X_train)),
        "n_prueba": int(len(X_test)),
    }
    predicciones = pd.DataFrame({"real_sintetico": y_test.to_numpy(), "prediccion": pred})
    return modelo, metricas, predicciones, X.columns.tolist()
