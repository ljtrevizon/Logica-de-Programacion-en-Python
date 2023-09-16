import random

nota1 = random.randint(0,20)
nota2 = random.randint(0,20)
nota3 = random.randint(0,20)
print("La nota 1: ",nota1)
print("La nota 2: ",nota2)
print("La nota 3: ",nota3)
nota_promedio = (nota1+nota2+nota3)/3
print("La nota promedio es ",nota_promedio)
if nota_promedio >= 10:
    print("Usted aprobo")
if nota_promedio >=18:
    print("Que crack")
if nota_promedio < 10:
    print("Usted reprobo")