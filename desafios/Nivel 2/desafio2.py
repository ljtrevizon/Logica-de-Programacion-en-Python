import random
# Variables de entrada (modelo_vehiculo, cantidad_dias).
# Variables de salida (costo_diario, monto_total y pago_inicial).
modelo_vehiculo = input("Ingrese el nombre del modelo del vehiculo: ")
cantidad_dias = int(input("Ingrese la cantidad de dias: "))
costo_diario = random.randint(25, 50)
if cantidad_dias > 30:
    print("No puedes alquilar el vehiculo por tantos dias")
else:
    monto_total = cantidad_dias*costo_diario
    pago_inicial = monto_total*0.35
    deposito = 0
    descuento = 0
    if cantidad_dias > 10:
        print("-------------")
        print("Son muchos dias, debido a esto debe pagar un deposito de 100$")
        deposito=100
    else:
        if cantidad_dias < 5:
            print("-------------")
            print("Son pocos dias, se le va otorgar un descuento del 10%")
            descuento=pago_inicial*0.10
    pago_inicial = pago_inicial+deposito-descuento
    print("-------------")
    print("El costo diario del alquiler es: ", costo_diario, "$")
    print("El monto total del alquiler es: ", monto_total, "$")
    print("El pago inicial del alquiler es: ", pago_inicial, "$")
