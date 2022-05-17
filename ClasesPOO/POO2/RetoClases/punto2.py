from Clientes.Cliente import Cliente
from Cuentas.Cuenta import Cuenta
listaDeClientes=[]
listaDeCuentas=[]
opcion=1

while(opcion != 0):
    print("\n")
    print("Digite una acción del siguiente menú:")
    print("******")
    print("1. Agregar cliente")
    print("2. Agregar cuenta")
    print("3. Consultar saldo")
    print("4. Ingresar dinero")
    print("5. Retirar dinero")
    print("6. Listado de clientes")
    print("7. Listado de cuentas")
    print("0. Para salir")
    print("******")
    opcion = int(input("Bienvenido, digita una opcion: "))
    if(opcion == 1):
        clienteObjetos={}
        cliente=Cliente()
        cliente.nombre = clienteObjetos['nombre'] = input("Ingrese el nombre del cliente:")
        cliente.apellido = clienteObjetos['apellido'] = input("Ingrese el apellido del cliente:")
        cliente.cedula = clienteObjetos['cedula'] = input("Ingrese la cédula del cliente:")
        cliente.ciudad = clienteObjetos['ciudad'] = input("Ingrese la ciudad del cliente:")
        listaDeClientes.append(clienteObjetos)
        print("\n Cliente creado exitosamente")
    elif(opcion == 2):
        clienteCuentas={}
        cuenta=Cuenta()
        cuenta.numeroCuenta = clienteCuentas['numeroCuenta'] = input("Ingrese el número de cuenta del cliente:")
        cuenta.saldo = clienteCuentas['saldo'] = input("¿Cuánto dinero desea ingresar?:")
        listaDeCuentas.append(clienteCuentas)
        print("\n Cuenta creada exitosamente")
    elif(opcion == 3):
        estado=True
        cuenta=input("Ingrese el número de la cuenta:")
        for cuentas in clienteCuentas:
            if cuenta == clienteCuentas['numeroCuenta']:
                print("\n El saldo es: $"+clienteCuentas['saldo'])
                estado=True
                break
            else:
                estado=False
    elif(opcion == 4):
        estado=True
        cuenta=input("Ingrese el número de la cuenta:")
        for cuentas in clienteCuentas:
            if cuenta == clienteCuentas['numeroCuenta']:
                ingresoDinero = int(input("¿Cuánto dinero desea ingresar?:"))
                nuevoSaldo = ingresoDinero + int(clienteCuentas['saldo'])
                clienteCuentas['saldo']=nuevoSaldo
                print("\n Saldo agregado con éxito")
                estado=True
                break
            else:
                estado=False
    elif(opcion == 5):
        estado=True
        cuenta=input("Ingrese el número de la cuenta:")
        for cuentas in clienteCuentas:
            if cuenta == clienteCuentas['numeroCuenta']:
                retiroDinero = int(input("¿Cuánto dinero desea retirar?:"))
                nuevoSaldo = int(clienteCuentas['saldo']) - retiroDinero
                clienteCuentas['saldo']=nuevoSaldo
                print("\n Saldo retirado con éxito")
                estado=True
                break
            else:
                estado=False
    elif(opcion == 6):
        print(listaDeClientes)
    elif(opcion == 7):
        print(listaDeCuentas)
    else:
        print("En construcción")