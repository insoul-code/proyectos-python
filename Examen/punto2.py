'''Leer el nombre de 10 frutas para preparar un salpicón; el programa debe
permitir mostrar las 10 frutas ingresadas al mismo tiempo en sentido
inverso al ingresado'''
conteo=0
frutas = []
while(conteo < 10):
    fruta = input('Ingrese una fruta: ')
    frutas.append(fruta)
    conteo+=1

listaFrutas = list(reversed(frutas))
print(f'La lista de frutas ingresadas es: {frutas}')
print(f'La lista de frutas invertidas es: {listaFrutas}')