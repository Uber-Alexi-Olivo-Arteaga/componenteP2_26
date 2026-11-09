"""
Sistema Principal: Operaciones Básicas de Pilas y Colas en Python
Carrera: Ingeniería de Software - UNEMI
Asignatura: Estructura de Datos
Autor: Uber Alexi Olivo Arteaga
"""

import sys
from pila import Pila, EditorTextoDeshacer
from cola import Cola, SistemaTurnosBanco
from excepciones import PilaVaciaError, ColaVaciaError


def limpiar_pantalla():
    """Imprime un separador limpio en la consola."""
    print("\n" + "=" * 65 + "\n")


def leer_entero(mensaje: str, min_val: int = None, max_val: int = None) -> int:
    """Solicita un número entero por teclado de forma segura evitando excepciones."""
    while True:
        try:
            valor = int(input(mensaje).strip())
            if min_val is not None and valor < min_val:
                print(f"  ⚠ El número debe ser mayor o igual a {min_val}.")
                continue
            if max_val is not None and valor > max_val:
                print(f"  ⚠ El número debe ser menor o igual a {max_val}.")
                continue
            return valor
        except ValueError:
            print("  ⚠ Entrada inválida: Ingrese un número entero válido.")


def leer_texto(mensaje: str) -> str:
    """Solicita un texto no vacío."""
    while True:
        cadena = input(mensaje).strip()
        if cadena:
            return cadena
        print("  ⚠ Este campo no puede estar vacío.")


# =====================================================================
# SUBMENÚ 1: OPERACIONES DE PILA (LIFO)
# =====================================================================

def menu_pila(pila: Pila):
    while True:
        print("\n" + "─" * 45)
        print("    🥞 OPERACIONES BÁSICAS: PILA (LIFO)")
        print("─" * 45)
        print("  [1] Apilar elemento (Push)         -> lista.append()")
        print("  [2] Desapilar elemento (Pop)       -> lista.pop()")
        print("  [3] Consultar cima/tope (Peek)     -> lista[-1]")
        print("  [4] Verificar si está vacía        -> len(lista) == 0")
        print("  [5] Ver tamaño actual              -> len(lista)")
        print("  [6] Mostrar pila gráficamente      -> [Tope a Base]")
        print("  [7] Vaciar pila (Clear)            -> lista.clear()")
        print("  [0] Volver al Menú Principal")
        print("─" * 45)

        opc = leer_entero("  Seleccione una opción: ", 0, 7)

        if opc == 1:
            elem = leer_texto("  Ingrese el valor o texto a apilar: ")
            pila.apilar(elem)
            print(f"  ✓ Elemento '{elem}' apilado en la cima con éxito.")
        elif opc == 2:
            try:
                elem = pila.desapilar()
                print(f"  ✓ Elemento desapilado del tope: '{elem}'")
            except PilaVaciaError as e:
                print(f"  ⚠ {e}")
        elif opc == 3:
            try:
                elem = pila.cima()
                print(f"  🔍 Cima actual de la pila: '{elem}'")
            except PilaVaciaError as e:
                print(f"  ⚠ {e}")
        elif opc == 4:
            if pila.esta_vacia():
                print("  ℹ La pila SÍ está vacía (0 elementos).")
            else:
                print(f"  ℹ La pila NO está vacía (contiene {pila.tamanio()} elementos).")
        elif opc == 5:
            print(f"  ℹ Tamaño de la pila: {pila.tamanio()} elementos.")
        elif opc == 6:
            print(pila.representacion_grafica())
        elif opc == 7:
            pila.limpiar()
            print("  ✓ Pila vaciada correctamente.")
        elif opc == 0:
            break


# =====================================================================
# SUBMENÚ 2: OPERACIONES DE COLA (FIFO)
# =====================================================================

