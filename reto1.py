'''El valle de aburra afronta altas temperaturas año tras año, Cree una función que permita calcular la temperatura media de la tierra partir de recibir 20 datos diarios de temperatura.'''

temperaturas=[10,50,70,60,57]
def temperaturaMedia(temperaturas):
    tmedia=(min(temperaturas)+max(temperaturas)/2)
    return tmedia

print(temperaturaMedia(temperaturas))
