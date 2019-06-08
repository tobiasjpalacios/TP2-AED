letras = 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', \
         'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',\
         's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
numeros = '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'

def validacion_patentes():
    patente = str(input('Ingrese la patente de su vehiculo'))
    cantdig = len(patente)
    while (cantdig != 6 and cantdig != 7):
        print('Ingrese una patente valida')
        patente = input('Ingrese la patente de su vehiculo')
        cantdig = len(patente)
    if cantdig == 6:
        parte1 = patente[0] + patente[1] + patente[2]
        parte2 = patente[3] + patente[4] + patente[5]
        parte3 = ''
        formafin = parte1 + parte2 + parte3
        patente = formafin
        patenteN = False
        patenteV = True

    elif cantdig == 7:
        parte1 = patente[0] + patente[1]
        parte2 = patente[3] + patente[2] + patente[4]
        parte3 = patente[5] + patente[6]
        formafin = parte1 + parte2 + parte3
        patente = formafin
        patenteN = True
        patenteV = False
    return patente

patente = validacion_patentes()
