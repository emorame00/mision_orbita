# Archivo: ejercicio8_regreso.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Integrante: Eddie Steven Mora Mesén
# Fecha: 21/10/2026    Versión: 1.0
# Descripción: Simula el regreso o calcula la supervivencia en el destino.

# Constantes: consumos diarios de la nave y de cada tripulante.
CONSUMO_COMBUSTIBLE_DIARIO = 8
CONSUMO_OXIGENO_TRIPULANTE = 2
CONSUMO_ENERGIA_DIARIO = 5
CONSUMO_PROVISIONES_TRIPULANTE = 1

# Entradas: estado de la nave después de la exploración.
cantidad_tripulantes = int(input('Cantidad de tripulantes: '))
dias_ida = int(input('Cantidad de días del viaje de ida: '))
combustible_disponible = int(input('Combustible disponible: '))
oxigeno_disponible = int(input('Oxígeno disponible: '))
energia_disponible = int(input('Energía disponible: '))
provisiones_disponibles = int(input('Provisiones disponibles: '))

# Procesamiento: el regreso no incluye la reserva de emergencia.
combustible_regreso = dias_ida * CONSUMO_COMBUSTIBLE_DIARIO
oxigeno_diario = cantidad_tripulantes * CONSUMO_OXIGENO_TRIPULANTE
provisiones_diarias = cantidad_tripulantes * CONSUMO_PROVISIONES_TRIPULANTE

# Caso A: el combustible alcanza para todo el regreso.
if combustible_disponible >= combustible_regreso:
    dias_completados = 0
    regreso_activo = True
    while dias_completados < dias_ida and regreso_activo:
        # Se comprueban todos los recursos antes de descontar el día.
        if (combustible_disponible >= CONSUMO_COMBUSTIBLE_DIARIO
                and oxigeno_disponible >= oxigeno_diario
                and energia_disponible >= CONSUMO_ENERGIA_DIARIO
                and provisiones_disponibles >= provisiones_diarias):
            combustible_disponible = combustible_disponible - CONSUMO_COMBUSTIBLE_DIARIO
            oxigeno_disponible = oxigeno_disponible - oxigeno_diario
            energia_disponible = energia_disponible - CONSUMO_ENERGIA_DIARIO
            provisiones_disponibles = provisiones_disponibles - provisiones_diarias
            dias_completados = dias_completados + 1
            print('Día', dias_completados, '| Combustible:', combustible_disponible,
                  '| Oxígeno:', oxigeno_disponible, '| Energía:', energia_disponible,
                  '| Provisiones:', provisiones_disponibles)
        else:
            regreso_activo = False

    # Salidas del regreso: éxito o todos los recursos que faltaron.
    if dias_completados == dias_ida:
        print('La tripulación regresó exitosamente a la Tierra.')
        print('Combustible restante:', combustible_disponible, 'unidades')
        print('Oxígeno restante:', oxigeno_disponible, 'unidades')
        print('Energía restante:', energia_disponible, 'unidades')
        print('Provisiones restantes:', provisiones_disponibles, 'unidades')
    else:
        dia_interrumpido = dias_completados + 1
        print('El regreso se interrumpió en el día', str(dia_interrumpido) + '.')
        if oxigeno_disponible < oxigeno_diario:
            print('Recurso insuficiente: oxígeno')
        if energia_disponible < CONSUMO_ENERGIA_DIARIO:
            print('Recurso insuficiente: energía')
        if provisiones_disponibles < provisiones_diarias:
            print('Recurso insuficiente: provisiones')
        print('La tripulación no completó el regreso.')
else:
    # Caso B: divisiones enteras para contar únicamente días completos.
    print('La tripulación quedó varada en el destino.')
    dias_oxigeno = oxigeno_disponible // oxigeno_diario
    dias_energia = energia_disponible // CONSUMO_ENERGIA_DIARIO
    dias_provisiones = provisiones_disponibles // provisiones_diarias

    # El mínimo se obtiene con condicionales, sin min() ni max().
    dias_supervivencia = dias_oxigeno
    if dias_energia < dias_supervivencia:
        dias_supervivencia = dias_energia
    if dias_provisiones < dias_supervivencia:
        dias_supervivencia = dias_provisiones

    # Las decisiones independientes incluyen todos los empates, en orden.
    recursos_limitantes = ''
    if dias_oxigeno == dias_supervivencia:
        recursos_limitantes = 'oxígeno'
    if dias_energia == dias_supervivencia:
        if recursos_limitantes != '':
            recursos_limitantes = recursos_limitantes + ', '
        recursos_limitantes = recursos_limitantes + 'energía'
    if dias_provisiones == dias_supervivencia:
        if recursos_limitantes != '':
            recursos_limitantes = recursos_limitantes + ', '
        recursos_limitantes = recursos_limitantes + 'provisiones'

    # Salidas de supervivencia: no se consumen recursos en este caso.
    print('Días por oxígeno:', dias_oxigeno)
    print('Días por energía:', dias_energia)
    print('Días por provisiones:', dias_provisiones)
    print('Supervivencia estimada:', dias_supervivencia, 'días')
    print('Recurso(s) limitante(s):', recursos_limitantes)
