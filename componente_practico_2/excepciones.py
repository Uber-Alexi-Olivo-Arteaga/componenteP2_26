"""
Módulo de Excepciones Personalizadas para Estructuras de Datos Lineales
Carrera: Ingeniería de Software - UNEMI
Asignatura: Estructura de Datos
"""


class EstructuraError(Exception):
    """Clase base para errores relacionados con estructuras de datos."""
    pass


class PilaVaciaError(EstructuraError):
    """Excepción lanzada cuando se intenta desapilar o consultar una pila vacía (Underflow)."""

    def __init__(self, mensaje: str = "Error de desbordamiento por defecto (Underflow): La pila está vacía."):
        super().__init__(mensaje)


class ColaVaciaError(EstructuraError):
    """Excepción lanzada cuando se intenta desencolar o consultar una cola vacía (Underflow)."""

    def __init__(self, mensaje: str = "Error de desbordamiento por defecto (Underflow): La cola está vacía."):
        super().__init__(mensaje)

