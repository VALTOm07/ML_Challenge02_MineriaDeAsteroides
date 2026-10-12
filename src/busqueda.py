"""Búsqueda en anchura sobre el grafo conceptual de evaluación."""
from collections import deque

GRAFO_ESTADOS = {
    "S0": ["S1"],
    "S1": ["S2"],
    "S2": ["S3"],
    "S3": ["S4", "S5"],
    "S4": [],
    "S5": [],
}
NOMBRES_ESTADOS = {
    "S0": "Inicio",
    "S1": "Tecnología revisada",
    "S2": "Economía calculada",
    "S3": "Restricciones revisadas",
    "S4": "Evaluación preliminar favorable",
    "S5": "Requiere más evidencia",
}

def busqueda_anchura(inicio="S0", objetivo="S4", grafo=None):
    """Devuelve orden visitado y camino más corto en número de transiciones."""
    grafo = grafo or GRAFO_ESTADOS
    cola = deque([inicio])
    padres = {inicio: None}
    visitados = []
    while cola:
        actual = cola.popleft()
        visitados.append(actual)
        if actual == objetivo:
            break
        for vecino in grafo.get(actual, []):
            if vecino not in padres:
                padres[vecino] = actual
                cola.append(vecino)
    camino = []
    if objetivo in padres:
        actual = objetivo
        while actual is not None:
            camino.append(actual)
            actual = padres[actual]
        camino.reverse()
    return {
        "inicio": inicio,
        "objetivo": objetivo,
        "visitados": visitados,
        "camino": camino,
        "encontrado": objetivo in padres,
        "nombres_visitados": [NOMBRES_ESTADOS.get(s, s) for s in visitados],
    }
