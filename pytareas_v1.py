#PyTareas


#POO

class Tarea:
    """Clase para crear objetos Tarea"""

    # El método constructor (__init__) se llama automáticamente cuando creamos un nuevo Objeto.
    def __init__(self, nombre_de_tarea):

        # 'self' se refiere al objeto que estamos creando (la galleta individual).
        self.nombre = nombre_de_tarea  #Guarda el nombre
        self.completada = False  #Inicializa el estado como Falso (no completada)

    #Lo que la tarea puede hacer
    def marcar_como_completa(self):
        """Cambia el estado de la tarea a completada."""

        self.completada = True
        print(f"¡Tarea '{self.nombre}' marcada como completada! ✅")


#lista para guardar objetos tarea
tareas_objetos = []


#funciones para ver 
def mostrar_tareas(lista_objetos):
    """Muestra todas las tareas y su estado (marcado con [X] o [ ])."""

    if not lista_objetos: #verifica si la lista está vacía
        print("¡La lista está vacía!")
        return #salir de la funcion
    
    print("\n=============================")
    print("TU LISTA ACTUAL DE TAREAS:")
    print("=============================")

    for indice, tarea in enumerate(lista_objetos):

        #ternario para estado de completado
        estado = "[X]" if tarea.completada else "[ ]"

        #muestra el índice y la tarea
        print(f" {indice + 1}. {estado} {tarea.nombre}")
    print("=============================\n")


#funcion de agregar tarea
def agregar_tarea(lista_objetos):
    """Pide una tarea, crea un objeto Tarea y lo añade a la lista."""
    nueva_tarea_nombre = input("Escribe la nueva tarea: ")

    #creamos el objeto tarea a partir de la clase
    nuevo_objeto_tarea = Tarea(nueva_tarea_nombre)

    lista_objetos.append(nuevo_objeto_tarea) #append agrega al final de la lista
    print(f"Tarea añadida: '{nuevo_objeto_tarea.nombre}'")


#funcion para eliminar tarea
def eliminar_tarea(lista):
    """Pide al usuario un número y elimina la tarea correspondiente."""
    #primero se muestra la lista de tareas
    mostrar_tareas(lista)

    try:
        #pedimos el número (el indice para el usuario
        num_tarea_str = input("Introduce el NÚMERO de la tarea a eliminar: ")

        #convertimos la entrada a un entero
        num_tarea = int(num_tarea_str)

        #calculamos el indice real de python (restamos 1)
        indice_a_eliminar = num_tarea - 1

        #comprobamos que el indice este dentro de los limites de la lista
        if 0 <= indice_a_eliminar < len(lista):
            #guardamos el nombre de la tarea antes de eliminarla
            tarea_eliminada = lista[indice_a_eliminar]

            #usamos "del" para eliminar la tarea
            del lista[indice_a_eliminar]
            print(f"Tarea ELIMINADA: '{tarea_eliminada}'")

        else:
            print("Error: El número de tarea no es válido.")

    except ValueError:
        #Si el usuario no introduce un número válido
        print("Error: Por favor, introduce un número válido.")

    except Exception as e:
        #Manejo general de errores
        print(f"Ocurrió un error inesperado: {e}")


#bandera de control para el bucle
ejecutando = True

print("¡Bienvenido a PyTareas! 🗒️")

while ejecutando:
    #todo el codigo "dentro" del bucle con una sangria

    #input del usuario para escoger una opción
    opcion = input("Elige una opción (Añadir/Ver/Salir/Eliminar): ").lower()

    if opcion == "añadir":
        print("¡Perfecto! Vamos a agregar una nueva tarea.")
        # llamar a la función de agregar
        agregar_tarea(tareas_objetos)

    elif opcion == "ver":
        print("Aquí está tu lista de tareas.")
        # llamar a la función de ver
        mostrar_tareas(tareas_objetos)

    elif opcion == "eliminar":
        print("Entendido, que tarea quieres eliminar?")
        # llamar a la función de eliminar
        eliminar_tarea(tareas_objetos)

    elif opcion == "salir":
        print("Saliendo del programa PyTareas. ¡Adiós!")
        # codigo para detener el bucle
        ejecutando = False

    else:
        # Esta es la opción de "último recurso" si el usuario escribe algo inválido
        print(f"La opción '{opcion}' no es válida. Por favor, elige Añadir, Ver o Salir.")

print("Programa finalizado")