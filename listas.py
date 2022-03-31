#Listas
valores=[1,2,3,4,5]

#Tupla - con esto se garantiza que los datos son de un lenght especifico
valoresTupla=(1,2,3,4,5)
print(valoresTupla)

'''for valor in valoresTupla:
    print(valor)

print(valoresTupla[0])'''

#Transformemos una tupla en una lista
listaValores=list(valoresTupla)
print(listaValores)
listaValores.append(6)
print(listaValores)
valoresTupla=tuple(listaValores)
print(valoresTupla)

#Ejercicio de clase 1
numeros=(50,45,20,30,40,87)
tuplaLista=list(numeros)
listaNumMayores=[]
for numero in tuplaLista:
    if(numero > 40):
        listaNumMayores.append(numero)
print(listaNumMayores)

#Ejercicio de clase 2
numeros=(50,45,20,30,40,87)
tuplaLista=list(numeros)
listaNumMayores=[]
for numero in tuplaLista:
    if(numero %2 == 0):
        listaNumMayores.append(numero)
print(listaNumMayores)
