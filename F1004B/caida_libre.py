# Calcular velocidad y posicion en Y al momento
g = 9.81

for time in range(11):
    v = g * time
    y = 0 - (0.5 * g * (time**2))
    print("Time: %2.0f s | Velocity: %3.2f m/s | Position: %3.2f" %(time,v,y))