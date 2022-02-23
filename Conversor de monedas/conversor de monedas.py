#Se define la función al inicio del código para que después se pueda invocar
def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuántos pesos " + tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")

'''Programa que convierte pesos a dólares'''

#Las comillas dobles repetidas 3 veces nos permiten guardar un string con el formato que nosotros le demos en el editor
menu = """"
Bienvenido al conversor de monedas 💵

1. Pesos mexicanos
2. Pesos colombianos
3. Pesos argentinos

Elige una opción: """

#Recibimos el input del usuario y lo convertimos a enteros
opcion = int(input(menu))

#Se hace el cálculo de pesos a dolares
if opcion == 1:
    conversor('mexicanos',21)
elif opcion == 2:
    conversor('colombianos',3875)
elif opcion == 3:
    conversor('argentinos',65)
else:
    print('Ingresa una opción correcta por favor')

