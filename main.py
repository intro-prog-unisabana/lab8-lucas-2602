"""Laboratorio 8 - CLI del gestor de tareas."""

# TODO: Implementar CLI según README.md
import sys
from todo_manager import read_todo_file, write_todo_file

try:
    if len(sys.argv) < 2:
        raise IndexError("Insufficient arguments provided!")
    ruta_del_archivo = sys.argv[1]
    try:
        accion_a_realizar = sys.argv[2]
        #print(f"Command-line arguments:\n{ruta_del_archivo}\n")
        if accion_a_realizar == "view":
            elementos_de_lista = read_todo_file(ruta_del_archivo)
            print("Task:")
            for elemento in elementos_de_lista:
                print(elemento)
        else:
            raise ValueError("Command not found!")
    except IndexError:
        pass
except IndexError as error:
    print(error)
except ValueError as error:
    print(error)