def menu_cola(cola: Cola):
    while True:
        print("\n" + "─" * 45)
        print("    🚶 OPERACIONES BÁSICAS: COLA (FIFO)")
        print("─" * 45)
        print("  [1] Encolar elemento (Enqueue)     -> lista.append()")
        print("  [2] Desencolar elemento (Dequeue)  -> lista.pop(0)")
        print("  [3] Consultar frente (Peek)        -> lista[0]")
        print("  [4] Consultar final (Último)       -> lista[-1]")
        print("  [5] Verificar si está vacía        -> len(lista) == 0")
        print("  [6] Ver tamaño actual              -> len(lista)")
        print("  [7] Mostrar cola gráficamente      -> [Frente -> Final]")
        print("  [8] Vaciar cola (Clear)            -> lista.clear()")
        print("  [0] Volver al Menú Principal")
        print("─" * 45)

        opc = leer_entero("  Seleccione una opción: ", 0, 8)

        if opc == 1:
            elem = leer_texto("  Ingrese el valor o texto a encolar: ")
            cola.encolar(elem)
            print(f"  ✓ Elemento '{elem}' agregado al final de la cola.")
        elif opc == 2:
            try:
                elem = cola.desencolar()
                print(f"  ✓ Elemento desencolado del frente: '{elem}'")
            except ColaVaciaError as e:
                print(f"  ⚠ {e}")
        elif opc == 3:
            try:
                elem = cola.frente()
                print(f"  🔍 Frente actual de la cola: '{elem}'")
            except ColaVaciaError as e:
                print(f"  ⚠ {e}")
        elif opc == 4:
            try:
                elem = cola.final()
                print(f"  🔍 Final actual de la cola: '{elem}'")
            except ColaVaciaError as e:
                print(f"  ⚠ {e}")
        elif opc == 5:
            if cola.esta_vacia():
                print("  ℹ La cola SÍ está vacía (0 elementos).")
            else:
                print(f"  ℹ La cola NO está vacía (contiene {cola.tamanio()} elementos).")
        elif opc == 6:
            print(f"  ℹ Tamaño de la cola: {cola.tamanio()} elementos.")
        elif opc == 7:
            print(cola.representacion_grafica())
        elif opc == 8:
            cola.limpiar()
            print("  ✓ Cola vaciada correctamente.")
        elif opc == 0:
            break


# =====================================================================
# SUBMENÚ 3: CASOS DE USO DEL MUNDO REAL
# =====================================================================

def demo_editor_deshacer():
    editor = EditorTextoDeshacer()
    while True:
        print("\n" + "─" * 50)
        print("  📝 SIMULADOR DE TEXTO: DESHACER / REHACER (PILA)")
        print("─" * 50)
        print(f"  Contenido actual del documento:\n  \"{editor.obtener_texto()}\"")
        print("─" * 50)
        print("  [1] Escribir texto")
        print("  [2] Deshacer (Undo - Pila LIFO)")
        print("  [3] Rehacer (Redo - Pila LIFO)")
        print("  [0] Regresar")
        opc = leer_entero("  Seleccione: ", 0, 3)

        if opc == 1:
            texto = input("  Texto a añadir: ")
            editor.escribir(texto)
        elif opc == 2:
            if editor.deshacer():
                print("  ✓ Acción deshecha con éxito.")
            else:
                print("  ⚠ No hay más acciones para deshacer.")
        elif opc == 3:
            if editor.rehacer():
                print("  ✓ Acción rehecha con éxito.")
            else:
                print("  ⚠ No hay más acciones para rehacer.")
        elif opc == 0:
            break


def demo_turnos_banco():
    banco = SistemaTurnosBanco()
    while True:
        print("\n" + "─" * 50)
        print("  🏦 SISTEMA DE GESTIÓN DE TURNOS BANCARIOS (COLA)")
        print("─" * 50)
        print(f"  Clientes en fila de espera: {banco.cantidad_en_espera()}")
        prox = banco.ver_proximo()
        if prox:
            print(f"  Siguiente en turno: {prox}")
        print("─" * 50)
        print("  [1] Solicitar nuevo turno (Encolar)")
        print("  [2] Atender siguiente cliente (Desencolar)")
        print("  [3] Ver cola gráfica de espera")
        print("  [4] Ver clientes ya atendidos")
        print("  [0] Regresar")
        opc = leer_entero("  Seleccione: ", 0, 4)

        if opc == 1:
            nombre = leer_texto("  Nombre del cliente: ")
            motivo = leer_texto("  Motivo de visita (Depósito / Retiro / Asesoría): ")
            turno = banco.emitir_turno(nombre, motivo)
            print(f"  ✓ Turno generado con éxito: {turno}")
        elif opc == 2:
            atendido = banco.atender_siguiente()
            if atendido:
                print(f"  ✓ Ahora se atiende a: {atendido}")
            else:
                print("  ⚠ No hay clientes en espera.")
        elif opc == 3:
            print(banco.cola_clientes.representacion_grafica())
        elif opc == 4:
            if not banco.atendidos_historial:
                print("  ℹ Aún no se ha atendido a ningún cliente.")
            else:
                print("  === CLIENTES ATENDIDOS ===")
                for i, c in enumerate(banco.atendidos_historial, 1):
                    print(f"  {i}. {c}")
        elif opc == 0:
            break


def menu_casos_reales():
    while True:
        print("\n" + "─" * 45)
        print("    💼 CASOS DE APLICACIÓN EN EL MUNDO REAL")
        print("─" * 45)
        print("  [1] Editor con Deshacer / Rehacer (Uso de Pilas LIFO)")
        print("  [2] Sistema de Turnos de Atención (Uso de Colas FIFO)")
        print("  [0] Volver al Menú Principal")
        print("─" * 45)
        opc = leer_entero("  Seleccione una opción: ", 0, 2)
        if opc == 1:
            demo_editor_deshacer()
        elif opc == 2:
            demo_turnos_banco()
        elif opc == 0:
            break


