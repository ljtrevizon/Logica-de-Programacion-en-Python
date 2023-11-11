cedulas = ["100000","100001","100002","100003"]
nombres = ["Jose","Jose","Maria","Pedro"]
apellidos = ["Rojas","Rodriguez","Martinez","Leon"]

cedula=input("Ingrese la cedula a buscar: ")
posicion=-1

for i in range(len(cedulas)):
    if cedulas[i].upper() == cedula.upper():
        posicion=i
        break

if posicion == -1:
    print("No esta registrada la cedula ",cedula)
else:
    print("Pertenece a:",nombres[posicion],apellidos[posicion])