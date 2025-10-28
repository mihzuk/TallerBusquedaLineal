#EJERCICIO 4: APLICACIÓN PRÁCTICA - SISTEMA DE BÚSQUEDA DE LIBROS


#Lista de libros de ejemplo
biblioteca = [
    {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "año": 1967, "género": "Realismo mágico", "disponible": True},
    {"titulo": "El amor en los tiempos del cólera", "autor": "Gabriel García Márquez", "año": 1985, "género": "Romance", "disponible": False},
    {"titulo": "1984", "autor": "George Orwell", "año": 1949, "género": "Distopía", "disponible": True},
    {"titulo": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes", "año": 1605, "género": "Clásico", "disponible": True},
    {"titulo": "Fahrenheit 451", "autor": "Ray Bradbury", "año": 1953, "género": "Ciencia ficción", "disponible": False},
]


#FUNCIONES DE BÚSQUEDA


def buscar_por_titulo(biblioteca, texto):
    """
    Busca libros cuyo título contenga el texto indicado (búsqueda parcial).
    Ejemplo: buscar 'amor' encuentra títulos con la palabra 'amor'.
    """
    resultados = []
    for libro in biblioteca:
        if texto.lower() in libro["titulo"].lower():
            resultados.append(libro)
    return resultados


def buscar_por_autor(biblioteca, autor):
    """Busca todos los libros escritos por un autor específico."""
    resultados = []
    for libro in biblioteca:
        if libro["autor"].lower() == autor.lower():
            resultados.append(libro)
    return resultados


def buscar_por_genero(biblioteca, genero):
    """Busca todos los libros que pertenezcan a un género determinado."""
    resultados = []
    for libro in biblioteca:
        if libro["género"].lower() == genero.lower():
            resultados.append(libro)
    return resultados


def buscar_por_año(biblioteca, año):
    """Busca todos los libros publicados en un año específico."""
    resultados = []
    for libro in biblioteca:
        if libro["año"] == año:
            resultados.append(libro)
    return resultados


def buscar_disponibles(biblioteca):
    """Devuelve todos los libros que estén disponibles para préstamo."""
    resultados = []
    for libro in biblioteca:
        if libro["disponible"]:
            resultados.append(libro)
    return resultados


#PRUEBAS DE FUNCIONAMIENTO

print(" Búsqueda por título (contiene 'amor'):")
for libro in buscar_por_titulo(biblioteca, "amor"):
    print("-", libro["titulo"])

print("\n Búsqueda por autor (Gabriel García Márquez):")
for libro in buscar_por_autor(biblioteca, "Gabriel García Márquez"):
    print("-", libro["titulo"])

print("\n Búsqueda por género (Ciencia ficción):")
for libro in buscar_por_genero(biblioteca, "Ciencia ficción"):
    print("-", libro["titulo"])

print("\n Búsqueda por año (1949):")
for libro in buscar_por_año(biblioteca, 1949):
    print("-", libro["titulo"])

print("\n Libros disponibles:")
for libro in buscar_disponibles(biblioteca):
    print("-", libro["titulo"])
