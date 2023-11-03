def leer_entradas():
    n=input("Introduzca el nombre del vendedor: ")
    y=int(input("Introduzca los anyos de servicios: "))
    v=float(input("Introduzca el valor de las ventas: "))
    return n,y,v

def calcular_comision_basica(monto_ventas):
    if monto_ventas < 50000:
        return monto_ventas*0.05
    else:
        if monto_ventas < 100000:
            return monto_ventas*0.07
        else:
            if monto_ventas <1000000:
                return monto_ventas*0.08
            else:
                return monto_ventas*0.1

def comision_x_antiguedad(years):
    if years > 15:
        return 5*(year-15)
    else:
        return 0
def mostrar_salidas(nombre,comision):
    print("El emleado ",nombre.upper()," tendra la comision: ",comision,"$")
while True:
    nombre,year,ventas=leer_entradas()
    comision_basica = round(calcular_comision_basica(ventas),1)
    comision_antiguedad = comision_x_antiguedad(year)
    comision_total = comision_basica + comision_antiguedad
    mostrar_salidas(nombre,comision_total)
    continuar=input("Desea continuar? S/N: ")
    if continuar.upper() == "N":
        break