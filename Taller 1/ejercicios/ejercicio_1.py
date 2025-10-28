#EJERCICIO 1: IMPLEMENTACIÓN BÁSICA

def buscar_string(lista_strings, string_buscado):
    """
    Realiza una búsqueda lineal en una lista de cadenas (strings).
    """

    comparaciones = 0  # Contador de comparaciones
    
    for i, valor in enumerate(lista_strings):
        comparaciones += 1  # Cada iteración es una comparación
        
        if valor == string_buscado:
            # Retorna el índice y el número de comparaciones
            return i, comparaciones

    # Si no se encuentra el elemento
    return -1, comparaciones


#PRUEBA

palabras = ["manzana", "pera", "uva", "mango", "fresa"]

#Caso 1: El elemento existe
indice, comps = buscar_string(palabras, "mango")
print(f"Resultado: índice={indice}, comparaciones={comps}")

#Caso 2: El elemento no existe
indice, comps = buscar_string(palabras, "sandía")
print(f"Resultado: índice={indice}, comparaciones={comps}")
