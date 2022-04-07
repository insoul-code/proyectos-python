class Personaje:
  #Constructor de la clase, inicializa los atributos y métodos de mi clase
  def  __init__(self,nombre,color,tipo,poder,patada):
    #Atributos=datos=variables
    self.nombre = nombre
    self.color = color
    self.tipo = tipo
    self.poder = poder
    self.patada = patada
  
  #Métodos=acciones=funciones
  def saludar(self):
    print("¡Hola!")