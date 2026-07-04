# Sistema de Gestión de Gimnasio

Trabajo Final Integrador — sistema de consola en Python para administrar socios,
membresías, actividades y asistencia de un gimnasio.

**Universidad Tecnológica Nacional — Facultad Regional Resistencia**
**Comisión:** K1.3

## Integrantes del grupo

- Antonio Benitez
- Gonzalo Jesús Mendoza
- Lucio Nicolás Pereyra
- Lucas Ezequiel Rafaul


## Cómo correrlo

```
cd gimnasio
python main.py
```

Al ejecutarse se crea automáticamente la carpeta `datos/` con los archivos
`socios.csv`, `inscripciones.csv` y `asistencias.csv`. Ahí queda guardada
toda la información entre una ejecución y otra.

## Estructura del proyecto (para repartirse el trabajo)

| Archivo             | Qué hace                                                        |
|----------------------|-------------------------------------------------------------------|
| `main.py`            | Menú principal. Conecta todos los módulos.                        |
| `socios.py`          | Alta, listado y búsqueda de socios.                                |
| `membresias.py`      | Tipos de membresía, asignación y control de pagos (cuotas).       |
| `actividades.py`     | Inscripción de socios a actividades del gimnasio.                 |
| `asistencia.py`      | Registro de asistencia diaria.                                    |
| `estadisticas.py`    | Estadísticas básicas: total de socios, recaudación, actividad más popular, socio con más asistencias. |

Cada módulo es independiente y solo se comunica con los demás a través de
funciones (no hay clases). Esto permite que cada integrante del grupo se
haga cargo de un archivo y lo entienda por completo, incluso si no participó
en los demás.

## Cómo cumple cada requisito de la consigna

- **Condicionales**: validaciones de datos, chequeo de opciones de menú, control de pagos/asistencia (`if`/`elif`/`else` en todos los módulos).
- **Repetitivas**: el menú principal es un `while True`; hay `while` para reintentar datos inválidos y `for` para recorrer listas.
- **Funciones**: todo el sistema está dividido en funciones con una sola responsabilidad cada una.
- **Validaciones**: DNI numérico, nombre no vacío, opciones de menú, DNI ya registrado, socio inexistente, pago pendiente.
- **Acumuladores y contadores**: `contador` en socios deudores, diccionarios `conteo` en estadísticas, `total` en recaudación.
- **Modularización**: 6 módulos + `main.py`.
- **Manejo de errores**: `try/except` al leer/escribir los archivos CSV y alrededor de cada opción del menú.

## IAs utilizadas
Se uso extensivamente la IA para el trabajo, integrado en el codigo, tanto para los diversos comentarios en los codigos, ideas de como estructuras por modulos y codigo en si (creacion de archivos para guardar datos)

La IA usada fue Claude Sonnet 4.6