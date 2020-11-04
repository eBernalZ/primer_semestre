#Leo García A00830831
#Samuel Fernández A01284436
#Marycela González A01197745
#Emilio Bernal A01570751

listaAlumnos = open('ListaAlumnos.txt' , 'a')

matricula = input('Ingresa tu Matricula:  ')
nombre = input('Ingresa tu Nombre:  ')
edad = input ('Ingresa tu edad:  ')
carrera = input ('Ingresa tu carrera  ')
procedencia = input('Ingresa tu procedencia:  ')

listaAlumnos.write (matricula.ljust (10))
listaAlumnos.write (nombre.ljust (25))
listaAlumnos.write (edad.ljust (2) + " ")
listaAlumnos.write (carrera.ljust (3) + " ")
listaAlumnos.write (procedencia.ljust (30))
listaAlumnos.write ('\n')

listaAlumnos.close()

ListaAlumnos = open('ListaAlumnos.txt' , 'r')
contenido = ListaAlumnos.read()
print (contenido)
ListaAlumnos.close ()
