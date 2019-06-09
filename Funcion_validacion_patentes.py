

def validacion_patente(patente):
    bandera = True
    n = 0
    for i in patente:
        n += 1
        if len(patente)==6:
            if n >= 1 and n <= 3:
                if "a" <= i <= "z":
                    pass
                else:
                    bandera = False
            elif n >= 4 and n <= 6:
                if "0" <= i <= "9":
                    pass
                else:
                    bandera = False
        if len(patente)==7: 
            if n >= 1 and n <= 2:
                if "a" <= i <= "z":
                    pass
                else:
                    bandera = False
            elif n >= 3 and n <= 5:
                if "0" <= i <= "9":
                    pass
                else:
                    bandera = False
            elif n >= 5 and n <= 6:
                if "a" <= i <= "z":
                    pass
                else:
                    bandera = False

    if n != 6 and n!= 7:
        bandera = False


    return bandera
            
patente =  tuple(input('Ingrese la patente de su vehiculo '))

flag = validacion_patente(patente)
if flag == True:
    print ("la patente esta bien")
else:
    print("no lo esta ")