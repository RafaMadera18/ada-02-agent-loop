def get_task():
    return input("Tarea: ")


def decide_action(task):
    task = task.lower()

    if "leer" in task or "read" in task:
        return "READ"
    elif "escribir" in task or "write" in task:
        return "WRITE"
    elif "editar" in task or "edit" in task:
        return "EDIT"
    elif "ejecutar" in task or "bash" in task:
        return "BASH"
    elif "terminar" in task or "salir" in task:
        return "FINISHED"

    return "READ"


def execute_tool(action):
    if action == "READ":
        return "Leyendo archivo..."

    elif action == "WRITE":
        return "Escribiendo archivo..."

    elif action == "EDIT":
        return "Editando archivo..."

    elif action == "BASH":
        return "Ejecutando comando BASH..."

    return "Acción desconocida"


def update_context(result):
    print(f"Resultado: {result}")


finished = False

while not finished:
    task = get_task()
    action = decide_action(task)

    if action == "FINISHED":
        finished = True
        print("Agent Loop finalizado.")
        continue

    print(f"Acción seleccionada: {action}")
    result = execute_tool(action)
    update_context(result)