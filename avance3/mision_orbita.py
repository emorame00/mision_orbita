# Archivo: mision_orbita.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Integrante: Eddie Steven Mora Mesén
# Fecha: 20/11/2026    Versión: 1.0
# Descripción: Sistema integrado Misión Órbita para trabajo individual.

# Constantes: catálogos fijos y posiciones de listas y matrices.
DESTINOS = (("Luna", 3), ("Marte", 5), ("Europa", 7))
ACTIVIDADES = (("Analizar terreno", 0, 8, 0, 10),
               ("Recolectar muestra", 0, 12, 2, 20),
               ("Realizar observación", 0, 5, 0, 8),
               ("Sobrevolar la zona", 15, 3, 0, 25))
RECURSOS = ("combustible", "oxígeno", "energía", "provisiones")
RECURSOS_VITALES = ("oxígeno", "energía", "provisiones")
RESULTADOS = ("Regreso exitoso", "Regreso interrumpido", "Tripulación varada",
              "No autorizada", "No planificada")
DES_NOMBRE = 0
DES_DIAS = 1
ACT_NOMBRE = 0
ACT_COMBUSTIBLE = 1
ACT_ENERGIA = 2
ACT_PROVISIONES = 3
ACT_PUNTOS = 4
COMBUSTIBLE = 0
OXIGENO = 1
ENERGIA = 2
PROVISIONES = 3
BIT_NUMERO = 0
BIT_ACTIVIDAD = 1
BIT_PUNTOS = 2
MIS_NUMERO = 0
MIS_NOMBRE = 1
MIS_DESTINO = 2
MIS_RESULTADO = 3
MIS_PUNTOS = 4

# Constantes de cálculo: ida y vuelta más las reservas de planificación.
CONSUMO_COMBUSTIBLE_DIARIO = 8
CONSUMO_OXIGENO_TRIPULANTE = 2
CONSUMO_ENERGIA_DIARIO = 5
CONSUMO_PROVISIONES_TRIPULANTE = 1
CANTIDAD_TRAYECTOS = 2
RESERVA_COMBUSTIBLE = 10
OXIGENO_EMERGENCIA = 5
ENERGIA_EXPLORACION = 10
PROVISIONES_ADICIONALES = 3
MARGEN_MINIMO_COMBUSTIBLE = 10


def mostrar_destinos():
    # Salida: numerar el catálogo sin modificarlo.
    print("Destinos disponibles:")
    numero = 1
    for destino in DESTINOS:
        print(f"{numero}. {destino[DES_NOMBRE]} ({destino[DES_DIAS]} días)")
        numero = numero + 1


def leer_recursos():
    # Entrada: conservar el mismo orden de la tupla RECURSOS.
    recursos = []
    for recurso in RECURSOS:
        cantidad = int(input(f"Cantidad disponible de {recurso}: "))
        recursos.append(cantidad)
    return recursos


def calcular_requeridos(dias_viaje, tripulantes):
    # Procesamiento: reservar recursos para ambos trayectos.
    combustible = (dias_viaje * CONSUMO_COMBUSTIBLE_DIARIO
                   * CANTIDAD_TRAYECTOS + RESERVA_COMBUSTIBLE)
    oxigeno = (dias_viaje * CONSUMO_OXIGENO_TRIPULANTE
               * CANTIDAD_TRAYECTOS * tripulantes + OXIGENO_EMERGENCIA)
    energia = (dias_viaje * CONSUMO_ENERGIA_DIARIO
               * CANTIDAD_TRAYECTOS + ENERGIA_EXPLORACION)
    provisiones = (dias_viaje * tripulantes * CONSUMO_PROVISIONES_TRIPULANTE
                   * CANTIDAD_TRAYECTOS + PROVISIONES_ADICIONALES)
    requeridos = [combustible, oxigeno, energia, provisiones]
    return requeridos


def mostrar_resumen(nombre_mision, nombre_destino, dias_viaje, tripulantes,
                    disponibles, requeridos):
    # Salida: comparar las existencias con los requisitos de planificación.
    print(f"Misión: {nombre_mision}")
    print(f"Destino: {nombre_destino}")
    print(f"Duración del viaje de ida: {dias_viaje} días")
    print(f"Tripulantes: {tripulantes}")
    for i in range(len(RECURSOS)):
        print(f"{RECURSOS[i].capitalize()}: disponible {disponibles[i]} | "
              f"requerido {requeridos[i]}")
    margen = disponibles[COMBUSTIBLE] - requeridos[COMBUSTIBLE]
    print(f"Margen adicional de combustible: {margen} unidades")
    # Decisión: la advertencia no sustituye la autorización.
    if margen < MARGEN_MINIMO_COMBUSTIBLE:
        print("Advertencia: el margen adicional de combustible es bajo.")


