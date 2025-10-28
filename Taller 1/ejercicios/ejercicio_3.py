import time
import random

"""
El ejercicio 3 para mayor demostración usamos los codigos dados para analizar la complejidad de estos.

"""

# Algoritmos dados

def algoritmo_a(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1

#Análisis de Complejidad:
#En el peor caso, el algoritmo revisa todos los elementos.
#Por tanto, su complejidad es:
#O(n)
#Donde n es el tamaño de la lista.
#En el mejor caso (si el elemento está al inicio), sería O(1).
#Promedio: O(n/2) ≈ O(n)


def algoritmo_b(lista, elemento):
    encontrado = False
    indice = 0
    while not encontrado and indice < len(lista):
        if lista[indice] == elemento:
            encontrado = True
        indice += 1
    return indice - 1 if encontrado else -1

#Análisis de Complejidad:
#Aunque usa un ciclo while, el número de iteraciones es el mismo
#que en el algoritmo A: recorre como máximo toda la lista.
#Complejidad temporal:
#Peor caso: O(n)
#Mejor caso: O(1)
#Promedio: O(n)
#Espacialmente, solo usa variables simples → O(1)

def algoritmo_c(lista, elemento):
    for i in range(len(lista)):
        for j in range(i, len(lista)):
            if lista[j] == elemento:
                return j
    return -1

#Análisis de Complejidad:
#Este algoritmo es mucho menos eficiente:
#Tiene dos bucles anidados.
#En el peor caso, el interno se ejecuta n - i veces para cada i.

#Total de operaciones ≈ n + (n-1) + (n-2) + ... + 1 = n(n+1)/2 → O(n²)

#Por tanto:
#Peor caso: O(n²)
#Mejor caso: O(1) (si el elemento está al inicio)
#Promedio: O(n²)
#Complejidad espacial: O(1)

#Función para medir tiempo de ejecución

def medir_tiempo(funcion, lista, elemento):
    inicio = time.time()
    resultado = funcion(lista, elemento)
    fin = time.time()
    return fin - inicio, resultado


#Prueba con listas grandes

def prueba_complejidad():
    tamanos = [1000, 3000, 5000]
    for n in tamanos:
        lista = list(range(n))
        elemento_no_existe = -1  #Un elemento que no está en la lista
        
        print(f"\n🔹 Tamaño de lista: {n} elementos")
        
        #Algoritmo A
        tiempo_a, _ = medir_tiempo(algoritmo_a, lista, elemento_no_existe)
        print(f"Algoritmo A - Tiempo: {tiempo_a:.6f} s (O(n))")
        
        #Algoritmo B
        tiempo_b, _ = medir_tiempo(algoritmo_b, lista, elemento_no_existe)
        print(f"Algoritmo B - Tiempo: {tiempo_b:.6f} s (O(n))")
        
        #Algoritmo C
        #Este es mucho más lento, así que mejor usar listas pequeñas
        if n <= 3000:
            tiempo_c, _ = medir_tiempo(algoritmo_c, lista, elemento_no_existe)
            print(f"Algoritmo C - Tiempo: {tiempo_c:.6f} s (O(n²))")
        else:
            print(f"Algoritmo C - (omitido, muy lento para {n} elementos)")



#prueba

prueba_complejidad()
