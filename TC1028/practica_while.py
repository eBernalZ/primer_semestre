edad = 0
carrera = "itc"
semestre = "3ro"
nombre = input("Ingresa tu nombre: \n")

while (edad != 20) or (carrera != "itc") or (semestre != "5to"):
    edad = int(input("Ingresa tu edad: \n"))
    carrera = input("Ingresa tu carrera: \n").lower()
    semestre = input("Ingresa tu semestre: \n").lower()
    print("El estudiante es " + nombre)
