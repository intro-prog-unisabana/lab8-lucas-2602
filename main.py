"""Laboratorio 8 - CLI del gestor de tareas."""

# TODO: Implementar CLI según README.md
import sys
from todo_manager import read_todo_file, write_todo_file

try:
    nombre_script = sys.argv[0]
    ruta_del_archivo = sys.argv[1]
except IndexError:
    print("Insufficient arguments provided!")