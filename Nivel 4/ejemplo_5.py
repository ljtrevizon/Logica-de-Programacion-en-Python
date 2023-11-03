notas = [0,0,0,0,0,0,0,0,0,0]

for i in range(10):
    print("Introduzca la nota ",i+1,":")
    notas[i]=int(input())
print("---------------")
print("Las notas leidas fueron: ")
for nota in notas:
    print(nota)