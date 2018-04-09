var_numero = 0
var_sino = "Si"


print("¿Vamos a multiplicar?")
var_sino = input ("Si/No")
while var_sino == "Si":
	print("Dime un numero y yo te diré su tabla de multiplicar")
	var_numero = int(input())
	for i in range (11):
		print(var_numero, "*", i, "=", var_numero*i)
	print("¿Quieres volver a jugar?")
	var_sino = input("Si/No")
else:
	print("Hasta, luego")