nombre_empleado=input("Introduzca su nombre: ")
salario_base=float(input("Introduzca su sueldo base: "))
ventas_enero=float(input("Introduzca el monto de ventas realizados en Enero: "))
ventas_febrero=float(input("Introduzca el monto de ventas realizado en Febrero: "))
ventas_marzo=float(input("Introduzca el monto de ventas realizado en Marzo: "))
promedio_ventas=(ventas_enero+ventas_febrero+ventas_marzo)/3
ventas_total=(ventas_enero+ventas_febrero+ventas_marzo)
comision=ventas_total*0.15
salario_total=salario_base+comision
print("----------")
print("Recibo:")
print("Nombre: ",nombre_empleado)
print("Salario base: ", salario_base)
print("Promedio de las ventas: ",promedio_ventas)
print("Comision de las ventas: ",comision)
print("Salario total: ",salario_total)
