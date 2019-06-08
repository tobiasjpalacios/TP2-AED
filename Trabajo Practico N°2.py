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

                retraso = random.randint(9, 15)  # La idea es que un vehiculo arribe al peaje entre 9 a 15 minutos
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

                if forma_pago == 2 and tipo == 1:
                    pass
                elif forma_pago == 2 and tipo == 2:
                    pass
                elif forma_pago == 2 and tipo == 3:
                    pass

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

                retraso = random.randint(9, 15)  # La idea es que un vehiculo arribe al peaje entre 9 a 15 minutos
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
                forma_pago = 1

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

                if forma_pago == 2 and tipo == 1:
                    pass
                elif forma_pago == 2 and tipo == 2:
                    pass
                elif forma_pago == 2 and tipo == 3:
                    pass

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

                time.sleep(retraso)
                ahora = time.time()
            print(total_recaudado, recaudado_hora4, recaudado_hora3, recaudado_hora2, recaudado_hora1,c_hora1 + c_hora2 + c_hora3 + c_hora4)

            # TIMER CON ---> CARGA AUTOMATICA <---

    elif opcion == 3:
        print("\n Cantidad de MOTOS: ", tipo1,
              "\n Cantidad de AUTOS: ", tipo2,
              "\n Cantidad de CAMIONES: ", tipo3,
              "\n Recaudado en EFECTIVO: ", recaudado_efectivo,
              "\n Recaudado en TELEPEAJE: "
              "\n Recaudadcion TOTAL: ", total_recaudado,
              "\n Cantidad TOTAL de PASES: ", c_hora1 + c_hora2 + c_hora3 + c_hora4,
              "\n Pago mas usado: ",
              "\n Cantidad de pases PROMEDIO: ", (c_hora1+c_hora2+c_hora3+c_hora4)/4,
              "\n Patente mas nueva: "
              "\n HORA PICO: ")





    opcion = menu_principal()