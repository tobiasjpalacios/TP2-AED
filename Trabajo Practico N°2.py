######## FUNCIONES ########

#Menu principal...
def menu_principal():
    print("1. Definir FORMA DE CARGA \n"
          "2. PROCESAR las pasadas \n"
          "3. Ver RESULTADOS \n"
          "4. Salir \n")
    opcion = int(input("Ingrese la opcion: "))
    while opcion != 1 and opcion != 2 and opcion != 3 and opcion != 4:
        print("Ingrese las opciones disponibles.")
        print("1. Definir FORMA DE CARGA \n"
              "2. PROCESAR las pasadas \n"
              "3. Ver RESULTADOS \n"
              "4. Salir \n")
        opcion = int(input("Ingrese la opcion: "))

    return opcion

#Timer...

######## PROGRAMA ########

opcion = menu_principal()
while opcion != 4:

    if opcion == 1:

        opcion2 = int (input("1 - MANUAL / 2 - AUTOMATICO: "))
        while opcion != 1 and opcion != 2:
            print("Ingrese las opciones disponibles.")
            opcion2 = int(input("1 - MANUAL / 2 - AUTOMATICO: "))

        if opcion2 == 1:
            automatico = False
        else:
            automatico = True

    if opcion == 2:
        if automatico == False:
            print("Funciona")
        else:
            print("Tambien funciona")




    opcion = menu_principal()