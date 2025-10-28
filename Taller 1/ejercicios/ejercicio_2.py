# EJERCICIO 2: BÚSQUEDA MÚLTIPLE


def buscar_elementos_condicion(lista, condicion_func):
    """
    Busca todos los elementos que cumplan la condición dada.
    """
    resultados = []  # Lista para guardar los elementos que cumplen la condición
    
    for elemento in lista:
        if condicion_func(elemento):  # Se evalúa la condición
            resultados.append(elemento)  # Si cumple, se agrega a resultados
    
    return resultados


#PRUEBAS

#Lista de ejemplo
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Caso 1: Buscar números pares
pares = buscar_elementos_condicion(numeros, lambda x: x % 2 == 0)
print("Números pares:", pares)  # Esperado: [2, 4, 6, 8, 10]

#Caso 2: Buscar números mayores que 5
mayores_que_5 = buscar_elementos_condicion(numeros, lambda x: x > 5)
print("Mayores que 5:", mayores_que_5)  # Esperado: [6, 7, 8, 9, 10]

#Caso 3: Buscar números impares menores que 7
impares_menores_7 = buscar_elementos_condicion(numeros, lambda x: x % 2 != 0 and x < 7)
print("Impares menores que 7:", impares_menores_7)  # Esperado: [1, 3, 5]
