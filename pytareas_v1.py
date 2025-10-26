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

# Función guardar las tareas para despues cargarlas
def guardar_tareas(lista_objetos, nombre_archivo="tareas.csv"):
    """Guarda la lista de objetos Tarea en un archivo CSV,"""
    try:
        #Abrimos el archivo en modo "w" (escritura)
        with open(nombre_archivo, "w") as archivo:
            for tarea in lista_objetos:
                #Obtenemos el nombre y el estado (convertimos el booleano a cadena)
                linea = f"{tarea.nombre},{tarea.completada}\n"

                #escribimos la linea en el archivo
                archivo.write(linea)
        print(f"\n💾 {len(lista_objetos)} tareas guardadas en '{nombre_archivo}'")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")
    
# Función para cargar las tareas desde un archivo
def cargar_tareas(nombre_archivo="tareas.csv"):
    """Carga tareas desde un archivo CSV y devuelve una lista de objetos Trea."""
    lista_cargada = []
    try:
        #Abrimos el archivo en modo "r" (lectura)
        with open(nombre_archivo, "r") as archivo:
            for linea in archivo:
                #Limpiamos la linea (quitamos  el "\n" y espacios)
                linea_limpia = linea.strip()
                #Separamos el nombre y el estado por la coma
                nombre, estado_str = linea_limpia.split(',')
                #Convertimos el estado string a booleano
                estado_completado = (estado_str == "True") #Sera True si el string es "True", False en otro caso
                #Creamos el nuevo objeto tarea
                nueva_tarea = Tarea(nombre)
                nueva_tarea.completada = estado_completado
                #Añadimos el objeto a la lista
                lista_cargada.append(nueva_tarea)
            return lista_cargada
                
        print(f"\n📥 {len(lista_cargada)} tareas cargadas desde '{nombre_archivo}' al iniciar.")
    except FileNotFoundError:
        #Esto es normal la primera vez que se ejecuta el programa
        print(f"Archivo {nombre_archivo}no encontrado. Iniciando con lista vacía.")
        return []
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return []

#lista para guardar objetos tarea
tareas_objetos = cargar_tareas()


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
def eliminar_tarea(lista_objetos):
    """Pide al usuario un número y elimina la tarea correspondiente."""
    #primero se muestra la lista de tareas
    mostrar_tareas(lista_objetos)

    try:
        #pedimos el número (el indice para el usuario
        num_tarea_str = input("Introduce el NÚMERO de la tarea a eliminar: ")

        #convertimos la entrada a un entero
        num_tarea = int(num_tarea_str)

        #calculamos el indice real de python (restamos 1)
        indice_a_eliminar = num_tarea - 1

        #comprobamos que el indice este dentro de los limites de la lista
        if 0 <= indice_a_eliminar < len(lista_objetos):
            #guardamos el objeto, pero accedemos a su .nombre para la confirmacion
            tarea_a_confirmar = lista_objetos[indice_a_eliminar]
            nombre_eliminado = tarea_a_confirmar.nombre

            #usamos "del" para eliminar la tarea
            del lista_objetos[indice_a_eliminar]
            print(f"Tarea ELIMINADA: '{nombre_eliminado}'")

        else:
            print("Error: El número de tarea no es válido.")

    except ValueError:
        #Si el usuario no introduce un número válido
        print("Error: Por favor, introduce un número válido.")

    except Exception as e:
        #Manejo general de errores
        print(f"Ocurrió un error inesperado: {e}")


#Funcion para maracar tarea como completa
def completar_tarea(lista_objetos):
    """Pide un número de tarea y llama al método para marcarla como completada."""

    mostrar_tareas(lista_objetos)

    try:
        num_tarea_str = input("Introduce el NÚMERO de la tarea a marcar como completada: ")
        num_tarea = int(num_tarea_str)
        indice_a_completar = num_tarea - 1  #el indice real de python

        #validacion similar a la de eliminar
        if 0 <= indice_a_completar < len(lista_objetos):

            #obtenemos el objeto tarea
            tarea_a_modificar = lista_objetos[indice_a_completar]

            #llamamos al método para marcar como completa
            tarea_a_modificar.marcar_como_completa()

        else:
            print("Error: El número de tarea no es válido.")
    
    except ValueError:
        print("Error: Por favor, introduce un número válido.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


#bandera de control para el bucle
ejecutando = True

print("¡Bienvenido a PyTareas! 🗒️")

while ejecutando:
    #todo el codigo "dentro" del bucle con una sangria

    #input del usuario para escoger una opción
    opcion = input("Elige una opción (Añadir/Ver/Salir/Eliminar/Completar): ").lower()

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

    elif opcion == "completar":
        print("Vamos a marcar una tarea como completada.")
        #llamar a la funcion de completar
        completar_tarea(tareas_objetos)

    else:
        # Esta es la opción de "último recurso" si el usuario escribe algo inválido
        print(f"La opción '{opcion}' no es válida. Por favor, elige Añadir, Ver o Salir.")

#Guardar las tareas al salir
guardar_tareas(tareas_objetos)
print("Programa finalizado")