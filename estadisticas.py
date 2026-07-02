"""
Módulo de estadísticas.
Calcula estadísticas básicas a partir de los socios, inscripciones y asistencias.
"""


def total_socios(socios):
    return len(socios)


def total_recaudado(socios, tipos_membresia):
    """Suma (acumulador) lo recaudado por socios que están al día."""
    total = 0
    for socio in socios:
        if socio["pago_al_dia"] == "Sí":
            for nombre, precio in tipos_membresia.values():
                if socio["membresia"] == nombre:
                    total += precio
    return total


def actividad_mas_popular(inscripciones):
    """Devuelve la actividad con más inscriptos usando un diccionario contador."""
    conteo = {}
    for inscripcion in inscripciones:
        actividad = inscripcion["actividad"]
        conteo[actividad] = conteo.get(actividad, 0) + 1

    if len(conteo) == 0:
        return None, 0

    actividad_top = None
    cantidad_top = 0
    for actividad, cantidad in conteo.items():
        if cantidad > cantidad_top:
            actividad_top = actividad
            cantidad_top = cantidad
    return actividad_top, cantidad_top


def socio_mas_asistio(asistencias):
    """Devuelve el DNI del socio con más asistencias registradas."""
    conteo = {}
    for asistencia in asistencias:
        dni = asistencia["dni_socio"]
        conteo[dni] = conteo.get(dni, 0) + 1

    if len(conteo) == 0:
        return None, 0

    dni_top = None
    cantidad_top = 0
    for dni, cantidad in conteo.items():
        if cantidad > cantidad_top:
            dni_top = dni
            cantidad_top = cantidad
    return dni_top, cantidad_top


def mostrar_estadisticas(socios, inscripciones, asistencias, tipos_membresia):
    print("\n--- Estadísticas del gimnasio ---")
    print(f"Cantidad total de socios: {total_socios(socios)}")
    print(f"Total recaudado (socios al día): ${total_recaudado(socios, tipos_membresia)}")

    actividad, cantidad = actividad_mas_popular(inscripciones)
    if actividad is not None:
        print(f"Actividad más popular: {actividad} ({cantidad} inscriptos)")
    else:
        print("Todavía no hay inscripciones a actividades.")

    dni_top, cantidad_top = socio_mas_asistio(asistencias)
    if dni_top is not None:
        print(f"Socio con más asistencias: DNI {dni_top} ({cantidad_top} veces)")
    else:
        print("Todavía no hay asistencias registradas.")
