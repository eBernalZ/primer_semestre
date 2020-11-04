renglones = int(input("Cuantos renglones tienen las matrices?\n"))
columnas = int(input("Cuantas columnas tienen las matrices?\n"))

matrices = []
for i in range(2):
    matrix = []
    for j in range(renglones):
        row = []
        for k in range(columnas):
            value = int(input("Que valor tiene la celda en el renglon %i columna %i de la matriz #%i?\n" %(j+1,k+1, i+1)))
            row.append(value)
        matrix.append(row)
    matrices.append(matrix)

resultant_matrix = []
for i in range(renglones):
    row = []
    for j in range(columnas):
        value = matrices[0][i][j] + matrices[1][i][j]
        row.append(value)
    resultant_matrix.append(row)
print(resultant_matrix)
