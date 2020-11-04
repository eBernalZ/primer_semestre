# nombre de comida, calorias, lipidos, proteina, carbohidratos, sodio
import random
food_array = [["Huevo revuelto con jamón,150,16,22,0,1","Huevo revuelto con salchicha,100,19,36,0,9", "Quesadillas de maíz,400,8.2,11.4,52.1,350.4", "Huevo con frijol,560,15.2,19.4,0,6", "Hotcakes,524,22.4,14.8,65.4,1014.10", "Pan dulce,350,14,6.8,50,275", "Sandwich de huevo con queso y jamón,435,7,25,25,750", "Machacado con huevo,250,17,27.1,1.1,571", "Tacos de chicharron,125,67.3,56.8,141.2,2413", "Molletes,600,12.3,6.4,73.8,14.2"], ["Milanesa de pollo empanizada,225,28.5,42,16.5,5", "Calabacitas rellenas,606,45,18,42,45", "Pizza de Domino's,430,9,8,25,520", "Pollo asado,390,6,72,12,1290", "Enchiladas,290,5,11,49,640", "Milanesa de res,314,16.6,24.8,14.7,295", "Chilaquiles,400,22,20,22,630", "Spaghetti,442,2.6,16.2,86.4,2.8", "Pierna de pollo,170,17.6,54.8,13.2,9.7", "Pescado empanizado,232,12,22,17,532"],["Hotdog,200,10.2,40.6,73.1,32.8", "Hamburguesa al carbón,440,60,45,34.1,430.2", "Quesadillas de maíz,400,8.2,11.4,52.1,350.4", "Pizza Italiana,1360,58,72,144,3080", "Torta de Carnitas,500,32.8,29.1,40.2,431.2", "Pan dulce,350,14,6.8,50,275", "Molletes,600,12.3,6.4,73.8,14.2", "Sincronizada,360,6,4,26,428", "Tacos de carne asada,380,6.5,23.1,49.7,353.1", "Huevo con frijol,560,15.2,19.4,0,6"]]
f = open("output.csv", "w")

for i in range(6):
  for j in range(3):
    x = random.randrange(0,10)
    f.write(food_array[j][x]+ "\n,,,,,\n")

