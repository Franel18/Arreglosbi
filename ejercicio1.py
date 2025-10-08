# Ejercicio 2: Procesar matriz - valores máximo y mínimo

#  dimensiones
filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))

# matriz vacía
matriz = []

#  valores
print("\nIngrese los valores de la matriz:")
for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = int(input(f"Elemento [{i},{j}]: "))
        fila.append(valor)
    matriz.append(fila)

# matriz
print("\nMatriz ingresada:")
for fila in matriz:
    print("\t".join(map(str, fila)))

# valores máximo y mínimo
maximo = matriz[0][0]
minimo = matriz[0][0]
pos_max = (0, 0)
pos_min = (0, 0)

# encontrar máximo y mínimo
for i in range(filas):
    for j in range(columnas):
        if matriz[i][j] > maximo:
            maximo = matriz[i][j]
            pos_max = (i, j)
        if matriz[i][j] < minimo:
            minimo = matriz[i][j]
            pos_min = (i, j)

# resultados
print(f"\nValor máximo: {maximo} en posición {pos_max}")
print(f"Valor mínimo: {minimo} en posición {pos_min}")
