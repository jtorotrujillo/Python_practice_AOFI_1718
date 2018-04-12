var_numero = 0
import time

print ("Dime un numero para la cuenta atras del lanzamiento")
var_numero = int(input())
for i in range (1, var_numero+1):
    time.sleep (1)
    print (var_numero-i)

print ("¡DESPEGE")