"""
EJERCICIOS PRÁCTICOS - BÚSQUEDA LINEAL
======================================

Este archivo contiene ejercicios paso a paso para practicar la implementación
del algoritmo de búsqueda lineal en el contexto de una tienda de electrónica.

INSTRUCCIONES:
- Completa cada función según las especificaciones
- Prueba tu código con los casos de prueba proporcionados
- No modifiques las funciones de prueba
"""

# =============================================================================
# EJERCICIO 1: IMPLEMENTACIÓN BÁSICA DE BÚSQUEDA LINEAL
# =============================================================================

def busqueda_lineal_simple(lista, elemento):
    """
    Busca un elemento en una lista usando búsqueda lineal.
    
    Args:
        lista: Lista de elementos donde buscar
        elemento: Elemento a buscar
    
    Returns:
        int: Índice del elemento si se encuentra, -1 si no se encuentra
    
    TODO: Implementa esta función usando un bucle for
    """
    # TU CÓDIGO AQUÍ
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1

def prueba_ejercicio_1():
    """Prueba la función de búsqueda lineal básica."""
    print("🧪 EJERCICIO 1: Búsqueda Lineal Básica")
    print("-" * 40)
    
    # Casos de prueba
    numeros = [64, 34, 25, 12, 22, 11, 90]
    
    # Prueba 1: Elemento encontrado
    resultado = busqueda_lineal_simple(numeros, 25)
    print(f"Buscando 25 en {numeros}: Índice {resultado}")
    assert resultado == 2, f"Esperado: 2, Obtenido: {resultado}"
    
    # Prueba 2: Elemento no encontrado
    resultado = busqueda_lineal_simple(numeros, 99)
    print(f"Buscando 99 en {numeros}: Índice {resultado}")
    assert resultado == -1, f"Esperado: -1, Obtenido: {resultado}"
    
    # Prueba 3: Lista vacía
    resultado = busqueda_lineal_simple([], 5)
    print(f"Buscando 5 en lista vacía: Índice {resultado}")
    assert resultado == -1, f"Esperado: -1, Obtenido: {resultado}"
    
    print("✅ ¡Ejercicio 1 completado correctamente!\n")

# =============================================================================
# EJERCICIO 2: BÚSQUEDA EN LISTA DE DICCIONARIOS
# =============================================================================

def buscar_producto_por_nombre(productos, nombre_buscado):
    """
    Busca un producto por nombre en una lista de diccionarios.
    
    Args:
        productos: Lista de diccionarios de productos
        nombre_buscado: Nombre del producto a buscar
    
    Returns:
        dict o None: Diccionario del producto si se encuentra, None si no
    
    TODO: Implementa esta función usando búsqueda lineal
    """
    # TU CÓDIGO AQUÍ
    for producto in productos:
        if producto['nombre'] == nombre_buscado:
            return producto
    return None

def buscar_productos_por_marca(productos, marca_buscada):
    """
    Busca todos los productos de una marca específica.
    
    Args:
        productos: Lista de diccionarios de productos
        marca_buscada: Marca a buscar
    
    Returns:
        list: Lista de productos que coinciden con la marca
    
    TODO: Implementa esta función usando búsqueda lineal
    """
    # TU CÓDIGO AQUÍ
    resultado = []
    for producto in productos:
        if producto['marca'] == marca_buscada:
            resultado.append(producto)
    return resultado

def prueba_ejercicio_2():
    """Prueba las funciones de búsqueda en productos."""
    print("🧪 EJERCICIO 2: Búsqueda en Productos")
    print("-" * 40)
    
    # Datos de prueba
    productos = [
        {'id': 1, 'nombre': 'iPhone 15', 'marca': 'Apple', 'precio': 999.99},
        {'id': 2, 'nombre': 'Samsung Galaxy S24', 'marca': 'Samsung', 'precio': 899.99},
        {'id': 3, 'nombre': 'MacBook Air M3', 'marca': 'Apple', 'precio': 1299.99},
        {'id': 4, 'nombre': 'Dell XPS 13', 'marca': 'Dell', 'precio': 1199.99}
    ]
    
    # Prueba 1: Buscar por nombre
    producto = buscar_producto_por_nombre(productos, 'iPhone 15')
    print(f"Buscando 'iPhone 15': {producto['nombre'] if producto else 'No encontrado'}")
    assert producto is not None, "Producto debería ser encontrado"
    assert producto['nombre'] == 'iPhone 15', "Nombre del producto incorrecto"
    
    # Prueba 2: Buscar producto que no existe
    producto = buscar_producto_por_nombre(productos, 'Producto Inexistente')
    print(f"Buscando 'Producto Inexistente': {'Encontrado' if producto else 'No encontrado'}")
    assert producto is None, "Producto no debería ser encontrado"
    
    # Prueba 3: Buscar por marca
    productos_apple = buscar_productos_por_marca(productos, 'Apple')
    print(f"Productos de Apple: {len(productos_apple)} encontrados")
    assert len(productos_apple) == 2, f"Deberían encontrarse 2 productos, se encontraron {len(productos_apple)}"
    
    print("✅ ¡Ejercicio 2 completado correctamente!\n")

