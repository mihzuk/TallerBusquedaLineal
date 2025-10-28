"""
ACTIVIDAD 2: BÚSQUEDA EN MÚLTIPLES CAMPOS

"""

import random
import time



# Clase Empleado

class Empleado:
    """Representa a un empleado de la empresa."""

    def __init__(self, nombre, departamento, salario, edad):
        self.nombre = nombre
        self.departamento = departamento
        self.salario = salario
        self.edad = edad

    def __repr__(self):
        """Representación amigable del objeto para impresión."""
        return f"{self.nombre} ({self.departamento}) - ${self.salario} - {self.edad} años"



# Función auxiliar: generar lista de empleados aleatorios

def generar_empleados(n):
    nombres = ["Ana", "Luis", "María", "Carlos", "Sofía", "Pedro", "Lucía", "Jorge", "Valentina", "Andrés"]
    departamentos = ["Ventas", "TI", "Recursos Humanos", "Finanzas", "Marketing"]

    empleados = []
    for _ in range(n):
        nombre = random.choice(nombres) + str(random.randint(1, 100))
        departamento = random.choice(departamentos)
        salario = random.randint(1000, 10000)
        edad = random.randint(20, 60)
        empleados.append(Empleado(nombre, departamento, salario, edad))

    return empleados



# Funciones de búsqueda lineal


def buscar_por_nombre(empleados, nombre):
    """Busca empleados por nombre exacto."""
    resultados = []
    for empleado in empleados:
        if empleado.nombre.lower() == nombre.lower():
            resultados.append(empleado)
    return resultados


def buscar_por_departamento(empleados, departamento):
    """Busca empleados por departamento."""
    resultados = []
    for empleado in empleados:
        if empleado.departamento.lower() == departamento.lower():
            resultados.append(empleado)
    return resultados


def buscar_por_rango_salario(empleados, salario_min, salario_max):
    """Busca empleados por rango de salario."""
    resultados = []
    for empleado in empleados:
        if salario_min <= empleado.salario <= salario_max:
            resultados.append(empleado)
    return resultados


def buscar_por_rango_edad(empleados, edad_min, edad_max):
    """Busca empleados por rango de edad."""
    resultados = []
    for empleado in empleados:
        if edad_min <= empleado.edad <= edad_max:
            resultados.append(empleado)
    return resultados


# Función para medir rendimiento de una búsqueda

def medir_rendimiento(funcion_busqueda, *args):
    """Mide el tiempo de ejecución y número de comparaciones estimadas."""
    inicio = time.time()
    resultados = funcion_busqueda(*args)
    fin = time.time()
    tiempo = fin - inicio

    # Aproximación: el número de comparaciones es el tamaño de la lista
    # ya que todas las funciones son búsquedas lineales
    total_comparaciones = len(args[0])

    return {
        "tiempo": tiempo,
        "comparaciones": total_comparaciones,
        "resultados": resultados
    }


# Ejecución del análisis de rendimiento

empleados = generar_empleados(5000)  # Base de datos simulada

print("\n===== ANÁLISIS DE RENDIMIENTO - BÚSQUEDAS MÚLTIPLES =====\n")
print(f"{'Tipo de Búsqueda':<25}{'Comparaciones':<15}{'Tiempo (s)':<12}Resultados encontrados")
print("-" * 70)

# Búsqueda por nombre
r1 = medir_rendimiento(buscar_por_nombre, empleados, "Ana50")
print(f"{'Por nombre':<25}{r1['comparaciones']:<15}{r1['tiempo']:<12.6f}{len(r1['resultados'])}")

# Búsqueda por departamento
r2 = medir_rendimiento(buscar_por_departamento, empleados, "TI")
print(f"{'Por departamento':<25}{r2['comparaciones']:<15}{r2['tiempo']:<12.6f}{len(r2['resultados'])}")

# Búsqueda por rango de salario
r3 = medir_rendimiento(buscar_por_rango_salario, empleados, 3000, 6000)
print(f"{'Por rango de salario':<25}{r3['comparaciones']:<15}{r3['tiempo']:<12.6f}{len(r3['resultados'])}")

# Búsqueda por rango de edad
r4 = medir_rendimiento(buscar_por_rango_edad, empleados, 30, 40)
print(f"{'Por rango de edad':<25}{r4['comparaciones']:<15}{r4['tiempo']:<12.6f}{len(r4['resultados'])}")
