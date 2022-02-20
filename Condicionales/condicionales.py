'''Ejercicio introductorio a los condicionales'''

from ast import If


edad = int(input("Escribe tu edad: "))
if edad > 17:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
    #También se puede agregar la función "pass" que se ejecutaría como una función vacía que después modificaríamos
    pass

numero = int(input("Escribe un número: "))

if numero > 5:
    print("Es mayor a 5")
elif numero == 5:
    print("Es igual a 5")
else:
    print("Es menos a 5")