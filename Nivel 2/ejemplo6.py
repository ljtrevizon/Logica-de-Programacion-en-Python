import random

n=random.randint(-9999999999999,9999999999999)

print("El numero es: ",n)
print("-----------------")

if n>0:
    print("Es positivo")
else:
    if n<0:
        print("Es negativo")
    else:
        print("Es 0")