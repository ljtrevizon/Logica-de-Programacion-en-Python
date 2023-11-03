# Una agencia de carros paga a su personal de ventas 
	# un salario base de 500.000 Bs. m�s una comisi�n de 200.000 Bs. 
	# por cada autom�vil vendido, m�s el 10% del valor total de 
	# las ventas. Si se tiene como entrada el nombre del vendedor, 
	# el n�mero de autos vendidos y el valor total de sus ventas. 
	# Se pide calcular e imprimir el sueldo que debe percibir 
	# el vendedor.
	# variables de entrada

valor_ventas = float()
nro_autos_vendidos = int()
nombre_vendedor = str()
# variables de salida
sueldo_final = float()
# variables de proceso
comision_x_ventas = float()
comision_x_autos_vend = float()
def leer_entradas():
    global nombre_vendedor
    global nro_autos_vendidos
    global valor_ventas
    print("Introduzca el nombre del vendedor:", end="")
    nombre_vendedor = input()
    print("introduzca el número de autos vendidos:", end="")
    nro_autos_vendidos = int(input())
    print("Introduzca el valor de las ventas en $:", end="")
    valor_ventas = float(input())

def mostrar_encabezado():
    print("############################################")
    print("###### Sistema de control de salarios ######")
    print("############################################")
    print("")

def calcular_salario():
    global nro_autos_vendidos
    global sueldo_final
    comision_x_autos_vend = 200*nro_autos_vendidos
    comision_x_ventas = valor_ventas*0.10
    sueldo_final = 500+comision_x_autos_vend+comision_x_ventas
def mostrar_salidas():
    global nombre_vendedor
    global sueldo_final
    print("")
    print("##############################################")
    print("El sueldo final del vendedor ",nombre_vendedor.upper(), end="")
    print(" es ",sueldo_final,"$")
    print("##############################################")
mostrar_encabezado()
# leer las entradas
leer_entradas()
# proceso
calcular_salario()
# mostrar salidas
mostrar_salidas()