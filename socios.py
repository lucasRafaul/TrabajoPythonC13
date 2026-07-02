"""
Módulo de socios.
Se encarga de registrar socios, listarlos y guardarlos/leerlos de un archivo CSV.
"""

import csv
import os

ARCHIVO_SOCIOS = "datos/socios.csv"
CAMPOS_SOCIOS = ["id", "nombre", "dni", "membresia", "pago_al_dia"]


def cargar_socios():
    """Lee el archivo de socios y devuelve una lista de diccionarios."""
    socios = []
    if not os.path.exists(ARCHIVO_SOCIOS):
        return socios
    try:
        with open(ARCHIVO_SOCIOS, "r", newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                socios.append(fila)
    except Exception as error:
        print(f"Error al leer el archivo de socios: {error}")
    return socios


def guardar_socios(socios):
    """Guarda la lista de socios en el archivo CSV."""
    try:
        with open(ARCHIVO_SOCIOS, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=CAMPOS_SOCIOS)
            escritor.writeheader()
            escritor.writerows(socios)
    except Exception as error:
        print(f"Error al guardar los socios: {error}")


def validar_dni(dni):
    """Un DNI válido: solo números y al menos 7 dígitos."""
    return dni.isdigit() and len(dni) >= 7


def buscar_socio_por_dni(socios, dni):
    """Devuelve el diccionario del socio si existe, o None si no se encuentra."""
    for socio in socios:
        if socio["dni"] == dni:
            return socio
    return None


def registrar_socio(socios):
    """Pide datos por consola, valida y agrega un nuevo socio."""
    print("\n--- Registrar nuevo socio ---")

    nombre = input("Nombre y apellido: ").strip()
    while nombre == "":
        print("El nombre no puede estar vacío.")
        nombre = input("Nombre y apellido: ").strip()

    dni = input("DNI: ").strip()
    while not validar_dni(dni):
        print("DNI inválido. Debe contener solo números (mínimo 7 dígitos).")
        dni = input("DNI: ").strip()

    if buscar_socio_por_dni(socios, dni) is not None:
        print("Ya existe un socio registrado con ese DNI.")
        return

    nuevo_id = str(len(socios) + 1)
    nuevo_socio = {
        "id": nuevo_id,
        "nombre": nombre,
        "dni": dni,
        "membresia": "Sin asignar",
        "pago_al_dia": "No",
    }
    socios.append(nuevo_socio)
    guardar_socios(socios)
    print(f"Socio '{nombre}' registrado con éxito (ID {nuevo_id}).")


def listar_socios(socios):
    """Muestra por consola todos los socios registrados."""
    print("\n--- Listado de socios ---")
    if len(socios) == 0:
        print("No hay socios registrados.")
        return
    for socio in socios:
        print(
            f"ID {socio['id']} | {socio['nombre']} | DNI {socio['dni']} | "
            f"Membresía: {socio['membresia']} | Pago al día: {socio['pago_al_dia']}"
        )
