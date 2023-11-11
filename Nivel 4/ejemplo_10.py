cedulas = ["12345678","9101112","13141516","17181920"]
nombres = ["Jose","Jose","Maria","Pedro"]

nombreBuscado=input("Ingrese el nombre que busca: ")
cont=0

for i in range(len(nombres)):
    if nombres[i].upper() == nombreBuscado.upper():
        cont = cont+1

print("Hay ",cont," coincidencias")