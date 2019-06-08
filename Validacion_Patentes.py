"""Forma de pago:
1: Efectivo.
2: Telepeaje.
Si es telepeaje se debe solicitar además la patente del vehículo, teniendo en cuenta que sólo se aceptan patentes
correctas: ya sea de la forma LLLNNN o LLNNNLL (siendo L una letra y N un número). """

forma_pago = int(input('Ingrese su forma de pago: '))
while forma_pago !=1 and fpago !=2:
    print('Ingrese una forma de pago valida')
    forma_pago = int(input('Ingrese su forma de pago: '))
if forma_pago == 1:
    efectivo = True
    telepeaje = False
else:
    efectivo = False
    telepeaje = True
    patente = input('Ingrese la patente de su vehiculo')
    cantdig = len(patente)
    while cantdig != 6 and cantdig != 7:
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
