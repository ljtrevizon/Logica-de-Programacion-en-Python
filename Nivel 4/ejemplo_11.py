cedulas = ["100000","100001","100002","100003"]
nombres = ["Jose","Jose","Maria","Pedro"]

cedula=input("Ingrese la cedula a buscar: ")
encontrado=False

for i in range(len(cedulas)):
    if cedulas[i].upper() == cedula.upper():
        encontrado=True
        break

if encontrado:
    print("Se encontro el elemento buscado")
else:
    print("No se encontro el elemento buscado")