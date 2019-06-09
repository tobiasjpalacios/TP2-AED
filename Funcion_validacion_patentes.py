

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
            
patente =  tuple(input('Ingrese la patente de su vehiculo '))

flag = validacion_patente(patente)
if flag == True:
    print ("la patente esta bien")
else:
    print("no lo esta ")