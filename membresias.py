"""
Módulo de membresías.
Maneja los tipos de membresía disponibles, la asignación a un socio
y el registro de pagos (control de cuotas).
"""

from socios import buscar_socio_por_dni, guardar_socios

# Diccionario fijo con los tipos de membresía: clave -> (nombre, precio)
TIPOS_MEMBRESIA = {
    "1": ("Mensual", 15000),
    "2": ("Trimestral", 40000),
    "3": ("Anual", 140000),
}


def mostrar_tipos_membresia():
    print("\n--- Tipos de membresía ---")
    for clave, (nombre, precio) in TIPOS_MEMBRESIA.items():
        print(f"{clave}) {nombre} - ${precio}")


def asignar_membresia(socios):
    """Asigna un tipo de membresía a un socio existente."""
    dni = input("Ingrese el DNI del socio: ").strip()
    socio = buscar_socio_por_dni(socios, dni)
    if socio is None:
        print("No se encontró ningún socio con ese DNI.")
        return

    mostrar_tipos_membresia()
    opcion = input("Seleccione el tipo de membresía: ").strip()
    while opcion not in TIPOS_MEMBRESIA:
        print("Opción inválida.")
        opcion = input("Seleccione el tipo de membresía: ").strip()

    nombre_membresia, precio = TIPOS_MEMBRESIA[opcion]
    socio["membresia"] = nombre_membresia
    socio["pago_al_dia"] = "Sí"
    guardar_socios(socios)
    print(f"Membresía '{nombre_membresia}' asignada. Total a pagar: ${precio}")


def registrar_pago(socios):
    """Marca a un socio como 'al día' con el pago de su cuota."""
    dni = input("Ingrese el DNI del socio: ").strip()
    socio = buscar_socio_por_dni(socios, dni)
    if socio is None:
        print("No se encontró ningún socio con ese DNI.")
        return
    if socio["membresia"] == "Sin asignar":
        print("Este socio todavía no tiene una membresía asignada.")
        return

    socio["pago_al_dia"] = "Sí"
    guardar_socios(socios)
    print("Pago registrado. El socio quedó al día.")


def listar_deudores(socios):
    """Lista los socios que tienen el pago pendiente. Usa un contador."""
    print("\n--- Socios con pago pendiente ---")
    contador = 0
    for socio in socios:
        if socio["pago_al_dia"] == "No":
            print(f"{socio['nombre']} (DNI {socio['dni']})")
            contador += 1

    if contador == 0:
        print("No hay socios con pagos pendientes.")
    else:
        print(f"Total de socios con deuda: {contador}")
