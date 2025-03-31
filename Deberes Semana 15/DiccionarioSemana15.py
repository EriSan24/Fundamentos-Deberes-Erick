import json  # Importar módulo para impresión formateada

# Paso 1: Crear un Diccionario
informacion_personal = {
    "nombre": "Erick Sánchez",
    "edad": 25,
    "ciudad": "Lago Agrio",
    "profesion": "Ingeniero en Sistemas"
}

# Paso 2: Acceder y Modificar Valores
informacion_personal["ciudad"] = "Lago Agrio"  # Modificar la ciudad

# Paso 3: Verificar Existencia de Claves y Agregar si no existe
informacion_personal.setdefault("telefono", "0978713417")

# Paso 4: Eliminar una Clave
informacion_personal.pop("edad", None)

# Paso 5: Imprimir el Diccionario Final con formato legible
print(json.dumps(informacion_personal, indent=4, ensure_ascii=False))
