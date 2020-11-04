from turtle import *
pendown()
speed(10)
shape("turtle")
pencolor("blue")
bgcolor("light blue")

fillcolor("yellow")
begin_fill()
circle(100)
end_fill()
penup()
goto(0,100)

for i in range(12):
	fd(110)
	pendown()
	fd(45)

	penup()
	bk(155)

	lt(30)

penup()
goto(-100,-150)
pendown()

def cuadrado(size,x,y):
	penup()
	goto(x,y)
	pendown()
	fillcolor("red")
	begin_fill()
	for i in range(4):
		fd(size)
		lt(90)
	end_fill()
def triangulo(size,x,y):
	penup()
	goto(x,y)
	pendown()
	for i in range(3):
		forward(size)
		lt(360/3)

def estrella(size):
	pendown()
	for i in range(5):
		forward(size)
		rt(144)

cuadrado(70,-130,-250)
triangulo(70,-130,-180)
cuadrado(40,150,200)
estrella(100)
done()