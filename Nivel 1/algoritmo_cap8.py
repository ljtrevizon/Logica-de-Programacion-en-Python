# Este codigo ha sido generado por el modulo psexport 20230113-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	m = int()
	p = int()
	n = int()
	q = int()
	r = int()
	z = int()
	print("Coloque el valor de M")
	m = int(input())
	print("El descuento de un 25% de M (",m,") es: ",m-(m*0.25))
	print("Coloque el valor de N")
	n = int(input())
	print("El aumento de un 35% de N (",n,") es: ",n+(n*0.35))
	print("Coloque el valor de P")
	p = int(input())
	print("Coloque el valor de Q")
	q = int(input())
	print("El valor de Q (",q,") menos 25 es: ",q-25)
	print("Coloque el valor de Z")
	z = int(input())
	print("El triple de Z (",z,") es: ",z*3)
	print("Coloque el valor de R")
	r = int(input())
	print("Su promedio es: ",(m+n+q+p+r+z)/6)
	print("El 15% de P (",p,") es: ",p*(15/100))
	print("El promedio de M (",m,"), N (",n,") y Q (",q,") es: ",(m+n+q)/3)
	print("")

