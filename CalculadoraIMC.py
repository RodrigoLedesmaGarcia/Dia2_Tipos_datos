print("CALCULADORA DE INDCIDE DE MASA CORPORAL")
altura = input("Ingresa tu altura en metros: ")
peso = input("Ingresa tu peso en kilos: ")

imc = int(peso) / float(altura) ** 2
imc_int = int(imc)
print(imc_int)