"""
ACTIVIDAD 1: ANÁLISIS DE RENDIMIENTO
------------------------------------
Objetivo:
    Comparar el rendimiento de la búsqueda lineal con diferentes tamaños de datos.

Instrucciones cumplidas:
    ✅ Generar listas de diferentes tamaños
    ✅ Buscar elementos en distintas posiciones (primero, medio, último, no existe)
    ✅ Registrar número de comparaciones y tiempo de ejecución
    ✅ Mostrar resultados formateados
"""

import random
import time



# Función 1: Generar una lista aleatoria de tamaño N

def generar_lista_aleatoria(tamaño):
    """Genera una lista de números aleatorios entre 1 y 1000."""
    return [random.randint(1, 1000) for _ in range(tamaño)]



# Función 2: Búsqueda lineal con estadísticas

def busqueda_lineal_con_estadisticas(lista, elemento):
    """
    Realiza una búsqueda lineal y devuelve estadísticas del proceso.

    Retorna:
        {
            'posicion': índice encontrado o -1,
            'comparaciones': número de comparaciones realizadas,
            'tiempo': duración de la búsqueda en segundos
        }
    """
    comparaciones = 0
    inicio = time.time()

    for i, valor in enumerate(lista):
        comparaciones += 1
        if valor == elemento:
            fin = time.time()
            return {
                'posicion': i,
                'comparaciones': comparaciones,
                'tiempo': fin - inicio
            }

    # Si no se encuentra el elemento
    fin = time.time()
    return {
        'posicion': -1,
        'comparaciones': comparaciones,
        'tiempo': fin - inicio
    }



# Función 3: Analizar el rendimiento para distintos tamaños
def analizar_rendimiento():
    tamaños = [100, 500, 1000, 5000, 10000]
    posiciones = ['primero', 'medio', 'ultimo', 'no_existe']

    print("\n===== ANÁLISIS DE RENDIMIENTO - BÚSQUEDA LINEAL =====\n")
    print(f"{'Tamaño':<10}{'Posición':<12}{'Comparaciones':<15}{'Tiempo (s)':<12}Observaciones")
    print("-" * 65)

    for tamaño in tamaños:
        lista = generar_lista_aleatoria(tamaño)

        for pos in posiciones:
            # Selección del elemento según la posición
            if pos == 'primero':
                elemento = lista[0]
                obs = "Elemento al inicio"
            elif pos == 'medio':
                elemento = lista[tamaño // 2]
                obs = "Elemento en el medio"
            elif pos == 'ultimo':
                elemento = lista[-1]
                obs = "Elemento al final"
            else:  # no_existe
                elemento = 9999  # Número fuera del rango
                obs = "Elemento no existe"

            resultado = busqueda_lineal_con_estadisticas(lista, elemento)

            print(f"{tamaño:<10}{pos:<12}{resultado['comparaciones']:<15}{resultado['tiempo']:<12.6f}{obs}")


analizar_rendimiento()
