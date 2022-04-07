listaDeProductos=[]
opcion=1
while(opcion != 0):
    print("Digite una acción del siguiente menú:")
    print("******")
    print("1. Agregar producto (código, nombre, precio)")
    print("2. Ver productos")
    print("3. Editar producto")
    print("4. Eliminar producto")
    print("0. Digitar 0 para saliro)")
    print("******")
    opcion = int(input("Bienvenido, digita una opcion: "))
    if(opcion == 1):
        producto={}
        #Llenando el diccionario
        producto['codigo']=input("Ingrese el código del producto:")
        producto['nombre']=input("Ingrese el nombre del producto:")
        producto['precio']=input("Ingrese el precio del producto:")
        #Llenando la lista
        listaDeProductos.append(producto)
    elif(opcion == 2):
        print(listaDeProductos)
    elif(opcion == 3):
        estado=True
        codigo=input("Ingrese el código del producto que quiere editar:")
        for producto in listaDeProductos:
            if codigo == producto['codigo']:
                producto['precio']=input("Ingrese el precio del producto:")
                estado=True
                break
            else:
                estado=False
        if(estado==False):
            print("Producto no encontrado")
    elif(opcion == 4):
        estado=True
        codigo=input("Ingrese el código del producto que quiere editar:")
        for producto in listaDeProductos:
            if codigo == producto['codigo']:
                listaDeProductos.remove(producto)
                estado=True
                break
            else:
                estado=False
    else:
        print("En construcción")
