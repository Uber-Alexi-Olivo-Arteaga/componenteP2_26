"""
Suite de Pruebas Unitarias Automatizadas para Pilas y Colas en Python
Carrera: Ingeniería de Software - UNEMI
Asignatura: Estructura de Datos
"""

import unittest
from pila import Pila, EditorTextoDeshacer
from cola import Cola, SistemaTurnosBanco
from excepciones import PilaVaciaError, ColaVaciaError


class TestPila(unittest.TestCase):
    """Pruebas unitarias para la estructura de datos Pila (LIFO)."""

    def setUp(self):
        self.pila = Pila()

    def test_inicializacion_vacia(self):
        """Verifica que la pila comience vacía."""
        self.assertTrue(self.pila.esta_vacia())
        self.assertEqual(self.pila.tamanio(), 0)
        self.assertEqual(len(self.pila), 0)

    def test_apilar_y_tamanio(self):
        """Verifica la inserción correcta de elementos (push)."""
        self.pila.apilar("Elemento A")
        self.assertFalse(self.pila.esta_vacia())
        self.assertEqual(self.pila.tamanio(), 1)
        self.assertEqual(self.pila.cima(), "Elemento A")

        self.pila.apilar("Elemento B")
        self.assertEqual(self.pila.tamanio(), 2)
        self.assertEqual(self.pila.cima(), "Elemento B")

    def test_desapilar_orden_lifo(self):
        """Verifica que los elementos salgan en orden inverso al de entrada (LIFO)."""
        self.pila.apilar(10)
        self.pila.apilar(20)
        self.pila.apilar(30)

        self.assertEqual(self.pila.desapilar(), 30)
        self.assertEqual(self.pila.desapilar(), 20)
        self.assertEqual(self.pila.desapilar(), 10)
        self.assertTrue(self.pila.esta_vacia())

    def test_cima_no_remueve(self):
        """Verifica que consultar la cima no modifique el tamaño de la pila."""
        self.pila.apilar(999)
        self.assertEqual(self.pila.cima(), 999)
        self.assertEqual(self.pila.tamanio(), 1)

    def test_desapilar_vacia_lanza_excepcion(self):
        """Verifica que desapilar de una pila vacía dispare PilaVaciaError."""
        with self.assertRaises(PilaVaciaError):
            self.pila.desapilar()

    def test_cima_vacia_lanza_excepcion(self):
        """Verifica que consultar la cima de una pila vacía dispare PilaVaciaError."""
        with self.assertRaises(PilaVaciaError):
            self.pila.cima()

    def test_limpiar(self):
        """Verifica el vaciado completo de la pila."""
        self.pila.apilar("X")
        self.pila.apilar("Y")
        self.pila.limpiar()
        self.assertTrue(self.pila.esta_vacia())
        self.assertEqual(self.pila.tamanio(), 0)

    def test_capacidad_maxima(self):
        """Verifica el comportamiento con capacidad acotada y OverflowError."""
        pila_acotada = Pila(capacidad_maxima=2)
        pila_acotada.apilar("Uno")
        pila_acotada.apilar("Dos")
        with self.assertRaises(OverflowError):
            pila_acotada.apilar("Tres")

    def test_caso_real_editor_deshacer(self):
        """Prueba del simulador de deshacer/rehacer con pilas."""
        editor = EditorTextoDeshacer()
        editor.escribir("Hola ")
        editor.escribir("Mundo")
        self.assertEqual(editor.obtener_texto(), "Hola Mundo")

        # Deshacer "Mundo"
        self.assertTrue(editor.deshacer())
        self.assertEqual(editor.obtener_texto(), "Hola ")

        # Rehacer "Mundo"
        self.assertTrue(editor.rehacer())
        self.assertEqual(editor.obtener_texto(), "Hola Mundo")


class TestCola(unittest.TestCase):
    """Pruebas unitarias para la estructura de datos Cola (FIFO)."""

    def setUp(self):
        self.cola = Cola()

    def test_inicializacion_vacia(self):
        """Verifica que la cola comience vacía."""
        self.assertTrue(self.cola.esta_vacia())
        self.assertEqual(self.cola.tamanio(), 0)

    def test_encolar_y_tamanio(self):
        """Verifica la inserción correcta de elementos (enqueue)."""
        self.cola.encolar("Ticket 1")
        self.assertFalse(self.cola.esta_vacia())
        self.assertEqual(self.cola.tamanio(), 1)
        self.assertEqual(self.cola.frente(), "Ticket 1")
        self.assertEqual(self.cola.final(), "Ticket 1")

        self.cola.encolar("Ticket 2")
        self.assertEqual(self.cola.tamanio(), 2)
        self.assertEqual(self.cola.frente(), "Ticket 1")
        self.assertEqual(self.cola.final(), "Ticket 2")

    def test_desencolar_orden_fifo(self):
        """Verifica que los elementos salgan en el mismo orden de llegada (FIFO)."""
        self.cola.encolar("Primero")
        self.cola.encolar("Segundo")
        self.cola.encolar("Tercero")

        self.assertEqual(self.cola.desencolar(), "Primero")
        self.assertEqual(self.cola.desencolar(), "Segundo")
        self.assertEqual(self.cola.desencolar(), "Tercero")
        self.assertTrue(self.cola.esta_vacia())

    def test_frente_y_final_no_remueven(self):
        """Verifica que peek no altere los elementos ni el tamaño."""
        self.cola.encolar(100)
        self.cola.encolar(200)
        self.assertEqual(self.cola.frente(), 100)
        self.assertEqual(self.cola.final(), 200)
        self.assertEqual(self.cola.tamanio(), 2)

    def test_desencolar_vacia_lanza_excepcion(self):
        """Verifica que desencolar en cola vacía dispare ColaVaciaError."""
        with self.assertRaises(ColaVaciaError):
            self.cola.desencolar()

    def test_frente_vacia_lanza_excepcion(self):
        """Verifica que consultar el frente en cola vacía dispare ColaVaciaError."""
        with self.assertRaises(ColaVaciaError):
            self.cola.frente()

    def test_limpiar(self):
        """Verifica el vaciado de la cola."""
        self.cola.encolar(1)
        self.cola.encolar(2)
        self.cola.limpiar()
        self.assertTrue(self.cola.esta_vacia())

    def test_capacidad_maxima(self):
        """Verifica el comportamiento con capacidad acotada y OverflowError."""
        cola_acotada = Cola(capacidad_maxima=2)
        cola_acotada.encolar("A")
        cola_acotada.encolar("B")
        with self.assertRaises(OverflowError):
            cola_acotada.encolar("C")

    def test_caso_real_turnos_banco(self):
        """Prueba del simulador de turnos de banco con colas."""
        banco = SistemaTurnosBanco()
        c1 = banco.emitir_turno("Carlos Vera", "Depósito")
        c2 = banco.emitir_turno("Ana Soto", "Apertura de Cuenta")

        self.assertEqual(banco.cantidad_en_espera(), 2)
        self.assertEqual(banco.ver_proximo().nombre, "Carlos Vera")

        atendido1 = banco.atender_siguiente()
        self.assertEqual(atendido1.nombre, "Carlos Vera")
        self.assertEqual(banco.cantidad_en_espera(), 1)

        atendido2 = banco.atender_siguiente()
        self.assertEqual(atendido2.nombre, "Ana Soto")
        self.assertEqual(banco.cantidad_en_espera(), 0)
        self.assertIsNone(banco.atender_siguiente())


if __name__ == "__main__":
    unittest.main()

