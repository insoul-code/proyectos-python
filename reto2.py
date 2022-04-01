'''Crea una función  que reciba una lista con valores numéricos y devuelva el valor máximo y el mínimo ingresados'''

valores=[10,20,30,40,50]
def valoresMaximosMinimos(valores):
    valorMin=min(valores)
    valorMax=max(valores)
    return valorMin,valorMax

print(valoresMaximosMinimos(valores))