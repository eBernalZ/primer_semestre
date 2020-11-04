# Escribe un programa en Python que calcule la Velocidad 
# y la altura de un objeto en los primeros 10 segundos 
# de su lanzamiento vertical (hacia arriba)
# El programa debe contener una función que calcule la velocidad 
# y otra función que calcule la altura.
g = -9.81

print("Hola! Bienvenido a la calculadora de velocidad y altura de tiro vertical.")
Vo = int(input("Cual es la velocidad inicial del tiro?\n"))

def height(Vo,t):
    return Vo * t + (0.5)*g*(t**2)
    
def velocity(Vo,t):
    return Vo + g * t

for i in range(11):
    h = height(Vo,i)
    v = velocity(Vo,i)
    print("Tiempo: %i | Altura: %2.2f | Velocidad: %2.2f" %(i,h,v))
    
print("Gracias por tu preferencia, nos vemos pronto!")
