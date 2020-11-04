# Escribe un programa en Python que pregunte al usuario un número y 
# determine si este número es un número primo y en caso de que no lo 
# sea que muestre en pantalla los factores de dicho número.
factors = []
number = int(input("Cual numero quieres averiguar si es primo?\n"))

for i in range(2,number):
    if number % i == 0:
        factors.append(i)

if len(factors) > 0:
    print("Los factores del numero %i son: " %(number))
    print(factors)
else:
    print("Este numero es primo")