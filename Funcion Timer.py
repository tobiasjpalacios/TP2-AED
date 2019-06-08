def timer ():

    import time
    import random
    #import random

    inicio = time.time()
    ahora = inicio
    fin = inicio + 240


    #turno = (fin - inicio)

    #print(turno)

    while (ahora < fin):
        slp = random.randint(1, 10)
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

        tipo = int (input("1. Moto / 2. Auto / 3. Camion : "))
        while tipo != 1 and tipo != 2 tipo != 3:
            print("Ingrese las opciones disponibles")
            tipo = int(input("1. Moto / 2. Auto / 3. Camion : "))
        form_pago = int (input("1. Efectivo"))
        time.sleep(slp)
        ahora = time.time()

    contador = False
    return contador

timer()