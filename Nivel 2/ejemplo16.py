while True:
    nombre = input("Introduzca el nombre: ")
    nota = int(input("Introduzca la nota: "))
    if nota>=80:
        print(nombre.upper(),"superaste el desafio")
        if nota==100:
            print("Excelente trabajo")
    else:
        print("Debes recuperar")
    respuesta = input("Desea procesar la nota de otro alumno? (s/n): ")
    if respuesta.upper()=="N":
        break
print("------------")
print("Hasta pronto")