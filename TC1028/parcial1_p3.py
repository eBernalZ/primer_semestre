from turtle import *

# Estrellas
for i in range(5):
    pendown()
    fillcolor("yellow")
    begin_fill()
    for i in range(5):
        forward(75)
        rt(144)
    end_fill()
    penup()
    forward(85)

# Moverse para que no se empalme
goto(-100,-100)

# Cuadrados
for i in range(4):
    pendown()
    fillcolor("blue")
    begin_fill()
    for i in range(4):
        forward(50)
        rt(90)
    end_fill()
    penup()
    forward(85)

# Moverse para que no se empalme
goto(-300,100)

# Triangulos
for i in range(2):
    pendown()
    fillcolor("green")
    begin_fill()
    for i in range(3):
        forward(65)
        lt(360/3)
    end_fill()
    penup()
    forward(80)
done()
