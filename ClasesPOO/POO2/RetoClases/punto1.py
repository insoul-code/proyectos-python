from Ciclistas.Ciclista import Ciclista 
listaDeCiclistas=[]
opcion=1

while(opcion != 0):
    print("Digite una acción del siguiente menú:")
    print("******")
    print("1. Agregar ciclistas")
    print("2. Listado ciclistas")
    print("3. Mejor tiempo")
    print("0. Para salir")
    opcion = int(input("Bienvenido, digita una opcion: "))
    if(opcion == 1):
        ciclistaObjetos={}
        ciclista=Ciclista()
        ciclista.id = ciclistaObjetos['id'] = input("Ingrese el id del ciclista:")
        ciclista.nombre = ciclistaObjetos['nombre'] = input("Ingrese el nombre del ciclista:")
        ciclista.edad = ciclistaObjetos['edad'] =input("Ingrese la edad del ciclista:")
        ciclista.pais= ciclistaObjetos['pais'] = input("Ingrese el pais del ciclista:")
        ciclista.tiempo= ciclistaObjetos['tiempo'] = input("Ingrese el tiempo del ciclista:")
        listaDeCiclistas.append(ciclistaObjetos)
    elif(opcion == 2):
        print(listaDeCiclistas)
    elif(opcion == 3):
        listaTiempos=[]
        for ciclista in listaDeCiclistas:
            minTime=0
            if(minTime==0):
                minTime=int(ciclista['tiempo'])
            else:
                minTime=ciclista['tiempo']

        print(minTime,ciclista)
    else:
        print("En construcción")

