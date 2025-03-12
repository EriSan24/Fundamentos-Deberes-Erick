
# funcion para ordenar una fila de manera ascendente utilizando Bubble Sort

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
def bubble_sort_fila(fila):
    n = len(fila)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]

# Función para mostrar la matriz

def mostrar_fila(fila):
    for fila in fila:
        print(fila)