# =============================================================================
# EJERCICIO 3: BÚSQUEDA CON CRITERIOS MÚLTIPLES
# =============================================================================

def buscar_productos_disponibles(productos):
    """
    Busca productos disponibles (stock > 0 y disponible = True).
    
    Args:
        productos: Lista de diccionarios de productos
    
    Returns:
        list: Lista de productos disponibles
    
    TODO: Implementa esta función verificando ambas condiciones
    """
    # TU CÓDIGO AQUÍ
    disponibles = []
    for producto in productos:
        if producto['stock'] > 0 and producto['disponible']:
            disponibles.append(producto)
    return disponibles

def buscar_productos_por_rango_precio(productos, precio_min, precio_max):
    """
    Busca productos dentro de un rango de precios.
    
    Args:
        productos: Lista de diccionarios de productos
        precio_min: Precio mínimo
        precio_max: Precio máximo
    
    Returns:
        list: Lista de productos dentro del rango
    
    TODO: Implementa esta función verificando el rango de precios
    """
    # TU CÓDIGO AQUÍ
    resultado = []
    for producto in productos:
        if precio_min <= producto['precio'] <= precio_max:
            resultado.append(producto)
    return resultado

def prueba_ejercicio_3():
    """Prueba las funciones de búsqueda con criterios múltiples."""
    print("🧪 EJERCICIO 3: Búsqueda con Criterios Múltiples")
    print("-" * 40)
    
    # Datos de prueba
    productos = [
        {'id': 1, 'nombre': 'iPhone 15', 'precio': 999.99, 'stock': 10, 'disponible': True},
        {'id': 2, 'nombre': 'Samsung Galaxy S24', 'precio': 899.99, 'stock': 0, 'disponible': False},
        {'id': 3, 'nombre': 'MacBook Air M3', 'precio': 1299.99, 'stock': 5, 'disponible': True},
        {'id': 4, 'nombre': 'Dell XPS 13', 'precio': 1199.99, 'stock': 3, 'disponible': True},
        {'id': 5, 'nombre': 'Producto Barato', 'precio': 99.99, 'stock': 1, 'disponible': True}
    ]
    
    # Prueba 1: Productos disponibles
    disponibles = buscar_productos_disponibles(productos)
    print(f"Productos disponibles: {len(disponibles)}")
    assert len(disponibles) == 4, f"Deberían encontrarse 4 productos disponibles, se encontraron {len(disponibles)}"
    
    # Prueba 2: Rango de precios
    productos_rango = buscar_productos_por_rango_precio(productos, 800, 1200)
    print(f"Productos entre $800 y $1200: {len(productos_rango)}")
    assert len(productos_rango) == 3, f"Deberían encontrarse 3 productos en el rango, se encontraron {len(productos_rango)}"
    
    print("✅ ¡Ejercicio 3 completado correctamente!\n")

# =============================================================================
# EJERCICIO 4: BÚSQUEDA DE EMPLEADOS
# =============================================================================

def buscar_empleado_por_id(empleados, id_buscado):
    """
    Busca un empleado por ID.
    
    Args:
        empleados: Lista de diccionarios de empleados
        id_buscado: ID del empleado a buscar
    
    Returns:
        dict o None: Diccionario del empleado si se encuentra, None si no
    
    TODO: Implementa esta función usando búsqueda lineal
    """
    # TU CÓDIGO AQUÍ
    for empleado in empleados:
        if empleado['id'] == id_buscado:
            return empleado
    return None

