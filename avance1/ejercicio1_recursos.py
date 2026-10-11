# ============================================================
# Archivo: ejercicio1_recursos.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Integrante: Eddie Steven Mora Mesén
# Fecha: 10/10/2026    Versión: 1.0
# Descripción: Cálculo de recursos necesarios para una misión.
# ============================================================

# Constantes: valores fijos establecidos por la consigna.
CONSUMO_COMBUSTIBLE_DIARIO = 8
RESERVA_COMBUSTIBLE = 10
TRAYECTOS = 2
CONSUMO_OXIGENO_DIARIO = 2
RESERVA_OXIGENO = 5
CONSUMO_ENERGIA_DIARIO = 5
ENERGIA_EXPLORACION = 10
CONSUMO_PROVISIONES_DIARIO = 1
RESERVA_PROVISIONES = 3

# Entradas: se asumen datos válidos y cantidades enteras positivas.
nombre_mision = input('Nombre de la misión: ')
cantidad_tripulantes = int(input('Cantidad de tripulantes: '))
dias_viaje = int(input('Días estimados de ida: '))

# Procesamiento: se incluye el regreso y la reserva de combustible.
# El soporte vital y la energía cubren ambos trayectos.
combustible_ida = dias_viaje * CONSUMO_COMBUSTIBLE_DIARIO
combustible_regreso = dias_viaje * CONSUMO_COMBUSTIBLE_DIARIO
combustible_total = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE
oxigeno_requerido = (
    dias_viaje
    * TRAYECTOS
    * cantidad_tripulantes
    * CONSUMO_OXIGENO_DIARIO
    + RESERVA_OXIGENO
)
energia_requerida = (
    dias_viaje
    * TRAYECTOS
    * CONSUMO_ENERGIA_DIARIO
    + ENERGIA_EXPLORACION
)
provisiones_requeridas = (
    dias_viaje
    * TRAYECTOS
    * cantidad_tripulantes
    * CONSUMO_PROVISIONES_DIARIO
    + RESERVA_PROVISIONES
)

# Salidas: resumen con las unidades correspondientes.
print('Misión:', nombre_mision)
print('Tripulantes:', cantidad_tripulantes)
print('Duración estimada hasta el destino:', dias_viaje, 'días')
print('Combustible para llegar:', combustible_ida, 'unidades')
print('Combustible para regresar:', combustible_regreso, 'unidades')
print('Reserva de combustible:', RESERVA_COMBUSTIBLE, 'unidades')
print('Combustible total requerido:', combustible_total, 'unidades')
print('Oxígeno requerido:', oxigeno_requerido, 'unidades')
print('Energía requerida:', energia_requerida, 'unidades')
print('Provisiones requeridas:', provisiones_requeridas, 'unidades')