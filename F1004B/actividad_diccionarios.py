# Emilio Bernal A01570751, Maria Santacruz A01284122, Adrian Maldonado A01284189, Jorge Sanchez A00829922
import json
dictionary = {}
loop = True
dep_num = int(input("Cuantos departamentos quieres registrar?\n"))
for i in range(dep_num):
    name = input("\nComo se llama el departamento #%i?\n" %(i+1))
    dictionary[name] = []
    emp_num = int(input("Cuantos empleados hay en %s?\n" %(name)))
    for j in range(emp_num):
        employee = {}
        employee["name"] = input("\nCual es el nombre del empleado #%i?\n" %(j+1))
        employee["age"] = int(input("Cual es la edad de %s?\n" %(employee["name"])))
        employee["years_worked"] = int(input("Cuantos años tiene %s trabajando en la empresa?\n" %(employee["name"])))
        employee["hometown"] = input("En que ciudad nacio %s?\n" %(employee["name"]))
        employee["nationality"] = input("Cual es la ciudadania de %s?\n" %(employee["name"]))
        dictionary[name].append(employee)

while(loop):
    action = input("\n\nQue quieres hacer ahora?\n- EDITAR registro\n- BORRAR registro\n- AGREGAR registro nuevo\n- LEER los registros\n").lower()
    if action == "leer":
        print(json.dumps(dictionary, indent=2))

    elif action == "editar":
        name = input("Como se llama el empleado?\n")
        department = input("A que departamento pertenece %s?\n" %(name))
        for ii in range(len(dictionary[department])):
                if dictionary[department][ii]["name"] == name:
                    print("entro")
                    del dictionary[department][ii]
        print("Complete las siguientes preguntas para cambiar la informacion del empleado por favor:\n")
        employee = {}
        employee["name"] = input("\nCual es el nuevo nombre del empleado?\n")
        employee["age"] = int(input("Cual es la edad de %s?\n" %(employee["name"])))
        employee["years_worked"] = int(input("Cuantos años tiene %s trabajando en la empresa?\n" %(employee["name"])))
        employee["hometown"] = input("En que ciudad nacio %s?\n" %(employee["name"]))
        employee["nationality"] = input("Cual es la ciudadania de %s?\n" %(employee["name"]))

        dictionary[department].append(employee)
        print("\n\n")
        print(json.dumps(dictionary, indent=2))

    elif action == "borrar":
        item = input("Que quieres borrar?\n- DEPARTAMENTO\n- EMPLEADO\n").lower()

        if item == "departamento":
            department = input("Como se llama el departamento?\n")
            del dictionary[department]
            print("\n\n")
            print(json.dumps(dictionary, indent=2))

        elif item == "empleado":
            name = input("Como se llama el empleado?\n")
            department = input("A que departamento pertenece %s?\n" %(name))

            for jj in range(len(dictionary[department])):
                if dictionary[department][jj]["name"] == name:
                    del dictionary[department][jj]
            print("\n\n")
            print(json.dumps(dictionary, indent=2))

    elif action == "agregar":
        item = input("Que quieres agregar?\n- DEPARTAMENTO\n- EMPLEADO\n").lower()

        if item == "departamento":
            name = input("\nComo se llama el nuevo departamento?\n")
            dictionary[name] = []
            emp_num = int(input("Cuantos empleados hay en %s?\n" %(name)))

            for ll in range(emp_num):
                employee = {}
                employee["name"] = input("\nCual es el nombre del empleado #%i?\n" %(ll+1))
                employee["age"] = int(input("Cual es la edad de %s?\n" %(employee["name"])))
                employee["years_worked"] = int(input("Cuantos años tiene %s trabajando en la empresa?\n" %(employee["name"])))
                employee["hometown"] = input("En que ciudad nacio %s?\n" %(employee["name"]))
                employee["nationality"] = input("Cual es la ciudadania de %s?\n" %(employee["name"]))
                dictionary[name].append(employee)
            print("\n\n")
            print(json.dumps(dictionary, indent=2))

        elif item == "empleado":
            emp_num = int(input("Cuantos empleados quieres agregar?\n"))

            for mm in range(emp_num):
                employee = {}
                employee["name"] = input("\nCual es el nombre del empleado #%i?\n" %(mm+1))
                employee["age"] = int(input("Cual es la edad de %s?\n" %(employee["name"])))
                employee["years_worked"] = int(input("Cuantos años tiene %s trabajando en la empresa?\n" %(employee["name"])))
                employee["hometown"] = input("En que ciudad nacio %s?\n" %(employee["name"]))
                employee["nationality"] = input("Cual es la ciudadania de %s?\n" %(employee["name"]))
                department = input("A que departamento pertenece %s?\n" %(employee["name"]))
                dictionary[department].append(employee)
            print("\n\n")
            print(json.dumps(dictionary, indent=2))

    response = input("Quieres seguir haciendo cambios?\n").lower()

    if response == "si":
        loop = True
    elif response == "no":
        loop = False