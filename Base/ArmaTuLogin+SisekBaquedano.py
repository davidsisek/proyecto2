
#Primera entrega David Germán Sisek Baquedano
#Comision 85000

datos=  {
    
}

opt=0
def ingreso_info():

    while True:
        usuario = input("Ingrese el nombre de usuario: ")

        if usuario in datos:
            print("--------¡Error! El usuario ya existe vuelva a intentarlo------------")
        else:
            contraseña =input("Ingrese la constraseña de usuario: ")
            datos[usuario] = { "usuario": usuario, "contraseña": contraseña }
            break
def mostrar_info():
    if not datos:
        print("-------------No hay información almadenada todavia----------")
    else:
        for nombre, sub_dic in datos.items():
            nom = sub_dic["usuario"]
            clave = sub_dic["contraseña"] 
            print(f"USUARIO: {nom} ------ CONTRASEÑA: {clave}")

def login():
    print("Bienvenido al Login")
    print("Cada vez que finalice de escribir, presionar ENTER para continuar")
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña =input("Ingrese su contraseña de usuario: ")

    if usuario in datos:
        if contraseña == datos[usuario]["contraseña"]:
            print("----------Acceso autorizado------------\n\n")    
        else:
            print("----------Contraseña Incorrecta---------\n\n")
    else:
        print("----------El usuario no existe----------\n\n")
    

while True:
    print("------------Menú de opciones--------")
    print("Opcion 1: Cargar usuarios")
    print("Opcion 2: Login")
    print("Opcion 3: Ver base de datos completa")
    print("Opcion 4: Salir del menú")
    print("--------------------------------------")

    try:
        opt = int(input("Ingrese la opcion que desee: "))
    except ValueError:
        print("¡ERROR! Solo se permiten números enteros. Intenta de nuevo.")
        continue

    if opt==1:
        ingreso_info()
        continue
    elif opt==2:
        login()
        continue
    elif opt==3:
        mostrar_info()
        continue
    elif opt==4:
        print("Saliendo del programa")
        break
    else:
        print("La opcion no existe")
        continue
        
