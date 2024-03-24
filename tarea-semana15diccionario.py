# Crear un diccionario llamado informacion_personal
informacion_personal = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Ciudad A",
    "profesion": "Ingeniero"
}

# Acceder y modificar el valor asociado con la clave "ciudad"
informacion_personal["ciudad"] = "Ciudad B"

# Agregar una nueva clave-valor al diccionario
informacion_personal["profesion"] = "Desarrollador"

# Verificar la existencia de la clave "telefono" y agregarla si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "123456789"

# Eliminar la clave "edad" del diccionario
del informacion_personal["edad"]

# Imprimir el diccionario resultante
print(informacion_personal)
