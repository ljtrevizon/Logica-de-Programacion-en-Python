import random
# Variables de entrada (modelo_vehiculo, dias).
modelo_vehiculo = input("Ingrese el nombre del modelo del vehiculo: ")
dias = int(input("Ingrese la cantidad de dias: "))
# Variables de salida (costo_diario, monto_total y pago_inicial).
costo_diario = random.randint(25, 50)
monto_total = dias*costo_diario
pago_inicial = monto_total*0.35
print("--------")
print("El costo diario del alquiler es: ", costo_diario, "$")
print("El monto total del alquiler es: ", monto_total, "$")
print("El pago inicial del alquiler es: ", pago_inicial, "$")