def buscar_empleados_por_departamento(empleados, departamento):
    """
    Busca empleados de un departamento específico.
    
    Args:
        empleados: Lista de diccionarios de empleados
        departamento: Departamento a buscar
    
    Returns:
        list: Lista de empleados del departamento
    
    TODO: Implementa esta función usando búsqueda lineal
    """
    # TU CÓDIGO AQUÍ
    resultado = []
    for empleado in empleados:
        if empleado['departamento'] == departamento:
            resultado.append(empleado)
    return resultado

def prueba_ejercicio_4():
    """Prueba las funciones de búsqueda de empleados."""
    print("🧪 EJERCICIO 4: Búsqueda de Empleados")
    print("-" * 40)
    
    # Datos de prueba
    empleados = [
        {'id': 101, 'nombre': 'Ana', 'apellido': 'García', 'departamento': 'Ventas', 'activo': True},
        {'id': 102, 'nombre': 'Carlos', 'apellido': 'López', 'departamento': 'Técnico', 'activo': True},
        {'id': 103, 'nombre': 'María', 'apellido': 'Rodríguez', 'departamento': 'Ventas', 'activo': False},
        {'id': 104, 'nombre': 'José', 'apellido': 'Martínez', 'departamento': 'Inventario', 'activo': True}
    ]
    
    # Prueba 1: Buscar por ID
    empleado = buscar_empleado_por_id(empleados, 102)
    print(f"Empleado con ID 102: {empleado['nombre'] if empleado else 'No encontrado'}")
    assert empleado is not None, "Empleado debería ser encontrado"
    assert empleado['nombre'] == 'Carlos', "Nombre del empleado incorrecto"
    
    # Prueba 2: Buscar empleado que no existe
    empleado = buscar_empleado_por_id(empleados, 999)
    print(f"Empleado con ID 999: {'Encontrado' if empleado else 'No encontrado'}")
    assert empleado is None, "Empleado no debería ser encontrado"
    
    # Prueba 3: Buscar por departamento
    empleados_ventas = buscar_empleados_por_departamento(empleados, 'Ventas')
    print(f"Empleados de Ventas: {len(empleados_ventas)}")
    assert len(empleados_ventas) == 2, f"Deberían encontrarse 2 empleados, se encontraron {len(empleados_ventas)}"
    
    print("✅ ¡Ejercicio 4 completado correctamente!\n")

# =============================================================================
# EJERCICIO 5: BÚSQUEDA AVANZADA Y ESTADÍSTICAS
# =============================================================================

def contar_productos_por_categoria(productos):
    """
    Cuenta cuántos productos hay en cada categoría.
    
    Args:
        productos: Lista de diccionarios de productos
    
    Returns:
        dict: Diccionario con categorías y sus conteos
    
    TODO: Implementa esta función usando búsqueda lineal
    """
    # TU CÓDIGO AQUÍ
    conteo = {}
    for producto in productos:
        categoria = producto['categoria']
        if categoria in conteo:
            conteo[categoria] += 1
        else:
            conteo[categoria] = 1
    return conteo

def obtener_valor_total_inventario(productos):
    """
    Calcula el valor total del inventario (precio * stock).
    
    Args:
        productos: Lista de diccionarios de productos
    
    Returns:
        float: Valor total del inventario
    
    TODO: Implementa esta función recorriendo todos los productos
    """
    # TU CÓDIGO AQUÍ
    total = 0
    for producto in productos:
        total += producto['precio'] * producto['stock']
    return total

def prueba_ejercicio_5():
    """Prueba las funciones de estadísticas."""
    print("🧪 EJERCICIO 5: Estadísticas y Conteos")
    print("-" * 40)
    
    # Datos de prueba
    productos = [
        {'id': 1, 'nombre': 'iPhone 15', 'categoria': 'Smartphone', 'precio': 999.99, 'stock': 10},
        {'id': 2, 'nombre': 'Samsung Galaxy S24', 'categoria': 'Smartphone', 'precio': 899.99, 'stock': 8},
        {'id': 3, 'nombre': 'MacBook Air M3', 'categoria': 'Laptop', 'precio': 1299.99, 'stock': 5},
        {'id': 4, 'nombre': 'Dell XPS 13', 'categoria': 'Laptop', 'precio': 1199.99, 'stock': 3},
        {'id': 5, 'nombre': 'AirPods Pro', 'categoria': 'Audífonos', 'precio': 249.99, 'stock': 20}
    ]
    
    # Prueba 1: Conteo por categoría
    conteo = contar_productos_por_categoria(productos)
    print(f"Conteo por categoría: {conteo}")
    assert conteo['Smartphone'] == 2, f"Deberían haber 2 smartphones, hay {conteo['Smartphone']}"
    assert conteo['Laptop'] == 2, f"Deberían haber 2 laptops, hay {conteo['Laptop']}"
    
    # Prueba 2: Valor total del inventario
    valor_total = obtener_valor_total_inventario(productos)
    print(f"Valor total del inventario: ${valor_total:.2f}")
    valor_esperado = (999.99 * 10) + (899.99 * 8) + (1299.99 * 5) + (1199.99 * 3) + (249.99 * 20)
    assert abs(valor_total - valor_esperado) < 0.01, f"Valor incorrecto. Esperado: {valor_esperado}, Obtenido: {valor_total}"
    
    print("✅ ¡Ejercicio 5 completado correctamente!\n")

