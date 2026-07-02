"""
Módulo de asistencia.
Registra la asistencia diaria de los socios y la guarda en CSV.
"""

import csv
import os
from datetime import date

from socios import buscar_socio_por_dni

ARCHIVO_ASISTENCIAS = "datos/asistencias.csv"
CAMPOS_ASISTENCIAS = ["dni_socio", "fecha"]


def cargar_asistencias():
    asistencias = []
    if not os.path.exists(ARCHIVO_ASISTENCIAS):
        return asistencias
    try:
        with open(ARCHIVO_ASISTENCIAS, "r", newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                asistencias.append(fila)
    except Exception as error:
        print(f"Error al leer asistencias: {error}")
    return asistencias


def guardar_asistencias(asistencias):
    try:
        with open(ARCHIVO_ASISTENCIAS, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=CAMPOS_ASISTENCIAS)
            escritor.writeheader()
            escritor.writerows(asistencias)
    except Exception as error:
        print(f"Error al guardar asistencias: {error}")


def registrar_asistencia(socios, asistencias):
    """Registra la asistencia del día para un socio, si tiene el pago al día."""
    dni = input("Ingrese el DNI del socio: ").strip()
    socio = buscar_socio_por_dni(socios, dni)
    if socio is None:
        print("No se encontró ningún socio con ese DNI.")
        return
    if socio["pago_al_dia"] == "No":
        print("El socio tiene el pago pendiente. No puede registrar asistencia.")
        return

    hoy = date.today().isoformat()
    asistencias.append({"dni_socio": dni, "fecha": hoy})
    guardar_asistencias(asistencias)
    print(f"Asistencia registrada para {socio['nombre']} ({hoy}).")