def autorizar_lanzamiento(disponibles, requeridos):
    # Decisión: basta un recurso insuficiente para rechazar la misión.
    autorizado = True
    for i in range(len(RECURSOS)):
        if disponibles[i] < requeridos[i]:
            autorizado = False
    return autorizado


def calcular_consumo_diario(tripulantes):
    # Procesamiento: oxígeno y provisiones dependen de la tripulación.
    consumo = [CONSUMO_COMBUSTIBLE_DIARIO,
               CONSUMO_OXIGENO_TRIPULANTE * tripulantes,
               CONSUMO_ENERGIA_DIARIO,
               CONSUMO_PROVISIONES_TRIPULANTE * tripulantes]
    return consumo


def viajar_al_destino(recursos, dias_viaje, tripulantes):
    # Procesamiento: el alcance individual usa descuento directo en la ida.
    consumo = calcular_consumo_diario(tripulantes)
    for i in range(len(RECURSOS)):
        recursos[i] = recursos[i] - consumo[i] * dias_viaje
    return recursos


def recursos_alcanzan(recursos, consumo):
    # Decisión: comprobar todos los recursos antes de consumir un día.
    alcanzan = True
    for i in range(len(RECURSOS)):
        if recursos[i] < consumo[i]:
            alcanzan = False
    return alcanzan


def simular_trayecto(recursos, dias, tripulantes):
    # Inicialización: no se descuenta un día que no pueda completarse.
    consumo = calcular_consumo_diario(tripulantes)
    dias_completados = 0
    puede_continuar = True
    while dias_completados < dias and puede_continuar:
        alcanzan = recursos_alcanzan(recursos, consumo)
        if alcanzan:
            # Procesamiento: actualizar la misma lista recibida.
            for i in range(len(RECURSOS)):
                recursos[i] = recursos[i] - consumo[i]
            dias_completados = dias_completados + 1
            # Salida: estado al terminar el día, en el orden de RECURSOS.
            print(f"Día {dias_completados} | Combustible: {recursos[COMBUSTIBLE]}"
                  f" | Oxígeno: {recursos[OXIGENO]} | Energía: {recursos[ENERGIA]}"
                  f" | Provisiones: {recursos[PROVISIONES]}")
        else:
            puede_continuar = False
    return dias_completados


def mostrar_recursos(recursos):
    # Salida: cada posición tiene el mismo significado en ambas listas.
    print("Recursos restantes:")
    for i in range(len(RECURSOS)):
        print(f"- {RECURSOS[i].capitalize()}: {recursos[i]} unidades")


def mostrar_menu_actividades():
    # Salida: obtener la numeración a partir del catálogo.
    numero = 1
    for actividad in ACTIVIDADES:
        print(f"{numero}. {actividad[ACT_NOMBRE]}")
        numero = numero + 1
    print(f"{len(ACTIVIDADES) + 1}. Finalizar exploración")


def explorar(recursos):
    # Inicialización: la bitácora registra solo actividades completadas.
    print("=== EXPLORACIÓN ===")
    bitacora = []
    exploracion_activa = True
    while exploracion_activa:
        # Entrada: repetir las opciones inválidas sin consumir recursos.
        mostrar_menu_actividades()
        opcion = int(input("Seleccione una actividad: "))
        if 1 <= opcion <= len(ACTIVIDADES):
            actividad = ACTIVIDADES[opcion - 1]
            if (recursos[COMBUSTIBLE] >= actividad[ACT_COMBUSTIBLE]
                    and recursos[ENERGIA] >= actividad[ACT_ENERGIA]
                    and recursos[PROVISIONES] >= actividad[ACT_PROVISIONES]):
                # Procesamiento: la exploración no consume oxígeno.
                recursos[COMBUSTIBLE] = (recursos[COMBUSTIBLE]
                                         - actividad[ACT_COMBUSTIBLE])
                recursos[ENERGIA] = recursos[ENERGIA] - actividad[ACT_ENERGIA]
                recursos[PROVISIONES] = (recursos[PROVISIONES]
                                         - actividad[ACT_PROVISIONES])
                fila = [len(bitacora) + 1, actividad[ACT_NOMBRE],
                        actividad[ACT_PUNTOS]]
                bitacora.append(fila)
                print(f"Actividad realizada: {actividad[ACT_NOMBRE]}. "
                      f"Puntos obtenidos: {actividad[ACT_PUNTOS]}")
            else:
                # Decisión: el primer intento sin recursos termina la exploración.
                print("Recursos insuficientes para realizar la actividad. "
                      "La exploración finaliza.")
                exploracion_activa = False
        elif opcion == len(ACTIVIDADES) + 1:
            print("Exploración finalizada por la tripulación.")
            exploracion_activa = False
        else:
            print("Opción no válida.")
    return bitacora


