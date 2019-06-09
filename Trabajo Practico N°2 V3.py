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

def validacion_patente(patente):
    letras= False
    numeros= False
    index= 0
    for i in patente:
        if len(patente)==7:
            if  2<= index<=4   and "A"<= i <= "z" :
                numeros = False
            else:
                if  0 <= index <=1 or 5 <= index <=6  and "A"<= i <= "Z"  :
                    letras = True
                elif  2 <= index <= 4  and 0 <= int(i) <= 9 :
                    numeros= True
                else:
                    pass
        if len(patente)==6:
            if 0<= index <=2 and "A" <= i<= "Z":
                letras = True
            elif 3 <= index <=6 and "0" <= i <= "9":
                numeros= True
            else:
                pass

        index = index+1
    if letras == True and numeros == True:
        patente = True
    else:
        patente= False
    return patente



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

    elif opcion == 2:

        # TIMER CON  ---> CARGA MANUAL <---

        if automatico == False:

            import time
            import random

            inicio = time.time()
            ahora = inicio
            fin = inicio + 240

            total_recaudado = 0
            tipo1 = 0
            recaudado_tipo1 = 0
            tipo2 = 0
            recaudado_tipo2 = 0
            tipo3 = 0
            recaudado_tipo3 = 0
            c_efectivo = 0
            recaudado_efectivo = 0
            c_telepeaje = 0
            recaudado_telepeaje = 0
            mayor_tipo = 0

            moto = 20
            auto = 40
            camion = 80
            bandera = None

            c_hora1 = 0
            recaudado_hora1 = 0
            c_hora2 = 0
            recaudado_hora2 = 0
            c_hora3 = 0
            recaudado_hora3 = 0
            c_hora4 = 0
            recaudado_hora4 = 0

            a = False

            while (ahora < fin):

                retraso = random.randint(1, 15)  # La idea es que un vehiculo arribe al peaje entre 9 a 15 minutos
                actual = int(ahora - inicio)
                if actual > 180:
                    hora = 4
                    print("Hora 4 Minuto", actual)
                elif actual > 120:
                    hora = 3
                    print("Hora 3 Minuto", actual)
                elif actual > 60:
                    hora = 2
                    print("Hora 2 Minuto", actual)
                else:
                    hora = 1
                    print("Hora 1 Minuto", actual)

                # Carga de datos: TIPO DE VEHICULO
                tipo = int(input("1. Moto / 2. Auto / 3. Camion : "))
                while tipo != 1 and tipo != 2 and tipo != 3:
                    print("Ingrese las opciones disponibles.")
                    tipo = int(input("1. Moto / 2. Auto / 3. Camion : "))

                # Carga de datos: FORMA DE PAGO
                forma_pago = int(input("1. Efectivo / 2. Telepeaje : "))
                while forma_pago != 1 and forma_pago != 2:
                    print("Ingrese las opciones disponibles.")
                    forma_pago = int(input("1. Efectivo / 2. Telepeaje : "))

                # Efectivo...
                if forma_pago == 1 and tipo == 1:
                    bandera = moto
                    c_efectivo += 1
                    total_recaudado += moto
                    tipo1 += 1
                    recaudado_tipo1 += moto
                    recaudado_efectivo += moto

                elif forma_pago == 1 and tipo == 2:
                    bandera = auto
                    c_efectivo += 1
                    total_recaudado += auto
                    tipo2 += 1
                    recaudado_tipo2 += auto
                    recaudado_efectivo += auto

                elif forma_pago == 1 and tipo == 3:
                    bandera = camion
                    c_efectivo += 1
                    total_recaudado += camion
                    tipo3 += 1
                    recaudado_tipo3 += camion
                    recaudado_efectivo += camion
                # Telepeaje...
                #VALIDACION!!!!!!!!!!!!
                patente =  (input('Ingrese la patente de su vehiculo '))

                a == validacion_patente(patente)

                while a == False:
                    print('Ingrese una patente valida')
                    patente =  input('Ingrese la patente de su vehiculo ')
                else:
                    if forma_pago == 2 and tipo == 1:
                        bandera = moto
                        c_telepeaje += 1
                        total_recaudado += moto
                        tipo1 += 1
                        recaudado_tipo1 += moto
                        recaudado_telepeaje += moto
                    elif forma_pago == 2 and tipo == 2:
                        bandera = auto
                        c_telepeaje += 1
                        total_recaudado += auto
                        tipo2 += 1
                        recaudado_tipo2 += auto
                        recaudado_telepeaje += auto
                    elif forma_pago == 2 and tipo == 3:
                        bandera = camion
                        c_telepeaje += 1
                        total_recaudado += camion
                        tipo3 += 1
                        recaudado_tipo3 += camion
                        recaudado_telepeaje += camion

                # CHEQUEO DE HORA DE TURNO

                if actual > 180:
                    c_hora4 += 1
                    recaudado_hora4 += bandera
                elif actual > 120:
                    c_hora3 += 1
                    recaudado_hora3 += bandera
                elif actual > 60:
                    c_hora2 += 1
                    recaudado_hora2 += bandera
                else:
                    c_hora1 += 1
                    recaudado_hora1 += bandera

                if c_hora1 > c_hora2 and c_hora1 > c_hora3 and c_hora1 > c_hora4:
                    hora_pico = "1° HORA"
                elif c_hora2 > c_hora3 and c_hora2 > c_hora4:
                    hora_pico = "2° HORA"
                elif c_hora3 > c_hora4:
                    hora_pico = "3° HORA"
                else:
                    hora_pico = "4° HORA"


                time.sleep(retraso)
                ahora = time.time()


        # TIMER CON CARGA ---> AUTMATICA <---
        else:
            import time
            import random

            inicio = time.time()
            ahora = inicio
            fin = inicio + 240

            total_recaudado = 0
            tipo1 = 0
            recaudado_tipo1 = 0
            tipo2 = 0
            recaudado_tipo2 = 0
            tipo3 = 0
            recaudado_tipo3 = 0
            c_efectivo = 0
            recaudado_efectivo = 0
            c_telepeaje = 0
            recaudado_telepeaje = 0
            mayor_tipo= 0


            moto = 20
            auto = 40
            camion = 80
            bandera = None

            c_hora1 = 0
            recaudado_hora1 = 0
            c_hora2 = 0
            recaudado_hora2 = 0
            c_hora3 = 0
            recaudado_hora3 = 0
            c_hora4 = 0
            recaudado_hora4 = 0

            while (ahora < fin):

                retraso = random.randint(1, 15)  # La idea es que un vehiculo arribe al peaje entre 9 a 15 minutos
                actual = int(ahora - inicio)
                if actual > 180:
                    hora = 4
                    print("Hora 4 Minuto", actual)
                elif actual > 120:
                    hora = 3
                    print("Hora 3 Minuto", actual)
                elif actual > 60:
                    hora = 2
                    print("Hora 2 Minuto", actual)
                else:
                    hora = 1
                    print("Hora 1 Minuto", actual)

                # Generacion de Datos : TIPO DE VEHICULO y FORMA DE PAGO
                tipo = random.randint(1,3)
                forma_pago = random.randint(1,2)

                # Efectivo...
                if forma_pago == 1 and tipo == 1:
                    print("Tipo: MOTO - Forma de Pago: Efectivo ")
                    bandera = moto
                    c_efectivo += 1
                    total_recaudado += moto
                    tipo1 += 1
                    recaudado_tipo1 += moto
                    recaudado_efectivo += moto

                elif forma_pago == 1 and tipo == 2:
                    print("Tipo: AUTO - Forma de Pago: Efectivo ")
                    bandera = auto
                    c_efectivo += 1
                    total_recaudado += auto
                    tipo2 += 1
                    recaudado_tipo2 += auto
                    recaudado_efectivo += auto

                elif forma_pago == 1 and tipo == 3:
                    print("Tipo: CAMION - Forma de Pago: Efectivo ")
                    bandera = camion
                    c_efectivo += 1
                    total_recaudado += camion
                    tipo3 += 1
                    recaudado_tipo3 += camion
                    recaudado_efectivo += camion
                # Telepeaje...
                #VALIDACION, FALTA PATENTE RANDOM
                if forma_pago == 2 and tipo == 1:
                    print("Tipo: MOTO - Forma de Pago: Telepeaje ")
                    bandera = moto
                    c_telepeaje += 1
                    total_recaudado += moto
                    tipo1 += 1
                    recaudado_tipo1 += moto
                    recaudado_telepeaje += moto
                elif forma_pago == 2 and tipo == 2:
                    print("Tipo: AUTO - Forma de Pago: Telepeaje ")
                    bandera = auto
                    c_telepeaje += 1
                    total_recaudado += auto
                    tipo2 += 1
                    recaudado_tipo2 += auto
                    recaudado_telepeaje += auto

                elif forma_pago == 2 and tipo == 3:
                    print("Tipo: CAMION - Forma de Pago: Telepeaje ")
                    bandera = camion
                    c_telepeaje += 1
                    total_recaudado += camion
                    tipo3 += 1
                    recaudado_tipo3 += camion
                    recaudado_telepeaje += camion

                # CHEQUEO DE HORA DE TURNO

                if actual > 180:
                    c_hora4 += 1
                    recaudado_hora4 += bandera
                elif actual > 120:
                    c_hora3 += 1
                    recaudado_hora3 += bandera
                elif actual > 60:
                    c_hora2 += 1
                    recaudado_hora2 += bandera
                else:
                    c_hora1 += 1
                    recaudado_hora1 += bandera

                if c_hora1 > c_hora2 and c_hora1 > c_hora3 and c_hora1 > c_hora4:
                    hora_pico = "1° HORA"
                elif c_hora2 > c_hora3 and c_hora2 > c_hora4:
                    hora_pico = "2° HORA"
                elif c_hora3 > c_hora4:
                    hora_pico = "3° HORA"
                else:
                    hora_pico = "4° HORA"

                if c_telepeaje > c_efectivo:
                    mayor_tipo = 'Telepeaje'
                elif c_efectivo > c_telepeaje:
                    mayor_tipo = 'Efectivo'
                else:
                    pass


                time.sleep(retraso)
                ahora = time.time()


            # TIMER CON ---> CARGA AUTOMATICA <---

    elif opcion == 3:
        print("\n Cantidad de MOTOS: ", tipo1,
              "\n Cantidad de AUTOS: ", tipo2,
              "\n Cantidad de CAMIONES: ", tipo3,
              "\n Recaudado en EFECTIVO: ", recaudado_efectivo,
              "\n Recaudado en TELEPEAJE: ", recaudado_telepeaje,
              "\n Recaudadcion TOTAL: ", total_recaudado,
              "\n Cantidad TOTAL de PASES: ", c_hora1 + c_hora2 + c_hora3 + c_hora4,
              "\n Pago mas usado: ", mayor_tipo,
              "\n Cantidad de pases PROMEDIO: ", (c_hora1+c_hora2+c_hora3+c_hora4)/4,
              "\n Patente mas nueva: "
              "\n HORA PICO: ", hora_pico,
              "\n 1° HORA: ", c_hora1,
              "\n 2° HORA: ", c_hora2,
              "\n 3° HORA: ", c_hora3,
              "\n 4° HORA: ", c_hora4,)





    opcion = menu_principal()