# =============================================================================
# EJERCICIO 6: DESAFÍO - BÚSQUEDA CON CONTADOR DE COMPARACIONES
# =============================================================================

def busqueda_lineal_con_contador(lista, elemento):
    """
    Busca un elemento y cuenta las comparaciones realizadas.
    
    Args:
        lista: Lista de elementos donde buscar
        elemento: Elemento a buscar
    
    Returns:
        tuple: (índice, número_de_comparaciones)
    
    TODO: Implementa esta función contando cada comparación
    """
    # TU CÓDIGO AQUÍ
    comparaciones = 0
    for i in range(len(lista)):
        comparaciones += 1
        if lista[i] == elemento:
            return i, comparaciones
    return -1, comparaciones

def analizar_rendimiento_busqueda():
    """
    Analiza el rendimiento de la búsqueda lineal con diferentes tamaños de lista.
    
    TODO: Implementa esta función para mostrar cómo aumenta el número de comparaciones
    """
    print("🧪 EJERCICIO 6: Análisis de Rendimiento")
    print("-" * 40)
    
    # Casos de prueba con diferentes tamaños
    tamanos = [10, 50, 100, 500]
    
    for tamaño in tamanos:
        # Crear lista de números del 1 al tamaño
        lista = list(range(1, tamaño + 1))
        
        # Buscar el último elemento (peor caso)
        indice, comparaciones = busqueda_lineal_con_contador(lista, tamaño)
        
        print(f"Lista de {tamaño} elementos:")
        print(f"  - Buscando el último elemento ({tamaño})")
        print(f"  - Comparaciones realizadas: {comparaciones}")
        print(f"  - Complejidad: O({comparaciones})")
        print()

# =============================================================================
# FUNCIÓN PRINCIPAL PARA EJECUTAR TODAS LAS PRUEBAS
# =============================================================================

def ejecutar_todos_los_ejercicios():
    """Ejecuta todos los ejercicios y sus pruebas."""
    print("🚀 INICIANDO EJERCICIOS DE BÚSQUEDA LINEAL")
    print("=" * 60)
    print("📝 Instrucciones:")
    print("   1. Completa cada función según las especificaciones")
    print("   2. Ejecuta las pruebas para verificar tu implementación")
    print("   3. Si una prueba falla, revisa tu código y corrígelo")
    print("=" * 60)
    
    try:
        # Ejecutar pruebas (solo si las funciones están implementadas)
        prueba_ejercicio_1()
        prueba_ejercicio_2()
        prueba_ejercicio_3()
        prueba_ejercicio_4()
        prueba_ejercicio_5()
        analizar_rendimiento_busqueda()
        
        print("🎉 ¡TODOS LOS EJERCICIOS COMPLETADOS EXITOSAMENTE!")
        print("=" * 60)
        print("💡 Reflexiones:")
        print("   - ¿Cuál es la complejidad temporal de la búsqueda lineal?")
        print("   - ¿En qué casos es eficiente este algoritmo?")
        print("   - ¿Cuándo sería mejor usar otro algoritmo de búsqueda?")
        
    except NotImplementedError:
        print("⚠️  Algunas funciones no están implementadas aún.")
        print("   Completa las funciones marcadas con 'TODO' y vuelve a ejecutar.")
    except AssertionError as e:
        print(f"❌ Error en las pruebas: {e}")
        print("   Revisa tu implementación y corrige el error.")

if __name__ == "__main__":
    ejecutar_todos_los_ejercicios()

