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
    pesos = input("¿Cuántos pesos mexicanos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 21
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")
elif opcion == 2:
    pesos = input("¿Cuántos pesos colombianos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 3931
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")
elif opcion == 3:
    pesos = input("¿Cuántos pesos argentinos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 106
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")
else:
    print('Ingresa una opción correcta por favor')

