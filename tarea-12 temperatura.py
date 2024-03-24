# Crear matriz 3D de temperaturas diarias
temperaturas = [
    [[28, 29, 30, 31, 27, 26, 25], [26, 28, 29, 33, 31, 30, 29]],  # Ciudad 1, Semana 1
    [[24, 22, 21, 25, 26, 27, 23], [20, 23, 24, 26, 27, 28, 25]],  # Ciudad 2, Semana 1
    [[32, 33, 34, 30, 29, 31, 28], [30, 31, 32, 33, 34, 35, 29]],  # Ciudad 1, Semana 2
    [[22, 23, 24, 25, 21, 20, 19], [18, 20, 21, 25, 23, 22, 24]],  # Ciudad 2, Semana 2
]

# Calcular promedio de temperaturas por ciudad y semana
for ciudad_temps in temperaturas:
    for semana_temps in ciudad_temps:
        promedio_semana = sum(semana_temps) / len(semana_temps)
        print(f"Promedio de temperaturas para una ciudad en la semana: {promedio_semana}")
