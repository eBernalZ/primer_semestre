# Este programa calcula el IMc de una persona

calculate_again = True
#Saludar
print("Hola buenos dias!")

# Preguntar y asignar el nombre
nombre = input("Cual es tu nombre?: ")
print("Un gusto en conocerte " + nombre)

while(calculate_again):
    # Pedir datos al usuario (peso y estatura)
    peso = float(input("Ingresa tu peso en Kg: "))
    estatura = float(input("Ingresa tu estatura en metros: "))

    # Calcular el IMC
    imc = peso / (estatura ** 2)

    # Imprimir IMC
    print("Tu IMC es: " + str(imc))

    if imc < 18.5:
        print("Tienes bajo peso necesitas consumir mas calorias e ir al nutriologo")
    elif imc < 24.9:
        print("Tienes peso ideal sigue cuidandote come frutas y verduras y vete por al sombrita")
    else:
        print("Tienes sobrepeso cuida tu alimentacion y consulta al nutriologo")
    
    response = input("Quieres calcular otro IMC? \n")
    if response == "Si":
        calculate_again = True
    elif response == "No":
        calculate_again = False
        
print("Gracias por usar mi calculadora de IMC " + nombre + " hasta pronto")