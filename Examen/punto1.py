'''Construir un programa que permita ingresar N (cantidad digitada por el
usuario) números enteros y cuente cuantos múltiplos de 2 y de 3 fueron
ingresados'''

conteo = 0
cantidadNumeros = int(input('Ingrese la cantidad de números a procesar: '))
conteoMultiplos2 = 0
conteoMultiplos3 = 0
while(conteo < cantidadNumeros):
    numero = int(input('Ingrese un número entero: '))
    if(numero %2 == 0 and numero%3 ==0):
        conteoMultiplos2 += 1
        conteoMultiplos3 += 1
    elif(numero %3 == 0):
        conteoMultiplos3 += 1
    elif(numero %2 == 0):
        conteoMultiplos2 += 1
    conteo+=1
print(f'La cantidad de los números ingresados multiplos de 2 es: {conteoMultiplos2}')
print(f'La cantidad de los números ingresados multiplos de 3 es: {conteoMultiplos3}')
