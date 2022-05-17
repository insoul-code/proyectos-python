class Personaje:
    def __init__(self):
        self.__nombre = None
        self.__arma = None
        self.__edad = None

    #Getter    
    @property
    def nombre(self):
        return self.__nombre
    @property
    def arma(self):
        return self.__arma
    @property
    def edad(self):
        return self.__edad

    #Setter
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre
    @arma.setter
    def arma(self,arma):
        self.__arma=arma
    @edad.setter
    def edad(self,edad):
        if(edad<0):
            print('Digite edad valida')
        else:
            self.__edad=edad
