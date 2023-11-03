import random
def mostrar_salidas(cliente,sueldo):
    print("El cliente ",cliente," posee el sueldo: ",sueldo)

def leer_entradas():
    nombre=input("Diga su nombre: ")
    sueldo=input("Diga su sueldo: ")
    return nombre,sueldo

n="omar"
s="100"
mostrar_salidas(n,s)
for i in range (3):
    n,s=leer_entradas()
    mostrar_salidas(n,s)

