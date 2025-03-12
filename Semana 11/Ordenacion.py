# ejemplo de busqueda lineal con matriz
matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

valor_a_buscar = 8

for fila in range(len(matriz)):
    for column in range(len(matriz[fila])):
        if matriz[fila][column] == valor_a_buscar:
            print(f"Encuentro la posición ({fila},{column})") #
            break
    else:
        continue # continua al siguiente
    break
else:
    print("valor no encontrado")

