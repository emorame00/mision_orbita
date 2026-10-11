# ============================================================
# Archivo: ejercicio3_soporte_tripulacion.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Integrante: Eddie Steven Mora Mesén
# Fecha: 10/10/2026    Versión: 1.0
# Descripción: Verificación del soporte para la tripulación.
# ============================================================

# Entradas: se asumen datos válidos y cantidades enteras positivas.
oxigeno_disponible = int(input('Oxígeno disponible (unidades): '))
oxigeno_requerido = int(input('Oxígeno requerido (unidades): '))
provisiones_disponibles = int(input('Provisiones disponibles (unidades): '))
provisiones_requeridas = int(input('Provisiones requeridas (unidades): '))

# Decisión y salida: todas las comparaciones deben cumplirse.
if (
    oxigeno_disponible >= oxigeno_requerido
    and provisiones_disponibles >= provisiones_requeridas
):
    print('La nave posee recursos suficientes para la tripulación.')
else:
    print('La nave no posee recursos suficientes para la tripulación.')
