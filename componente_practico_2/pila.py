"""
Implementación de la Estructura de Datos Pila (Stack - LIFO)
basada en listas dinámicas nativas de Python.
Carrera: Ingeniería de Software - UNEMI
Asignatura: Estructura de Datos
"""

from typing import Any, List, Optional
from excepciones import PilaVaciaError


class Pila:
    """
    Clase que representa una Pila (Stack) siguiendo la filosofía LIFO
    (Last In, First Out / Último en entrar, primero en salir).
    
    Se implementa internamente utilizando una lista nativa de Python (`list`),
    aprovechando los métodos de tiempo constante O(1):
      - Inserción: `append(elemento)` al final de la lista (tope de la pila).
      - Extracción: `pop()` desde el final de la lista (tope de la pila).
    """

    def __init__(self, capacidad_maxima: Optional[int] = None) -> None:
        """
        Inicializa una nueva Pila vacía.
        :param capacidad_maxima: Límite opcional de capacidad (para pilas acotadas).
        """
        self._items: List[Any] = []
        self._capacidad_maxima: Optional[int] = capacidad_maxima

    def apilar(self, elemento: Any) -> bool:
        """
        Inserta un elemento en la cima (tope) de la pila (operación PUSH).
        Complejidad temporal: O(1) amortizado.
        
        :param elemento: Objeto o valor a insertar en la pila.
        :return: True si se insertó con éxito.
        :raises OverflowError: Si se definió capacidad máxima y la pila está llena.
        """
        if self._capacidad_maxima is not None and len(self._items) >= self._capacidad_maxima:
            raise OverflowError(f"Error de desbordamiento (Overflow): Capacidad máxima alcanzada ({self._capacidad_maxima}).")
        
        self._items.append(elemento)
        return True

    def desapilar(self) -> Any:
        """
        Remueve y retorna el elemento que se encuentra en la cima de la pila (operación POP).
        Complejidad temporal: O(1).
        
        :return: El elemento extraído del tope.
        :raises PilaVaciaError: Si la pila no contiene elementos (Underflow).
        """
        if self.esta_vacia():
            raise PilaVaciaError("No se puede desapilar: La pila está vacía (Underflow).")
        
        return self._items.pop()

    def cima(self) -> Any:
        """
        Retorna el elemento ubicado en la cima sin removerlo (operación PEEK / TOPE).
        Complejidad temporal: O(1).
        
        :return: El elemento en el tope.
        :raises PilaVaciaError: Si la pila está vacía.
        """
        if self.esta_vacia():
            raise PilaVaciaError("No se puede consultar la cima: La pila está vacía.")
        
        return self._items[-1]

    def esta_vacia(self) -> bool:
        """
        Determina si la pila carece de elementos.
        Complejidad temporal: O(1).
        
        :return: True si está vacía, False en caso contrario.
        """
        return len(self._items) == 0

    def tamanio(self) -> int:
        """
        Retorna la cantidad actual de elementos en la pila.
        Complejidad temporal: O(1).
        """
        return len(self._items)

    def limpiar(self) -> None:
        """
        Elimina todos los elementos de la pila, restableciéndola a estado vacío.
        """
        self._items.clear()

    def a_lista(self) -> List[Any]:
        """
        Retorna una copia superficial de la lista interna.
        """
        return list(self._items)

    def representacion_grafica(self) -> str:
        """
        Genera una vista visual esquemática de la pila verticalmente en consola.
        """
        if self.esta_vacia():
            return "   |        |\n   +--------+  (Pila Vacía)\n"

        lineas = ["\n   === ESTADO DE LA PILA (LIFO) ==="]
        for i in range(len(self._items) - 1, -1, -1):
            elem_str = str(self._items[i])
            if len(elem_str) > 16:
                elem_str = elem_str[:13] + "..."
            etiqueta = " <- TOPE (Cima)" if i == len(self._items) - 1 else ""
            lineas.append(f"   | {elem_str:^16} |{etiqueta}")
        lineas.append("   +----------------+")
        lineas.append(f"   Total elementos: {self.tamanio()}\n")
        return "\n".join(lineas)

    def __len__(self) -> int:
        return self.tamanio()

    def __str__(self) -> str:
        return f"Pila(elementos={self._items}, tope={self._items[-1] if self._items else None})"

    def __repr__(self) -> str:
        return f"Pila({self._items!r})"


# =====================================================================
# CASO DE APLICACIÓN PRÁCTICA EN EL MUNDO REAL:
# Simulador de Deshacer / Rehacer (Undo / Redo) en un Editor de Texto
# =====================================================================

class EditorTextoDeshacer:
    """
    Demostración práctica del principio LIFO utilizando dos Pilas:
      1. `pila_deshacer`: Registra el historial de acciones realizadas.
      2. `pila_rehacer`: Permite volver a aplicar acciones deshechas.
    """

    def __init__(self) -> None:
        self.contenido: str = ""
        self.pila_deshacer = Pila()
        self.pila_rehacer = Pila()

    def escribir(self, nuevo_texto: str) -> None:
        """Añade texto al documento y guarda el estado previo en la pila."""
        self.pila_deshacer.apilar(self.contenido)
        self.pila_rehacer.limpiar()  # Al escribir algo nuevo se limpia el rehacer
        self.contenido += nuevo_texto

    def deshacer(self) -> bool:
        """Deshace la última acción retornando al estado anterior."""
        if self.pila_deshacer.esta_vacia():
            return False
        self.pila_rehacer.apilar(self.contenido)
        self.contenido = self.pila_deshacer.desapilar()
        return True

    def rehacer(self) -> bool:
        """Rehace la acción previamente deshecha."""
        if self.pila_rehacer.esta_vacia():
            return False
        self.pila_deshacer.apilar(self.contenido)
        self.contenido = self.pila_rehacer.desapilar()
        return True

    def obtener_texto(self) -> str:
        return self.contenido

