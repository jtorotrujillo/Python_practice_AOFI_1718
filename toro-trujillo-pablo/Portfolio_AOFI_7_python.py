import time
respuesta = 0
sino = "si"
lista =[]



while sino == "si":
	print("Dime una palabra")
	respuesta = input()
	lista.append(respuesta)
	sino = input("quieres añadir mas? si/no")

for i in lista:
	print(i)
	time.sleep (0.65)