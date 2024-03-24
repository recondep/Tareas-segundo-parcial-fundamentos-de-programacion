def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * porcentaje_descuento / 100
    return descuento

# Llamada 1: solo se proporciona el monto_total
monto_total_1 = 100
descuento_1 = calcular_descuento(monto_total_1)
monto_final_1 = monto_total_1 - descuento_1
print(f"Descuento: {descuento_1}")
print(f"Monto final a pagar: {monto_final_1}")

# Llamada 2: se proporciona tanto el monto_total como el porcentaje_descuento
monto_total_2 = 200
porcentaje_descuento_2 = 20
descuento_2 = calcular_descuento(monto_total_2, porcentaje_descuento_2)
monto_final_2 = monto_total_2 - descuento_2
print(f"Descuento: {descuento_2}")
print(f"Monto final a pagar: {monto_final_2}")
