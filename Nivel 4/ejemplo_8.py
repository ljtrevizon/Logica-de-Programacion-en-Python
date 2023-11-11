nombres = ["Jose","Maria","Jorge","Jesus"]
edades = [50,25,16,4]
signos_zodiacales = ["Aries","Capricornio","Sagitario","Piscis"]

def mostrar_arreglos(nombres,edades,signos_zodiacales):
    for i in range(4):
        print("El nombre ",i+1," es ",nombres[i]," y tene la edad ",edades[i]," y su signo zodiacal es ",signos_zodiacales[i])

def leer_arreglos(nombres,edades,signos_zodiacales):
    for i in range(4):
        print("Ingrese el nombre ",i+1,end=": ")
        nombres[i]=input()
        print("Ingrese la edad ",i+1,end=": ")
        edades[i]=int(input())
        print("Ingrese su signo zodiacal ",i+1,end=": ")
        signos_zodiacales[i]=input()

print("------------")
mostrar_arreglos(nombres,edades,signos_zodiacales)
print("------------")
leer_arreglos(nombres,edades,signos_zodiacales)
print("------------")
mostrar_arreglos(nombres,edades,signos_zodiacales)
print("------------")