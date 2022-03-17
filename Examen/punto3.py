'''-Construir un programa que permita la construcción del siguiente MENU:
1. Digitar 1 para recibir 5 números enteros
2. Digitar 2 para calcular la suma de los números ingresados previamente
3. Digitar 3 para permitir que el usuario agregue un nuevo número a la
lista
4. Digitar 4 para salir'''
opcion = 0
numerosEnteros=[]
while(opcion != 4):
    print("Digite una acción del siguiente menú:")
    print("******")
    print("1. Digitar 1 para recibir 5 números enteros")
    print("2. Digitar 2 para calcular la suma de los números ingresados previamente")
    print("3. Digitar 3 para permitir que el usuario agregue un nuevo número a la lista")
    print("4. Digitar 4 para salir")
    print("******")
    opcion = int(input("Bienvenido, digita una opcion: "))
    if(opcion == 1):
        conteo = 0
        while(conteo < 5):
            numero= int(input("digite un numero: "))
            numerosEnteros.append(numero)
            conteo += 1
    elif(opcion == 2):
        if(numerosEnteros==[]):
            print(f'No hay números en el arreglo, ejecute la opción 1 primero')
        else:
            sumaNumerosEnteros = sum(numerosEnteros)
            print(f'La suma de los números ingresados es: {sumaNumerosEnteros}')
    elif(opcion == 3):
        nuevoNumero= int(input("digite un nuevo número: "))
        numerosEnteros.append(nuevoNumero)
    elif(opcion == 4):
        print(f'Saliendo del programa')
        break
    else:
        print("digita una opcion valida del menú entre 1,2,3 y 4")
else:
    print("saliendo del ciclo")