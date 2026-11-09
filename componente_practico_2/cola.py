"""
Implementación de la Estructura de Datos Cola (Queue - FIFO)
basada en listas dinámicas nativas de Python.
Carrera: Ingeniería de Software - UNEMI
Asignatura: Estructura de Datos
"""

from typing import Any, List, Optional
from excepciones import ColaVaciaError


class Cola:
    """
    Clase que representa una Cola (Queue) siguiendo la filosofía FIFO
    (First In, First Out / Primero en entrar, primero en salir).
    
    Se implementa internamente utilizando una lista nativa de Python (`list`),
    aprovechando:
      - Inserción (Encolar): `append(elemento)` al final de la lista -> O(1) amortizado.
      - Extracción (Desencolar): `pop(0)` al inicio de la lista -> O(n), debido
        al desplazamiento en memoria de los n-1 elementos restantes en un arreglo continuo.
    """

    def __init__(self, capacidad_maxima: Optional[int] = None) -> None:
        """
        Inicializa una nueva Cola vacía.
        :param capacidad_maxima: Límite opcional de capacidad (para colas acotadas).
        """
        self._items: List[Any] = []
        self._capacidad_maxima: Optional[int] = capacidad_maxima

    def encolar(self, elemento: Any) -> bool:
        """
        Inserta un elemento al final de la cola (operación ENQUEUE).
        Complejidad temporal: O(1) amortizado.
        
        :param elemento: Objeto o valor a encolar.
        :return: True si se insertó con éxito.
        :raises OverflowError: Si se fijó una capacidad máxima y la cola está llena.
        """
        if self._capacidad_maxima is not None and len(self._items) >= self._capacidad_maxima:
            raise OverflowError(f"Error de desbordamiento (Overflow): Capacidad máxima alcanzada ({self._capacidad_maxima}).")
        
        self._items.append(elemento)
        return True

    def desencolar(self) -> Any:
        """
        Remueve y retorna el elemento al frente de la cola (operación DEQUEUE).
        Complejidad temporal: O(n) sobre listas nativas de Python debido al desplazamiento.
        
        :return: El elemento que estaba al frente.
        :raises ColaVaciaError: Si la cola se encuentra vacía (Underflow).
        """
        if self.esta_vacia():
            raise ColaVaciaError("No se puede desencolar: La cola está vacía (Underflow).")
        
        return self._items.pop(0)

    def frente(self) -> Any:
        """
        Retorna el elemento que está al frente de la cola sin extraerlo (operación PEEK).
        Complejidad temporal: O(1).
        
        :return: Elemento al frente.
        :raises ColaVaciaError: Si la cola se encuentra vacía.
        """
        if self.esta_vacia():
            raise ColaVaciaError("No se puede consultar el frente: La cola está vacía.")
        
        return self._items[0]

    def final(self) -> Any:
        """
        Retorna el último elemento ingresado a la cola sin extraerlo.
        Complejidad temporal: O(1).
        
        :return: Último elemento en la cola.
        :raises ColaVaciaError: Si la cola se encuentra vacía.
        """
        if self.esta_vacia():
            raise ColaVaciaError("No se puede consultar el final: La cola está vacía.")
        
        return self._items[-1]

    def esta_vacia(self) -> bool:
        """
        Determina si la cola carece de elementos.
        Complejidad temporal: O(1).
        
        :return: True si está vacía, False en caso contrario.
        """
        return len(self._items) == 0

    def tamanio(self) -> int:
        """
        Retorna el número de elementos contenidos en la cola.
        Complejidad temporal: O(1).
        """
        return len(self._items)

    def limpiar(self) -> None:
        """
        Vacía completamente la cola.
        """
        self._items.clear()

    def a_lista(self) -> List[Any]:
        """
        Retorna una copia de los elementos de la cola en orden de llegada.
        """
        return list(self._items)

    def representacion_grafica(self) -> str:
        """
        Genera una vista esquemática horizontal en consola con flechas de flujo FIFO.
        """
        if self.esta_vacia():
            return "   [FRENTE] -> (Cola Vacía) -> [FINAL]\n"

        bloques = [f"[{str(item)}]" for item in self._items]
        cadena_bloques = " -> ".join(bloques)
        
        salida = [
            "\n   === ESTADO DE LA COLA (FIFO) ===",
            f"   (SALIDA) [FRENTE] -> {cadena_bloques} -> [FINAL] (ENTRADA)",
            f"   Total en espera: {self.tamanio()}",
            f"   Próximo a ser atendido: {self._items[0]}",
            f"   Último en llegar:       {self._items[-1]}\n"
        ]
        return "\n".join(salida)

    def __len__(self) -> int:
        return self.tamanio()

    def __str__(self) -> str:
        frente_val = self._items[0] if self._items else None
        return f"Cola(elementos={self._items}, frente={frente_val})"

    def __repr__(self) -> str:
        return f"Cola({self._items!r})"


# =====================================================================
# CASO DE APLICACIÓN PRÁCTICA EN EL MUNDO REAL:
# Sistema de Gestión de Turnos de Atención Bancaria
# =====================================================================

class ClienteTurno:
    """Modela a un cliente que solicita un turno en una agencia de atención."""

    def __init__(self, numero_turno: int, nombre: str, motivo: str) -> None:
        self.codigo_turno = f"T-{numero_turno:03d}"
        self.nombre = nombre
        self.motivo = motivo

    def __str__(self) -> str:
        return f"[{self.codigo_turno}] {self.nombre} ({self.motivo})"


class SistemaTurnosBanco:
    """
    Simulador de atención por turnos bancarios implementado con la estructura Cola (FIFO).
    Los clientes son atendidos estrictamente en el orden en que solicitaron su turno.
    """

    def __init__(self) -> None:
        self.cola_clientes = Cola()
        self.contador_turnos = 0
        self.atendidos_historial: List[ClienteTurno] = []

    def emitir_turno(self, nombre: str, motivo: str) -> ClienteTurno:
        """Emite un nuevo ticket y lo encola al final de la fila de espera."""
        self.contador_turnos += 1
        nuevo_cliente = ClienteTurno(self.contador_turnos, nombre, motivo)
        self.cola_clientes.encolar(nuevo_cliente)
        return nuevo_cliente

    def atender_siguiente(self) -> Optional[ClienteTurno]:
        """Extrae al cliente del frente de la cola y lo procesa."""
        if self.cola_clientes.esta_vacia():
            return None
        cliente = self.cola_clientes.desencolar()
        self.atendidos_historial.append(cliente)
        return cliente

    def ver_proximo(self) -> Optional[ClienteTurno]:
        """Consulta el cliente al frente de la cola sin atenderlo."""
        if self.cola_clientes.esta_vacia():
            return None
        return self.cola_clientes.frente()

    def cantidad_en_espera(self) -> int:
        return self.cola_clientes.tamanio()

