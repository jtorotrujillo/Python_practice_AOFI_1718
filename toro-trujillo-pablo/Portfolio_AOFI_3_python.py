var_numero1 = 0
var_numero2 = 0
var_numero3 = 0

print ("Dime un numero (mayor que 0)")
var_numero1 = int(input())
if var_numero1 > 0:
	print ("Dime otro numero mayor que el anterior")
	var_numero2 = int(input())
	if var_numero2 > var_numero1:
		print ("Dime el ultimo numero (menor que 0")
		var_numero3 = int(input())
		if var_numero3 < 