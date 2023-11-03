
# Una compa��a dedicada al alquiler de veh�culos necesita un sistema para mostrar a sus clientes un recibo por contrato del servicio de alquiler.

nombre = str()
modelo_vehiculo = str()
dias_alquiler = int()
costo_diario = float()
monto_total = float()
pago_inicial = float()
cuotas_diarias = float()

def leer_entradas():
    global nombre
    global modelo_vehiculo
    global dias_alquiler
    global costo_diario
    print(" ingrese su nombre: ", end="")
    nombre = input()
    print(" ingrese el modelo del vehiculo: ", end="")
    modelo_vehiculo = input()
    print(" ingrese los dias de alquiler: ", end="")
    dias_alquiler = int(input())
    print("ingrese el monto diario por el vehiculo: ")
    costo_diario = float(input())

def calcular_monto():
    global costo_diario
    global monto_total
    global dias_alquiler
    global pago_inicial
    global cuotas_diarias
    monto_total = costo_diario*dias_alquiler
    pago_inicial = monto_total*0.35
    cuotas_diarias = (monto_total-pago_inicial)/dias_alquiler

def mostrar_salidas():
    global nombre
    global modelo_vehiculo
    global costo_diario
    global dias_alquiler
    global monto_total
    global pago_inicial
    global cuotas_diarias
    print(" su recibo de pago es: ")
    print(" nombre: ",nombre)
    print(" modelo del vehiculo: ",modelo_vehiculo)
    print(" costo diario de alquiler del vehiculo: ",costo_diario)
    print(" Dias de alquiler: ",dias_alquiler)
    print(" monto total por el servicio de alquiler del vehiculo ",monto_total)
    print(" pago inicial: ",pago_inicial)
    print(" cuotas diarias a cancelar: ",cuotas_diarias)




leer_entradas()

calcular_monto()

mostrar_salidas()