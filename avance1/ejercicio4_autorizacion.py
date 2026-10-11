# ============================================================
# Archivo: ejercicio4_autorizacion.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Integrante: Eddie Steven Mora Mesén
# Fecha: 11/10/2026    Versión: 1.0
# Descripción: Autorización inicial de lanzamiento.
# ============================================================

# Constantes: valores fijos establecidos por la consigna.
RESERVA_COMBUSTIBLE = 10

# Entradas: se asumen datos válidos y cantidades enteras positivas.
combustible_disponible = int(input('Combustible disponible (unidades): '))
combustible_ida = int(input('Combustible requerido de ida (unidades): '))
combustible_regreso = int(input('Combustible requerido de regreso (unidades): '))
oxigeno_disponible = int(input('Oxígeno disponible (unidades): '))
oxigeno_requerido = int(input('Oxígeno requerido (unidades): '))
energia_disponible = int(input('Energía disponible (unidades): '))
energia_requerida = int(input('Energía requerida (unidades): '))
provisiones_disponibles = int(input('Provisiones disponibles (unidades): '))
provisiones_requeridas = int(input('Provisiones requeridas (unidades): '))

# Procesamiento: se incluye el regreso y la reserva de combustible.
combustible_total = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE

# Decisión y salida: todas las comparaciones deben cumplirse.
if (
    combustible_disponible >= combustible_total
    and oxigeno_disponible >= oxigeno_requerido
    and energia_disponible >= energia_requerida
    and provisiones_disponibles >= provisiones_requeridas
):
    print('Lanzamiento autorizado.')
else:
    print('Lanzamiento no autorizado. La misión debe ser revisada.')
