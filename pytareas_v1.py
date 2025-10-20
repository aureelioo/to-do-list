#PyTareas

#lista de tareas 
tareas = ["Preparar café", "Revisar el correo"]

#funciones para ver y añadir tareas
def mostrar_tareas(lista):
    """Muestra todas las tareas con su índice."""
    if not lista: #verifica si la lista está vacía
        print("¡La lista está vacía!")
        return #salir de la funcion
    
    print("\n=============================")
    print("TU LISTA ACTUAL DE TAREAS:")
    print("=============================")
    for indice, tarea in enumerate(lista):
        #muestra el índice y la tarea
        print(f" {indice + 1}. {tarea}")
    print("=============================\n")

#funcion de agregar tarea
def agregar_tarea(lista):
    """Pide una tarea y la añade a la lista."""
    nueva_tarea = input("Escribe la nueva tarea: ")
    lista.append(nueva_tarea) #append agrega al final de la lista
    print(f"Tarea añadida: '{nueva_tarea}'")


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
        agregar_tarea(tareas)

    elif opcion == "ver":
        print("Aquí está tu lista de tareas.")
        # llamar a la función de ver
        mostrar_tareas(tareas)

    elif opcion == "eliminar":
        print("Entendido, que tarea quieres eliminar?")
        # llamar a la función de eliminar
        eliminar_tarea(tareas)

    elif opcion == "salir":
        print("Saliendo del programa PyTareas. ¡Adiós!")
        # codigo para detener el bucle
        ejecutando = False

    else:
        # Esta es la opción de "último recurso" si el usuario escribe algo inválido
        print(f"La opción '{opcion}' no es válida. Por favor, elige Añadir, Ver o Salir.")

print("Programa finalizado")