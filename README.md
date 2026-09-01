# ADA 02: Agent Loop

Este repositorio contiene un ejemplo práctico y educativo sobre el patrón **Agent Loop** (el ciclo fundamental de percepción, decisión, ejecución y retroalimentación de agentes de IA) junto con un módulo de calculadora y su suite de pruebas unitarias.

---

## 📁 Estructura del Proyecto

* **[`calculator.py`](calculator.py)**: Módulo aritmético que implementa operaciones básicas:
  * `add(a, b)`: Suma.
  * `subtract(a, b)`: Resta.
  * `multiply(a, b)`: Multiplicación.
  * `divide(a, b)`: División.
  * `modulo(a, b)`: Operación módulo (residuo).
* **[`test_calculator.py`](test_calculator.py)**: Suite de pruebas unitarias con `pytest` para validar todas las operaciones de la calculadora.
* **[`agent_loop.py`](agent_loop.py)**: Implementación interactiva y simplificada del ciclo de un agente (`Task -> Decide -> Execute Tool -> Update Context`) con soporte para primitivas `READ`, `WRITE`, `EDIT` y `BASH`.
* **[`agent-run.md`](agent-run.md)**: Bitácora de iteraciones del agente durante la resolución de tareas en el repositorio.

---

## 🚀 Cómo Ejecutar

### 1. Ejecutar las Pruebas Unitarias
Para correr la suite de tests con `pytest`:

```powershell
python -m pytest
```

### 2. Ejecutar la Simulación del Agent Loop
Para probar el ciclo interactivo del agente:

```powershell
python agent_loop.py
```

---

## 🔄 El Ciclo Agent Loop

El flujo del agente sigue el siguiente patrón iterativo:

```
+-----------------------------------------------------------+
|                        Agent Loop                         |
|                                                           |
|   1. get_task()        --> Captura la tarea o instrucción |
|   2. decide_action()   --> Razona y selecciona la tool    |
|   3. execute_tool()    --> Ejecuta READ/WRITE/EDIT/BASH   |
|   4. update_context()  --> Actualiza memoria / contexto   |
+-----------------------------------------------------------+
```
