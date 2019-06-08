op = 1
while op != 4:

#visualizacion de las opciones...

    print('Menu de opciones')
    print('1) Forma de carga')
    print('2) Procesar las paradas')
    print('3) Ver resultados')
    print('4) Salir\n')
    op = int(input('Ingrese la opcion elegida: '))



    if op == 1:
        pass
 #La segunda opcion comienza con el turno, iniciando el conteo del tiempo. El menu funciona correctamente.
    elif op == 2:
        import time
        #import random

        inicio = time.time()
        ahora = inicio
        fin = inicio + 240
        #turno = (fin - inicio)

        #print(turno)

        while (ahora < fin):
            actual = int(ahora - inicio)
            if actual > 180:
                hora = 4
                #print("Hora 4 Minuto", actual)
            elif actual > 120:
                hora = 3
                #print("Hora 3 Minuto", actual)
            elif actual > 60:
                hora = 2
                #print("Hora 2 Minuto", actual)
            else:
                hora = 1
                #print("Hora 1 Minuto", actual)
            #print(actual)
            time.sleep(1)
            ahora = time.time()
    elif op == 3:
        pass
