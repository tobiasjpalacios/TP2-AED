
def patente_nueva(patente, patentenueva):
    
    if len(patente) < len(patentenueva):
        patentenueva= patentenueva 
   
    elif len(patente) <=len(patentenueva):
        if len(patente)==7 :
            if patentenueva[0] > patente[0]:
                patentenueva= patente
            else:
                if patentenueva[1] > patente[1]:
                    patentenueva= patente
                else:
                    if patentenueva[2] > patente[2]:
                        patentenueva= patente
                    else:
                        if patentenueva[3] > patente[3]:
                            patentenueva= patente
                        else:
                            if patentenueva[4] > patente[4]:
                                patentenueva= patente
                            else:
                                if patentenueva[5] > patente[5]:
                                    patentenueva= patente
                                else:
                                    if patentenueva[6] > patente[6]:
                                        patentenueva= patente
                                    else:
                                        patentenueva= patentenueva
        if len(patentenueva)==6:
            if patentenueva[0] > patente[0]:
                patentenueva= patente
            else:
                if patentenueva[1] > patente[1]:
                    patentenueva= patente
                else:
                    if patentenueva[2] > patente[2]:
                        patentenueva= patente
                    else:
                        if patentenueva[3] > patente[3]:
                            patentenueva= patente
                        else:
                            if patentenueva[4] > patente[4]:
                                patentenueva= patente
                            else:
                                if patentenueva[5] > patente[5]:
                                    patentenueva= patente


    else:
        patentenueva= patente

    return patentenueva


patentenueva=input("patente ")

patente= input("otra patente")

patentenueva1=patente_nueva(patente,patentenueva)
print(patentenueva1)

