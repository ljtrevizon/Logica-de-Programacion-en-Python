import random

precio = random.randint(2,50)
cantidad = random.randint(1,10)

subTotal = precio*cantidad

if subTotal > 50:
    descuento=subTotal*0.05
else:
    descuento=subTotal*0.02
subTotalDescontado=(subTotal-descuento)
iva=subTotalDescontado*0.16
pago=subTotalDescontado+iva
print(descuento)
print(subTotal)
print(subTotalDescontado)
print(iva)