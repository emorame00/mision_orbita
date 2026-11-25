# Misión Órbita

Proyecto del curso Principios de Programación 1.

*Estudiante:* Eddie Steven Mora Mesén  
*Sección:* SCV6

## Descripción

El proyecto consiste en un simulador de misiones espaciales desarrollado en Python. Los primeros dos avances contienen ejercicios independientes que posteriormente se integran en un solo programa en el tercer avance.

## Avance 1: Preparación de la misión

- Ejercicio 1: Calcula los recursos necesarios para la misión.
- Ejercicio 2: Comprueba si el combustible alcanza para la ida, el regreso y la reserva de emergencia.
- Ejercicio 3: Verifica si hay suficiente oxígeno y provisiones para la tripulación.
- Ejercicio 4: Determina si se autoriza el lanzamiento según los recursos disponibles.

## Avance 2: Exploración y regreso

- Ejercicio 7: Permite realizar actividades de exploración científica y obtener puntos.
- Ejercicio 8: Simula el regreso a la Tierra y calcula los días de supervivencia si la tripulación queda varada.

## Avance 3: Sistema integrado Misión Órbita

El programa integra las etapas de planificación, autorización del lanzamiento, viaje de ida, exploración científica y regreso a la Tierra.

También permite generar un reporte final de cada misión y consultar el historial de misiones ordenado de mayor a menor puntaje científico.

El sistema utiliza funciones, listas, tuplas y matrices para organizar y procesar la información.

## Archivos

- avance1/: contiene los programas de los ejercicios 1 al 4.
- avance2/: contiene los programas de los ejercicios 7 y 8.
- avance3/: contiene el programa integrado mision_orbita.py.
- documentacion/: contiene los informes de los tres avances y los diagramas de flujo.

## Cómo ejecutar los programas

1. Abrir la carpeta del proyecto en Visual Studio Code con Python 3 instalado.
2. Para ejecutar los ejercicios anteriores, abrir el archivo correspondiente de cada avance.
3. Para ejecutar el sistema integrado, abrir avance3/mision_orbita.py.
4. Presionar el botón de ejecutar archivo de Python.
5. Ingresar los datos solicitados en la terminal y presionar Enter después de cada dato.

El sistema integrado permite ejecutar varias misiones, consultar el historial y salir desde el menú principal.

También se puede ejecutar desde la terminal con el comando:

python avance3/mision_orbita.py

## Documentación y pruebas

El informe del tercer avance incluye las tablas de variables, los nueve diagramas de flujo, el código fuente y los 27 casos de prueba con sus respectivas capturas y resultados.

### Informes del proyecto

- [Primer avance](documentacion/avance1_mision_orbita.pdf)
- [Segundo avance](documentacion/avance2_mision_orbita.pdf)
- [Tercer avance](documentacion/avance3_mision_orbita.pdf)

### Diagramas de flujo

- [Diagramas editables del tercer avance](documentacion/Diagramas%20de%20Flujo/Diagramas_Flujo_avance3.drawio)

## Convenciones y estilo

Los nombres de las variables y funciones se escriben en minúsculas, con guiones bajos entre palabras. Las constantes se escriben en mayúsculas. Se utiliza sangría de cuatro espacios y comentarios para identificar los bloques del programa.

El sistema no requiere librerías externas.