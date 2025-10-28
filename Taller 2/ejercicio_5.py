import tkinter as tk
from tkinter import messagebox, simpledialog

# =====================================================
# DATOS DE EJEMPLO
# =====================================================
INVENTARIO = [
    {'id': 1, 'nombre': 'iPhone 15', 'marca': 'Apple', 'precio': 999.99, 'stock': 10, 'disponible': True, 'categoria': 'Smartphone'},
    {'id': 2, 'nombre': 'Samsung Galaxy S24', 'marca': 'Samsung', 'precio': 899.99, 'stock': 8, 'disponible': True, 'categoria': 'Smartphone'},
    {'id': 3, 'nombre': 'MacBook Air M3', 'marca': 'Apple', 'precio': 1299.99, 'stock': 5, 'disponible': True, 'categoria': 'Laptop'},
    {'id': 4, 'nombre': 'Dell XPS 13', 'marca': 'Dell', 'precio': 1199.99, 'stock': 3, 'disponible': True, 'categoria': 'Laptop'},
    {'id': 5, 'nombre': 'AirPods Pro', 'marca': 'Apple', 'precio': 249.99, 'stock': 20, 'disponible': True, 'categoria': 'Audífonos'}
]

EMPLEADOS = [
    {'id': 101, 'nombre': 'Ana', 'apellido': 'García', 'departamento': 'Ventas', 'activo': True},
    {'id': 102, 'nombre': 'Carlos', 'apellido': 'López', 'departamento': 'Técnico', 'activo': True},
    {'id': 103, 'nombre': 'María', 'apellido': 'Rodríguez', 'departamento': 'Ventas', 'activo': False},
    {'id': 104, 'nombre': 'José', 'apellido': 'Martínez', 'departamento': 'Inventario', 'activo': True}
]

# =====================================================
# FUNCIONES DE BÚSQUEDA LINEAL
# =====================================================
def buscar_producto_por_nombre(nombre):
    for producto in INVENTARIO:
        if producto['nombre'].lower() == nombre.lower():
            return producto
    return None

def buscar_productos_por_marca(marca):
    return [p for p in INVENTARIO if p['marca'].lower() == marca.lower()]

def buscar_productos_por_rango_precio(minimo, maximo):
    return [p for p in INVENTARIO if minimo <= p['precio'] <= maximo]

def buscar_productos_disponibles():
    return [p for p in INVENTARIO if p['disponible'] and p['stock'] > 0]

def buscar_empleado_por_id(id_empleado):
    for e in EMPLEADOS:
        if e['id'] == id_empleado:
            return e
    return None

def buscar_empleados_por_departamento(departamento):
    return [e for e in EMPLEADOS if e['departamento'].lower() == departamento.lower()]

def obtener_valor_total_inventario():
    return sum(p['precio'] * p['stock'] for p in INVENTARIO)

# =====================================================
# FUNCIONES DE INTERFAZ
# =====================================================
def mostrar_resultado(titulo, texto):
    messagebox.showinfo(titulo, texto)

# ---- Submenú Productos ----
def menu_productos():
    win = tk.Toplevel(root)
    win.title("Búsqueda de Productos")
    win.geometry("400x400")

    def buscar_nombre():
        nombre = simpledialog.askstring("Buscar", "Nombre exacto del producto:")
        producto = buscar_producto_por_nombre(nombre)
        if producto:
            mostrar_resultado("Producto encontrado", f"{producto['nombre']} - ${producto['precio']}")
        else:
            mostrar_resultado("No encontrado", "No se encontró ese producto.")

    def buscar_marca():
        marca = simpledialog.askstring("Buscar", "Marca del producto:")
        resultados = buscar_productos_por_marca(marca)
        texto = "\n".join([f"{p['nombre']} - ${p['precio']}" for p in resultados]) or "No se encontraron productos."
        mostrar_resultado(f"Productos de {marca}", texto)

    def buscar_rango_precio():
        minimo = simpledialog.askfloat("Precio mínimo", "Ingresa el precio mínimo:")
        maximo = simpledialog.askfloat("Precio máximo", "Ingresa el precio máximo:")
        resultados = buscar_productos_por_rango_precio(minimo, maximo)
        texto = "\n".join([f"{p['nombre']} - ${p['precio']}" for p in resultados]) or "No se encontraron productos."
        mostrar_resultado("Rango de precios", texto)

    def productos_disponibles():
        disponibles = buscar_productos_disponibles()
        texto = "\n".join([f"{p['nombre']} - stock {p['stock']}" for p in disponibles])
        mostrar_resultado("Productos disponibles", texto)

    tk.Button(win, text="Buscar por nombre", command=buscar_nombre, width=30).pack(pady=5)
    tk.Button(win, text="Buscar por marca", command=buscar_marca, width=30).pack(pady=5)
    tk.Button(win, text="Buscar por rango de precio", command=buscar_rango_precio, width=30).pack(pady=5)
    tk.Button(win, text="Ver productos disponibles", command=productos_disponibles, width=30).pack(pady=5)
    tk.Button(win, text="Cerrar", command=win.destroy, width=30).pack(pady=10)

# ---- Submenú Empleados ----
def menu_empleados():
    win = tk.Toplevel(root)
    win.title("Búsqueda de Empleados")
    win.geometry("400x300")

    def buscar_id():
        id_empleado = simpledialog.askinteger("Buscar", "ID del empleado:")
        emp = buscar_empleado_por_id(id_empleado)
        if emp:
            mostrar_resultado("Empleado encontrado", f"{emp['nombre']} {emp['apellido']} - {emp['departamento']}")
        else:
            mostrar_resultado("No encontrado", "Empleado no encontrado.")

    def buscar_departamento():
        depto = simpledialog.askstring("Buscar", "Departamento:")
        resultados = buscar_empleados_por_departamento(depto)
        texto = "\n".join([f"{e['nombre']} {e['apellido']}" for e in resultados]) or "No se encontraron empleados."
        mostrar_resultado(f"Empleados de {depto}", texto)

    tk.Button(win, text="Buscar por ID", command=buscar_id, width=30).pack(pady=5)
    tk.Button(win, text="Buscar por departamento", command=buscar_departamento, width=30).pack(pady=5)
    tk.Button(win, text="Cerrar", command=win.destroy, width=30).pack(pady=10)

# ---- Submenú Estadísticas ----
def menu_estadisticas():
    total = obtener_valor_total_inventario()
    mostrar_resultado("Valor total del inventario", f"${total:,.2f}")

# =====================================================
# MENÚ PRINCIPAL
# =====================================================
root = tk.Tk()
root.title("Sistema Integrado - Búsqueda Lineal")
root.geometry("400x350")

tk.Label(root, text="SISTEMA INTEGRADO", font=("Arial", 16, "bold")).pack(pady=10)
tk.Button(root, text="📦 Productos", command=menu_productos, width=30, height=2).pack(pady=5)
tk.Button(root, text="👨‍💼 Empleados", command=menu_empleados, width=30, height=2).pack(pady=5)
tk.Button(root, text="📊 Estadísticas", command=menu_estadisticas, width=30, height=2).pack(pady=5)
tk.Button(root, text="❌ Salir", command=root.destroy, width=30, height=2).pack(pady=10)

root.mainloop()
