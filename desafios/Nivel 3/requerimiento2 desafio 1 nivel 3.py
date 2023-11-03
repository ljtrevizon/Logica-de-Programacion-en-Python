# Un alumno se considera aprobado cuando obtiene una nota mayor o igual a 48 pts

for i in range(1,10):
	print("ingrese la nota")
	nota = int(input())
	if nota < 48:
		print("usted esta reprobado ")
	else:
		print("usted esta aprobado ")
		if nota >= 85:
			print("usted saco A")
		else:
			if nota>=75:
				print("usted saco B")
			else:
				if nota>=65:
					print("usted saco C")
				else:
					if nota>=55:
						print("usted saco D")
					else:
						print("usted saco E")

