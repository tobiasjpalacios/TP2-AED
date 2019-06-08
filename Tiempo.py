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


