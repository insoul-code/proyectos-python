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

#bucle
contador = 0

while(contador<10):
    contador +=1
    print(contador)
else:
    print("Termino el ciclo")


