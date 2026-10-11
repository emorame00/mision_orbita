# ============================================================
# Archivo: ejercicio2_combustible.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Integrante: Eddie Steven Mora Mesén
# Fecha: 10/10/2026    Versión: 1.0
# Descripción: Verificación de combustible.
# ============================================================

# Constantes: valores fijos establecidos por la consigna.
RESERVA_COMBUSTIBLE = 10
MARGEN_ADICIONAL_MINIMO = 10

# Entradas: se asumen datos válidos y cantidades enteras positivas.
combustible_disponible = int(input('Combustible disponible (unidades): '))
combustible_ida = int(input('Combustible requerido de ida (unidades): '))
combustible_regreso = int(input('Combustible requerido de regreso (unidades): '))

# Procesamiento: se incluye el regreso y la reserva de combustible.
combustible_total = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE
combustible_adicional = combustible_disponible - combustible_total

# Salidas: resumen con las unidades correspondientes.
print('Combustible disponible:', combustible_disponible, 'unidades')
print('Combustible para llegar:', combustible_ida, 'unidades')
print('Combustible para regresar:', combustible_regreso, 'unidades')
print('Reserva de emergencia:', RESERVA_COMBUSTIBLE, 'unidades')
print('Combustible total requerido:', combustible_total, 'unidades')
print('Combustible adicional:', combustible_adicional, 'unidades')

# Decisión y salida: se advierte solo si el margen es bajo.
if combustible_adicional < MARGEN_ADICIONAL_MINIMO:
    print('Advertencia: el margen adicional de combustible es bajo.')
