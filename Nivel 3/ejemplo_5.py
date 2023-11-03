def leer_datos():
    n=int(input("Ingrese el numero: "))
    return n

auxiliar=-100

for i in range (2):
    numero = leer_datos()
    if numero>auxiliar:
        auxiliar=numero
print("El mayor numero es: ",auxiliar)