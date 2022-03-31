persona={
    'nombre':'Carlos',
    'edad':24,
    'estatura':1.73,
    'intereses':['Futbol','Video Juegos'],
    'esPapa':False
}
print(persona)
print(persona['intereses'])
print(persona.get('estatura'))

persona['carrera']='Ingeniero'
print(persona)