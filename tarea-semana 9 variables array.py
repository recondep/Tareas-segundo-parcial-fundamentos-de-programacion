def buscar_valor(matriz, valor):
  for i in range(len(matriz)):
      for j in range(len(matriz[i])):
          if matriz[i][j] == valor:
              return f"El valor {valor} se encontró en la posición ({i}, {j}) de la matriz."
  return f"El valor {valor} no se encontró en la matriz."


# Ejemplo de uso
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
valor_buscado = 5
resultado = buscar_valor(matriz, valor_buscado)
print(resultado)
def ordenar_fila(matriz, fila):
    matriz[fila] = sorted(matriz[fila])


# Ejemplo de uso
matriz = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
fila_a_ordenar = 1
print("Matriz original:")
for fila in matriz:
    print(fila)

ordenar_fila(matriz, fila_a_ordenar)

print("Matriz con la fila ordenada:")
for fila in matriz:
    print(fila)
