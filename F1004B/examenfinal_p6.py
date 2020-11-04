def calc(weight, height):
    imc = weight / (height ** 2)
    return imc

output = open("Pacientes.txt", "w")

n = int(input("Cuantos pacientes quieres registar?\n"))

for i in range(n):
    name = input("Ingresa el nombre del paciente #%i:\n" %(i+1))
    age = int(input("Ingresa su edad:\n"))
    weight = float(input("Ingresa su peso:\n"))
    height = float(input("Ingresa su estatura en metros:\n"))
    imc = calc(weight, height)
    patient = "Nombre: %s, Edad: %i, Peso: %3.2f, Estatura: %3.2f, IMC: %3.2f\n" %(name, age, weight, height, imc)
    output.write(patient)
    patient = ""

output.close()

output_file = open("Pacientes.txt", "r")
content = output_file.read()
print(content)