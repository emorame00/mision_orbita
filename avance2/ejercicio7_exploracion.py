# Archivo: ejercicio7_exploracion.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Integrante: Eddie Steven Mora Mesén
# Fecha: 21/10/2026    Versión: 1.0
# Descripción: Gestiona las actividades de exploración científica.

# Constantes: costos y puntos establecidos para cada actividad.
ENERGIA_TERRENO = 8
ENERGIA_MUESTRA = 12
ENERGIA_OBSERVACION = 5
PROVISIONES_MUESTRA = 2
PUNTOS_TERRENO = 10
PUNTOS_MUESTRA = 20
PUNTOS_OBSERVACION = 8

# Entradas: recursos que quedan al llegar al destino.
energia_disponible = int(input('Energía disponible al llegar al destino: '))
provisiones_disponibles = int(input('Provisiones disponibles al llegar al destino: '))

# Inicialización: la exploración comienza sin actividades ni puntos.
puntos_cientificos = 0
actividades_realizadas = 0
muestras_recolectadas = 0
exploracion_activa = True

# Menú: una opción inválida permite intentar otra vez.
while exploracion_activa:
    print('1. Analizar terreno')
    print('2. Recolectar muestra')
    print('3. Realizar observación')
    print('4. Finalizar exploración')
    opcion = int(input('Seleccione una actividad: '))

    # Selección: se asignan los costos antes de comprobar los recursos.
    if opcion == 1 or opcion == 2 or opcion == 3:
        if opcion == 1:
            nombre_actividad = 'Analizar terreno'
            energia_actividad = ENERGIA_TERRENO
            provisiones_actividad = 0
            puntos_actividad = PUNTOS_TERRENO
        elif opcion == 2:
            nombre_actividad = 'Recolectar muestra'
            energia_actividad = ENERGIA_MUESTRA
            provisiones_actividad = PROVISIONES_MUESTRA
            puntos_actividad = PUNTOS_MUESTRA
        else:
            nombre_actividad = 'Realizar observación'
            energia_actividad = ENERGIA_OBSERVACION
            provisiones_actividad = 0
            puntos_actividad = PUNTOS_OBSERVACION

        # Solo una actividad completada cambia recursos y resultados.
        if (energia_disponible >= energia_actividad
                and provisiones_disponibles >= provisiones_actividad):
            energia_disponible = energia_disponible - energia_actividad
            provisiones_disponibles = provisiones_disponibles - provisiones_actividad
            actividades_realizadas = actividades_realizadas + 1
            puntos_cientificos = puntos_cientificos + puntos_actividad
            if opcion == 2:
                muestras_recolectadas = muestras_recolectadas + 1
            print('Actividad realizada:', nombre_actividad + '.',
                  'Puntos obtenidos:', puntos_actividad)
        else:
            print('Recursos insuficientes para realizar la actividad. '
                  'La exploración finaliza.')
            exploracion_activa = False
    elif opcion == 4:
        print('Exploración finalizada por la tripulación.')
        exploracion_activa = False
    else:
        print('Opción no válida.')

# Salidas: se conserva el orden indicado en la consigna.
print('Actividades realizadas:', actividades_realizadas)
print('Muestras recolectadas:', muestras_recolectadas)
print('Puntos científicos:', puntos_cientificos)
print('Energía restante:', energia_disponible, 'unidades')
print('Provisiones restantes:', provisiones_disponibles, 'unidades')
