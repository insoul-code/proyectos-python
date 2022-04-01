'''-Crear una subrutina llamada “Login”, que recibe un nombre de usuario y una contraseña y te devuelve Verdadero si el nombre de usuario es “admin” y la contraseña es “admin123*”. Además recibe el número de intentos que se ha intentado hacer login y si no se ha podido hacer login incremente este valor.'''

def login(usuario="",contra=""):
    intentos=0
    while(intentos < 4):
        usuario=input("Ingrese el usuario:")
        contra=input("Ingrese la contraseña:")
        if(usuario=='admin' and contra=='admin123'):
            print("Verdadero")
        else:
            print("Falso")
        intentos += 1

login()

