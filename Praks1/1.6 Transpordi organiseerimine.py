inimesi = int(input("Sisestage inimeste arv: "))
ühe_bussi_istekohad = int(input("Sisestage bussi kohtade arv ühes bussis: "))
busside_arv = inimesi // ühe_bussi_istekohad
istekohad = ühe_bussi_istekohad * busside_arv
mahajäänud_inimesed = inimesi % istekohad
if mahajäänud_inimesed > 0:
    busside_arv = busside_arv + 1
print(input("Tuleb tellida juurde: " + str(busside_arv) + " bussi"))

#print(input("Busside arv: " + str(busside_arv)))
#print(input("Mahajäänud inimesi on: " + str(mahajäänud_inimesed)))
