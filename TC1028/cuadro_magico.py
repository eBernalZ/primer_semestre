# Emilio Bernal, Diego Benitez, Soeun Park, Adrian Maldonado
renglon = 0
columna = 2
matriz = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

for i in range(1,26):
    matriz[renglon][columna] = i
    if (columna == 4 or renglon == -5):
        if (columna == 4 and renglon == -5):
            columna = -1
            renglon = 0
        elif (columna == 4):
            columna = -1
        elif (renglon == -5):
            renglon = 0
        if (matriz[renglon-1][columna+1] == 0):
            renglon -= 1
            columna += 1
        else:
            renglon += 1
    elif (matriz[renglon-1][columna+1] == 0):
        renglon -= 1
        columna += 1
    else:
        renglon += 1

for i in range(len(matriz)):
    print(matriz[i])
