''' 
#Comentario de línea
""" Comentario
de bloque """

#salida por consola
print("Hola mundo python, Gonorrea ome ⇩")

#variables
nombre = "Thiago"
edad = 28
estatura = 1.75
eshinchaVerde = False

print("Buenos días",nombre)

print(f'Buenos días {nombre} sabemos que tienes {edad} años, tu estatura es {estatura}')

#Recibiendo datos desde la consola

num1 = int(input("Ingrese un número entero: "))
num2 = int(input("Ingrese un número entero: "))
resultado = num1+ num2
print(f'La suma de los dos número es: {resultado}')
'''

#Tomando decisiones
'''
numero = int(input("Ingrese un número:"))
print(f'El número ingresado es: {numero}')

if(numero >= 0):
    print("El número es positivo")
else:
    print("El número es negativo")
'''

'''
#Hidroituango
nivelAgua = int(input("Digite el nivel de agua: "))
if(nivelAgua < 200):
    print("Hay muy poca agua en la represa")
elif(nivelAgua >= 200 and nivelAgua < 450):
    print("El nivel de agua es el adecuado")
else:
    print("Hay mucha agua, por favor abra las compuertas")
'''

'''
#Estaciones

mes = input("Digite cualquier mes: ")

if(mes == "enero" or mes == "febrero" or mes == "marzo"):
    print("Está en invierno")
elif(mes == "abril" or mes == "mayo" or mes == "junio"):
    print("Está en verano")
elif(mes == "julio" or mes == "agosto" or mes == "septiembre"):
    print("Está en otoño")
elif(mes == "octubre" or mes == "noviembre" or mes == "diciembre"):
    print("Está en primavera")
else:
    print("Ingresa un mes valido")
'''

'''#bucle
contador = 0

while(contador<10):
    contador +=1
    print(contador)
else:
    print("Termino el ciclo")'''

#menu de opciones
import math

menuOp = 0

while(menuOp != 5):
    print('\nBienvenido al menú de opciones selecciona una opción: \n1.Encontrar multiplo de 2\n2.Encontrar la raíz cuadrada\n3.Sumar +100\n4.Elevar a la 2\n5.Salir') #Muestra las opciones
    menuOp = int(input('Ingresa una opcion: ')) # Usuario ingresa opcion

    if menuOp == 1:
        numero=int(input('Digite un número entero: '))
        if(numero %2 == 0):
            print(f'El número {numero} es mulriplo de 2')
        else:
            print(f'El número {numero} no es multiplo de 2')
    elif menuOp == 2:
        numero = int(input('Ingresa un número para conocer la raíz: '))
        print(f'La raíz cuadrada del {numero} es: {math.sqrt(numero)}')
    elif menuOp == 3:
        numero = int(input('Ingrese el número que quiera para sumarle 100: '))
        print(f'El número {numero} sumado con 100 es: {numero+100}')
    elif menuOp == 4:
        numero = int(input('Ingrese un número para elevar a la 2: '))
        print(f'La potencia del número {numero} es: {numero*numero}')
    elif menuOp == 5:
        print('Salio...')
    else:
        print('¡Ingrese una opcion valida!')




