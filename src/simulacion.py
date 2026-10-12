"""Funciones de simulación económica didáctica. No son estimaciones reales."""
from dataclasses import dataclass, asdict

@dataclass
class Escenario:
    costo_mision: float = 500.0
    ingresos_potenciales: float = 800.0
    probabilidad_exito: float = 0.55
    tiempo_recuperacion: float = 8.0

    def validar(self):
        if self.costo_mision < 0 or self.ingresos_potenciales < 0:
            raise ValueError("Costo e ingresos deben ser no negativos.")
        if not 0 <= self.probabilidad_exito <= 1:
            raise ValueError("La probabilidad debe estar entre 0 y 1.")
        if self.tiempo_recuperacion < 0:
            raise ValueError("El tiempo debe ser no negativo.")

    def resultados(self):
        self.validar()
        beneficio_si_exito = self.ingresos_potenciales - self.costo_mision
        beneficio_esperado = self.probabilidad_exito * self.ingresos_potenciales - self.costo_mision
        roi = (beneficio_esperado / self.costo_mision * 100) if self.costo_mision > 0 else None
        return {
            "beneficio_si_exito": beneficio_si_exito,
            "beneficio_esperado": beneficio_esperado,
            "roi_simplificado_pct": roi,
            "tiempo_recuperacion": self.tiempo_recuperacion,
            "supuestos": asdict(self),
        }

def clasificar_escenario(escenario: Escenario, umbral_probabilidad=0.5, tiempo_maximo=10.0):
    """Clasificación académica basada en umbrales elegidos para la simulación."""
    r = escenario.resultados()
    cumple = (
        escenario.probabilidad_exito >= umbral_probabilidad
        and escenario.tiempo_recuperacion <= tiempo_maximo
        and r["beneficio_esperado"] > 0
    )
    return {
        "estado": "Evaluación preliminar favorable" if cumple else "Requiere más evidencia",
        "cumple_probabilidad": escenario.probabilidad_exito >= umbral_probabilidad,
        "cumple_tiempo": escenario.tiempo_recuperacion <= tiempo_maximo,
        "beneficio_esperado_positivo": r["beneficio_esperado"] > 0,
        "nota": "Clasificación hipotética; no demuestra viabilidad de una misión real."
    }
