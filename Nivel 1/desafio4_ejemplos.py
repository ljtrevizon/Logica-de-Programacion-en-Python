# Este codigo ha sido generado por el modulo psexport 20230113-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).

import random
if __name__ == '__main__':
	base_mayor = float()
	base_menor = float()
	area = float()
	altura = float()
	print("Introduzca la base mayor del trapecio")
	base_mayor = float(input())
	print("Introduzca la base menor del trapecio")
	base_menor = float(input())
	print("Introduzca la altura del trapecio")
	altura = float(input())
	suma=base_mayor+base_menor
	area = suma/2*altura
	print("El area del trapecio es: ",area)

print("(--------------------)")
if __name__ == '__main__':
	base_menor = random.randint(10, 50)
	base_mayor = random.randint(base_menor+10, base_menor+50)
	altura = random.randint(base_menor//2, base_menor//2+10)
	print("La base mayor es ",base_mayor)
	print("La base menor es ",base_menor)
	print("La altura es ",altura)
	suma = base_mayor+base_menor
	area = suma/2*altura
	print("El area del trapecio es: ",area)
