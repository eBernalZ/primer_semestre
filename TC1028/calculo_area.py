# Soeun Park, Rebeca Sanchez, Emiliano Medina, Fernanda de los Angeles
import math
process_repeat = True
print("Hola bienvenido a la aplicacion de calcular areas")
nombre = input("Cual es tu nombre? \n")
print("Gusto en conocerte " + nombre)
print("Las figuras que puedes calcular son: \nCuadrado\nRectangulo\nTriangulo\nCirculo\n")

while process_repeat:  
    figura = input("Que figura quieres calcular?\n").lower()

    if figura == "cuadrado":
        lado = float(input("Cual es el valor del lado del cuadrado?\n"))
        print("El area del cuadrado es " + str(lado ** 2))

    elif figura == "rectangulo":
        largo = float(input("Cual es el valor del largo del rectangulo?\n"))
        ancho = float(input("Cual es el valor del ancho del rectangulo?\n"))
        print("El area del rectangulo es " + str(largo * ancho))

    elif figura == "triangulo":
        base = float(input("Cual es el valor de la base del triangulo?\n"))
        altura = float(input("Cual es el valor de la altura del triangulo?\n"))
        print("El area del triangulo es " + str((base * altura)/2))

    elif figura == "circulo":
        radio = float(input("Cual es el valor del radio del circulo?\n"))
        print("El area del circulo es " + str(math.pi * (radio ** 2)))

    response = input("Quieres calcular otra area? (Si/No)\n").lower()

    if response == "si":
        process_repeat = True
    else:
        process_repeat = False
