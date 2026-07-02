"""
Sistema de Gestión de Gimnasio - Trabajo Final Integrador
Punto de entrada del programa: muestra el menú y llama a las funciones
de cada módulo según la opción elegida.
"""

import os

from socios import cargar_socios, registrar_socio, listar_socios
from membresias import TIPOS_MEMBRESIA, asignar_membresia, registrar_pago, listar_deudores
from actividades import cargar_inscripciones, inscribir_actividad
from asistencia import cargar_asistencias, registrar_asistencia
from estadisticas import mostrar_estadisticas


def mostrar_menu():
    print("\n===== GESTIÓN DE GIMNASIO =====")
    print("1) Registrar socio")
    print("2) Listar socios")
    print("3) Asignar membresía")
    print("4) Registrar pago de cuota")
    print("5) Listar socios con pago pendiente")
    print("6) Inscribir socio a una actividad")
    print("7) Registrar asistencia")
    print("8) Ver estadísticas")
    print("0) Salir")


def main():
    os.makedirs("datos", exist_ok=True)

    socios = cargar_socios()
    inscripciones = cargar_inscripciones()
    asistencias = cargar_asistencias()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        try:
            if opcion == "1":
                registrar_socio(socios)
            elif opcion == "2":
                listar_socios(socios)
            elif opcion == "3":
                asignar_membresia(socios)
            elif opcion == "4":
                registrar_pago(socios)
            elif opcion == "5":
                listar_deudores(socios)
            elif opcion == "6":
                inscribir_actividad(socios, inscripciones)
            elif opcion == "7":
                registrar_asistencia(socios, asistencias)
            elif opcion == "8":
                mostrar_estadisticas(socios, inscripciones, asistencias, TIPOS_MEMBRESIA)
            elif opcion == "0":
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida. Intente nuevamente.")
        except Exception as error:
            print(f"Ocurrió un error inesperado: {error}")


if __name__ == "__main__":
    main()
