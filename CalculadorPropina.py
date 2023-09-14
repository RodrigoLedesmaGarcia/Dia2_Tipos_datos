print("CALCULADORA DE PROPINA")
personas = input("Cuantas personas son en total? ")
cuenta = input("Cuanto es el total a pagar? ")
porcentaje = input("Cuanto es el pocentaje de propina a dar' elm .10 .12 .15 ")

individual = float(cuenta) / float(personas)
propina = (float(cuenta) / float(personas)) * float(porcentaje)

total = float(individual) + float(propina)

print(f"El total a pagar de cada uno es: {total}")