def contar_actividad(bitacora, nombre_actividad):
    # Procesamiento: contar coincidencias sin count().
    cantidad = 0
    for fila in bitacora:
        if fila[BIT_ACTIVIDAD] == nombre_actividad:
            cantidad = cantidad + 1
    return cantidad


def calcular_puntos(bitacora):
    # Procesamiento: acumular puntos sin sum().
    total = 0
    for fila in bitacora:
        total = total + fila[BIT_PUNTOS]
    return total


def mostrar_resumen_exploracion(bitacora, recursos):
    # Salida: derivar los totales de las actividades registradas.
    muestras = contar_actividad(bitacora, "Recolectar muestra")
    puntos = calcular_puntos(bitacora)
    print(f"Actividades realizadas: {len(bitacora)}")
    print(f"Muestras recolectadas: {muestras}")
    print(f"Puntos científicos: {puntos}")
    mostrar_recursos(recursos)


def puede_regresar(recursos, dias_viaje):
    # Decisión: el regreso no exige conservar la reserva de planificación.
    alcanza_combustible = (recursos[COMBUSTIBLE]
                           >= dias_viaje * CONSUMO_COMBUSTIBLE_DIARIO)
    return alcanza_combustible


def calcular_supervivencia(recursos, tripulantes):
    # Procesamiento: contar únicamente días completos de soporte vital.
    dias_oxigeno = (recursos[OXIGENO]
                    // (tripulantes * CONSUMO_OXIGENO_TRIPULANTE))
    dias_energia = recursos[ENERGIA] // CONSUMO_ENERGIA_DIARIO
    dias_provisiones = (recursos[PROVISIONES]
                        // (tripulantes * CONSUMO_PROVISIONES_TRIPULANTE))
    dias_por_recurso = [dias_oxigeno, dias_energia, dias_provisiones]
    return dias_por_recurso


def obtener_limitantes(dias_por_recurso, minimo):
    # Procesamiento: incluir todos los empates, en el orden de soporte vital.
    limitantes = []
    for i in range(len(RECURSOS_VITALES)):
        if dias_por_recurso[i] == minimo:
            limitantes.append(RECURSOS_VITALES[i])
    return limitantes


def regresar(recursos, dias_viaje, tripulantes):
    # Decisión: primero comprobar el combustible para todo el regreso.
    print("=== REGRESO ===")
    regreso_posible = puede_regresar(recursos, dias_viaje)
    if regreso_posible:
        dias_completados = simular_trayecto(recursos, dias_viaje, tripulantes)
        if dias_completados == dias_viaje:
            print("La tripulación regresó exitosamente a la Tierra.")
            mostrar_recursos(recursos)
            resultado = "Regreso exitoso"
        else:
            # Salida: informar todos los recursos que impidieron el próximo día.
            print(f"El regreso se interrumpió en el día {dias_completados + 1}.")
            consumo = calcular_consumo_diario(tripulantes)
            for i in range(len(RECURSOS)):
                if recursos[i] < consumo[i]:
                    print(f"Recurso insuficiente: {RECURSOS[i]}")
            print("La tripulación no completó el regreso.")
            resultado = "Regreso interrumpido"
    else:
        # Procesamiento: la supervivencia se estima sin descontar recursos.
        print("La tripulación quedó varada en el destino.")
        dias_por_recurso = calcular_supervivencia(recursos, tripulantes)
        for i in range(len(RECURSOS_VITALES)):
            print(f"Días por {RECURSOS_VITALES[i]}: {dias_por_recurso[i]}")
        minimo = min(dias_por_recurso)
        limitantes = obtener_limitantes(dias_por_recurso, minimo)
        print(f"Supervivencia estimada: {minimo} días")
        print("Recurso(s) limitante(s): " + ", ".join(limitantes))
        resultado = "Tripulación varada"
    return resultado


def obtener_puntos_actividad(fila):
    # Procesamiento: criterio usado por sorted().
    puntos = fila[BIT_PUNTOS]
    return puntos


def ordenar_bitacora(bitacora):
    # Procesamiento: sorted conserva el orden original cuando hay empate.
    ordenada = sorted(bitacora, key=obtener_puntos_actividad, reverse=True)
    return ordenada


def mostrar_reporte(mision, bitacora):
    # Salida: también se emite para misiones rechazadas o no planificadas.
    print("=== REPORTE FINAL ===")
    print(f"Misión: {mision[MIS_NOMBRE]}")
    print(f"Destino: {mision[MIS_DESTINO]}")
    print(f"Resultado: {mision[MIS_RESULTADO]}")
    print(f"Puntos científicos: {mision[MIS_PUNTOS]}")
    print("Bitácora de exploración (de mayor a menor puntaje):")
    if len(bitacora) == 0:
        print("Sin actividades registradas.")
    else:
        ordenada = ordenar_bitacora(bitacora)
        for fila in ordenada:
            print(f"#{fila[BIT_NUMERO]} {fila[BIT_ACTIVIDAD]} - "
                  f"{fila[BIT_PUNTOS]} puntos")


def ejecutar_mision(numero):
    # Entrada: recoger los datos de planificación antes de pedir recursos.
    print("=== PLANIFICACIÓN ===")
    nombre_mision = input("Nombre de la misión: ")
    tripulantes = int(input("Cantidad de tripulantes: "))
    mostrar_destinos()
    opcion = int(input("Seleccione un destino: "))
    bitacora = []
    nombre_destino = "Ninguno"
    resultado = "No planificada"
    if 1 <= opcion <= len(DESTINOS):
        destino = DESTINOS[opcion - 1]
        nombre_destino = destino[DES_NOMBRE]
        dias_viaje = destino[DES_DIAS]
        recursos = leer_recursos()
        requeridos = calcular_requeridos(dias_viaje, tripulantes)
        mostrar_resumen(nombre_mision, nombre_destino, dias_viaje,
                        tripulantes, recursos, requeridos)
        autorizado = autorizar_lanzamiento(recursos, requeridos)
        if autorizado:
            # Procesamiento: integrar ida, llegada, exploración y regreso.
            print("Lanzamiento autorizado.")
            print("=== VIAJE DE IDA ===")
            recursos = viajar_al_destino(recursos, dias_viaje, tripulantes)
            print(f"La nave llegó a {nombre_destino} en {dias_viaje} días.")
            mostrar_recursos(recursos)
            bitacora = explorar(recursos)
            mostrar_resumen_exploracion(bitacora, recursos)
            resultado = regresar(recursos, dias_viaje, tripulantes)
        else:
            print("Lanzamiento no autorizado. La misión debe ser revisada.")
            resultado = "No autorizada"
    else:
        print("Opción de destino no válida. La misión no puede planificarse.")
    # Salida: todas las rutas generan exactamente un reporte y una fila.
    puntos = calcular_puntos(bitacora)
    mision = [numero, nombre_mision, nombre_destino, resultado, puntos]
    mostrar_reporte(mision, bitacora)
    return mision


def mostrar_menu_principal():
    # Salida: opciones correspondientes al trabajo individual.
    print("===== MISIÓN ÓRBITA =====")
    print("1. Planificar y ejecutar una misión")
    print("2. Ver historial de misiones")
    print("3. Salir")


def obtener_puntos_mision(mision):
    # Procesamiento: criterio de ordenamiento del historial.
    puntos = mision[MIS_PUNTOS]
    return puntos


def ordenar_historial(historial):
    # Procesamiento: ordenar una copia; los empates conservan su número.
    ordenado = sorted(historial, key=obtener_puntos_mision, reverse=True)
    return ordenado


def linea_mision(mision):
    # Procesamiento: compartir el formato de cada fila del historial.
    linea = (f"#{mision[MIS_NUMERO]} {mision[MIS_NOMBRE]} | "
             f"{mision[MIS_DESTINO]} | {mision[MIS_RESULTADO]} | "
             f"{mision[MIS_PUNTOS]} puntos")
    return linea


def mostrar_historial(historial):
    # Salida: mostrar el historial ordenado sin cambiar el original.
    print("=== HISTORIAL DE MISIONES ===")
    if len(historial) == 0:
        print("No hay misiones registradas.")
    else:
        ordenado = ordenar_historial(historial)
        for mision in ordenado:
            linea = linea_mision(mision)
            print(linea)


def main():
    # Inicialización: el historial pertenece a esta ejecución del programa.
    historial = []
    sistema_activo = True
    while sistema_activo:
        # Entrada: repetir el menú hasta seleccionar salir.
        mostrar_menu_principal()
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            mision = ejecutar_mision(len(historial) + 1)
            historial.append(mision)
        elif opcion == 2:
            mostrar_historial(historial)
        elif opcion == 3:
            sistema_activo = False
        else:
            print("Opción no válida.")
    # Salida: cerrar únicamente después de abandonar el ciclo.
    print("Fin del sistema Misión Órbita.")


main()
