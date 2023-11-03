import random

def calcularIVA(precio):
    return precio*0.16
for i in range(10):
    subtotal=random.randint(1,50)
    iva=calcularIVA(subtotal)

    print("El iva es de: ",iva)
    p=subtotal+iva
    
    print("El precio es: ",p)
    print("------------")