#Pedir 20 números
contnum = 1
sumatoria = 0

while(contnum <= 5):
    numero = int(input('Ingrese un número: '))
    if(numero < 0):
        sumatoria +=1
    contnum +=1
print(f'Los números negativos fueron: {sumatoria}')