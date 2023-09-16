# Una compañía decide realizar un ajuste de sueldo a sus 10 empleados,
# para lo cual aplica la siguiente política:
# a.- Si tiene más de 5 años de servicio en la empresa tendrá un aumento del 10%
# del sueldo base.
# b.- Si tiene como mínimo 4 cursos realizados se le otorga un bono de
# mejoramiento de 25 $
# Desarrolle un programa que lea los siguientes datos de un empleado: nombre,
# sueldo base, años de servicio, números de cursos realizados,
# debe imprimir nombre, sueldo base, el monto del aumento y nuevo sueldo
# del empleado
# Ciclo repetir hasta
numero_empleados = 0
while True:

    nombre = input("Nombre: ")
    sueldo_base = int(input("Sueldo base: "))
    servicio = int(input("Ingrese los años de servicio: "))
    cursos = int(input("Cursos realizados: "))
    aumento = 0
    bono = 0
    if servicio >= 5:
        aumento = 10
    if cursos >= 4:
        bono = 25
    monto_aumento = sueldo_base+(sueldo_base*(aumento/100))
    sueldo_final = sueldo_base+bono+monto_aumento
    print("--------------")
    print("Empleado nro", numero_empleados+1)
    print("Nombre: ", nombre.upper())
    print("Sueldo base: ", sueldo_base)
    print("Monto del aumento: ", monto_aumento)
    print("Nuevo sueldo: ", sueldo_final)
    print("--------------")
    numero_empleados += 1
    if numero_empleados == 10:
        break
