import random

nombres = []
edades=[15,35,28,40]
dias_semanas = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]


print("El primer dia de la semana es: ",dias_semanas[0])
print("Para algunos el primer dia de la semana es: ",dias_semanas[6])
i = random.randint(-7,-1)
print("El dia en la posicion ",i,"es ",dias_semanas[i])
print("El dia ",i,"es ",dias_semanas[i])