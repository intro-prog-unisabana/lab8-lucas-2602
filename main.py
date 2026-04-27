"""Laboratorio 8 - CLI del gestor de tareas."""

# TODO: Implementar CLI según README.md
import sys
from todo_manager import read_todo_file, write_todo_file

try:
    if sys.argv[1] == "--help":
        print("""Usage: python main.py <file_path> <command> [arguments]...

Commands:
  add "task"    - Add a task to the list.
  remove "task" - Remove a task from the list.
  view          - Display all tasks.

Examples:
  python main.py tasks.txt add "Buy groceries"
  python main.py tasks.txt remove "Do laundry"
  python main.py tasks.txt view
  python main.py tasks.txt add "Call mom" remove "Take out trash" view""")
        sys.exit()
    
    if len(sys.argv) < 2:
        raise IndexError("Insufficient arguments provided!")
    
    if len(sys.argv) < 3:
        sys.exit()

    ruta_del_archivo = sys.argv[1]
    elementos_de_lista = read_todo_file(ruta_del_archivo)

    i = 2
    accion_a_realizar = sys.argv[i]

    if accion_a_realizar == "view":
        print("Task:")
        for elemento in elementos_de_lista:
            print(elemento)
        i += 1

    elif accion_a_realizar == "add":
        if len(sys.argv) < 4:
            raise IndexError('Task description required for "add".')
        
        elemento_a_agregar = sys.argv[3]
        elementos_de_lista.append(elemento_a_agregar)
        print(f'Task "{elemento_a_agregar}" added.')
        i += 2

    elif accion_a_realizar == "remove":
        if len(sys.argv) < 4:
            raise IndexError('Task description required for "remove".')
        
        elemento_a_eliminar = sys.argv[3]

        try:
            elementos_de_lista.remove(elemento_a_eliminar)
            print(f'Task "{elemento_a_eliminar}" remove.')
        except ValueError:
            print(f'Task "{elemento_a_eliminar}" not found.')
            
        i += 2

    else:
        raise ValueError("Command not found!")
    
except IndexError as error:
    print(error)

except ValueError as error:
    print(error)