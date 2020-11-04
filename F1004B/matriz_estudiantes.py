# Equipo: Rebeca Sanchez A00832498, Alexa de Leon A01382990, Maximiliano Armendariz A00830733, Emilio Bernal A01570751, Adrian Maldonado A01284189
#Este programa ingresa los datos personales de alumnos

#Preguntar cuantos alumnos desea ingresar

n = int(input('Ingresa el número de alumnos: '))
        
#Creamos la lista de alumnos vacía
        
Alumnos = []
        
#Pedimos los datos del alumno
        
for i in range(n): #i va a tomar los valores desde 0 hasta n-1

        #Mostramos separador de dato
        print('\n\n====== Ingresa los datos del alumno =====')
        
        Alumnos.append([]) #Agregamos un renglon vacio a la matriz
        
        #Pedir datos personales al alumno
        matricula = input('Matricula: ')
        nombre = input('Nombre: ')
        carrera = input('Carrera: ')
        edad = input('Edad: ')
        nummaterias = input('Numero de materias cursadas: ')

        materias = []
        for j in range (int(nummaterias)):
            materia = input('Ingrese nombre de materia')
            materias.append(materia)

        #Agregamos los elementos a la lista
        Alumnos[i].append(matricula)
        Alumnos[i].append(nombre)
        Alumnos[i].append(carrera)
        Alumnos[i].append(edad)
        Alumnos[i].append(materias)
        
#Mostrar la matriz de alumnos renglon por renglon
print('\n == Matriz Alumnos == ')
for i in range(len(Alumnos)):
    print(Alumnos[i])
        