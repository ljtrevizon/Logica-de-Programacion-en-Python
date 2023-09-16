for numero_empleados in range(10):
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
