nombre_prof = input("Introduzca el nombre del profesor")
while True:
    print("Introduzca el nombre del alumno")
    nombre_alumn=int()
    for j in range(1,4):
        print("Introduzca la nota")
        nota=float(input())
    resp=int("Desea continuar? S/N: ")
    if resp.upper() == "N":
        break