# =====================================================================
# SUBMENÚ 4: DEMOSTRACIÓN AUTOMATIZADA COMPLETA
# =====================================================================

def ejecutar_demostracion_completa():
    """Ejecuta una demostración automática y pedagógica de todas las operaciones."""
    limpiar_pantalla()
    print("🚀 EJECUTANDO DEMOSTRACIÓN COMPLETA DE PILAS Y COLAS")
    print("=" * 65)

    print("\n>>> PARTE 1: DEMOSTRACIÓN DE PILA (STACK - LIFO) <<<")
    p = Pila()
    print(f"1. Se inicializa Pila vacía: esta_vacia() = {p.esta_vacia()}, tamaño = {p.tamanio()}")
    
    print("\n2. Apilando elementos con lista.append()...")
    for item in ["Documento_A.pdf", "Documento_B.docx", "Imagen_C.png"]:
        p.apilar(item)
        print(f"   + Apilado: {item} | Cima actual: {p.cima()} | Tamaño: {p.tamanio()}")

    print("\n3. Visualización vertical de la Pila:")
    print(p.representacion_grafica())

    print("4. Desapilando elementos con lista.pop()...")
    while not p.esta_vacia():
        extraido = p.desapilar()
        print(f"   - Desapilado: {extraido} (LIFO: el último en entrar sale primero)")
    
    print(f"\n5. Estado final tras vaciado: esta_vacia() = {p.esta_vacia()}, tamaño = {p.tamanio()}")
    try:
        p.desapilar()
    except PilaVaciaError as e:
        print(f"   [Control de Excepción] Al intentar desapilar vacía: {e}")

    print("\n" + "-" * 65)
    print(">>> PARTE 2: DEMOSTRACIÓN DE COLA (QUEUE - FIFO) <<<")
    c = Cola()
    print(f"1. Se inicializa Cola vacía: esta_vacia() = {c.esta_vacia()}, tamaño = {c.tamanio()}")

    print("\n2. Encolando elementos con lista.append()...")
    for paciente in ["Paciente 1 (Mario)", "Paciente 2 (Lucía)", "Paciente 3 (Roberto)"]:
        c.encolar(paciente)
        print(f"   + Encolado al final: {paciente} | Frente actual: {c.frente()} | Tamaño: {c.tamanio()}")

    print("\n3. Visualización horizontal de la Cola:")
    print(c.representacion_grafica())

    print("4. Desencolando elementos con lista.pop(0)...")
    while not c.esta_vacia():
        atendido = c.desencolar()
        print(f"   - Desencolado del frente: {atendido} (FIFO: el primero en llegar es atendido)")

    print(f"\n5. Estado final tras vaciado: esta_vacia() = {c.esta_vacia()}, tamaño = {c.tamanio()}")
    try:
        c.desencolar()
    except ColaVaciaError as e:
        print(f"   [Control de Excepción] Al intentar desencolar vacía: {e}")

    print("\n" + "=" * 65)
    print("✓ Demostración finalizada exitosamente.")
    input("\nPresione Enter para regresar al menú principal...")


# =====================================================================
# MENÚ PRINCIPAL
# =====================================================================

def main():
    pila_global = Pila()
    cola_global = Cola()

    # Cargar algunos datos iniciales didácticos
    for x in ["Navegador: Google.com", "Navegador: Unemi.edu.ec", "Navegador: GitHub.com"]:
        pila_global.apilar(x)

    for x in ["Turno-01: Pago Matrícula", "Turno-02: Certificado", "Turno-03: Consulta General"]:
        cola_global.encolar(x)

    while True:
        print("\n" + "╔" + "═" * 63 + "╗")
        print("║   UNIVERSIDAD ESTATAL DE MILAGRO - INGENIERÍA DE SOFTWARE    ║")
        print("║   Estructura de Datos · Operaciones de Pilas y Colas          ║")
        print("╚" + "═" * 63 + "╝")
        print("  [1] Operaciones Básicas de Pila (Stack - LIFO)")
        print("  [2] Operaciones Básicas de Cola (Queue - FIFO)")
        print("  [3] Casos de Aplicación en el Mundo Real")
        print("  [4] Demostración Guiada y Completa (para Capturas de Informe)")
        print("  [0] Salir")
        print("─" * 65)

        opcion = leer_entero("  Ingrese su opción: ", 0, 4)

        if opcion == 1:
            menu_pila(pila_global)
        elif opcion == 2:
            menu_cola(cola_global)
        elif opcion == 3:
            menu_casos_reales()
        elif opcion == 4:
            ejecutar_demostracion_completa()
        elif opcion == 0:
            print("\n  ¡Gracias por utilizar el sistema de Pilas y Colas UNEMI! Hasta pronto.\n")
            sys.exit(0)


if __name__ == "__main__":
    main()

