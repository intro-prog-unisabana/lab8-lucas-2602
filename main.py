"""Laboratorio 8 - CLI del gestor de tareas."""

# TODO: Implementar CLI según README.md
import sys
from todo_manager import read_todo_file, write_todo_file

try:
    nombre_script = sys.argv[0]
    ruta_del_archivo = sys.argv[1]
    print(f"Command-line arguments:\n{ruta_del_archivo}\n")
    elementos_de_lista = read_todo_file(ruta_del_archivo)
    print("Task:")
    for elemento in elementos_de_lista:
        print(elemento)
except IndexError:
    print("Insufficient arguments provided!")