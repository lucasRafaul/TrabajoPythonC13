"""
Módulo de actividades.
Maneja la inscripción de socios a actividades del gimnasio
(Musculación, Spinning, Yoga, etc.) y su persistencia en CSV.
"""

import csv
import os

from socios import buscar_socio_por_dni

ARCHIVO_INSCRIPCIONES = "datos/inscripciones.csv"
CAMPOS_INSCRIPCIONES = ["dni_socio", "actividad"]

ACTIVIDADES_DISPONIBLES = ["Musculación", "Spinning", "Yoga", "Crossfit", "Funcional"]


def cargar_inscripciones():
    inscripciones = []
    if not os.path.exists(ARCHIVO_INSCRIPCIONES):
        return inscripciones
    try:
        with open(ARCHIVO_INSCRIPCIONES, "r", newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                inscripciones.append(fila)
    except Exception as error:
        print(f"Error al leer inscripciones: {error}")
    return inscripciones


def guardar_inscripciones(inscripciones):
    try:
        with open(ARCHIVO_INSCRIPCIONES, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=CAMPOS_INSCRIPCIONES)
            escritor.writeheader()
            escritor.writerows(inscripciones)
    except Exception as error:
        print(f"Error al guardar inscripciones: {error}")


def mostrar_actividades():
    print("\n--- Actividades disponibles ---")
    for indice, actividad in enumerate(ACTIVIDADES_DISPONIBLES, start=1):
        print(f"{indice}) {actividad}")


def inscribir_actividad(socios, inscripciones):
    """Inscribe a un socio existente en una actividad, evitando duplicados."""
    dni = input("Ingrese el DNI del socio: ").strip()
    socio = buscar_socio_por_dni(socios, dni)
    if socio is None:
        print("No se encontró ningún socio con ese DNI.")
        return

    mostrar_actividades()
    opcion = input("Seleccione una actividad: ").strip()
    while not opcion.isdigit() or int(opcion) not in range(1, len(ACTIVIDADES_DISPONIBLES) + 1):
        print("Opción inválida.")
        opcion = input("Seleccione una actividad: ").strip()

    actividad = ACTIVIDADES_DISPONIBLES[int(opcion) - 1]

    for inscripcion in inscripciones:
        if inscripcion["dni_socio"] == dni and inscripcion["actividad"] == actividad:
            print("El socio ya está inscripto en esa actividad.")
            return

    inscripciones.append({"dni_socio": dni, "actividad": actividad})
    guardar_inscripciones(inscripciones)
    print(f"Socio inscripto en '{actividad}' correctamente.")
