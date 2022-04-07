class Calculadora:
    def  __init__(self,numero1, numero2):
    #Atributos=datos=variables
        self.numero1 = numero1
        self.numero2 = numero2

    def sumar(self):
        return(self.numero1+self.numero2)
    def restar(self):
        return(self.numero1-self.numero2)
    def multiplicar(self):
        return(self.numero1*self.numero2)
    def dividir(self):
        return(self.numero1/self.numero2)