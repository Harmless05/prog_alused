def tervitus(tervitusarv):
    for i in range (1, tervitusarv + 1):
        print('Võõrustaja: "Tere!"')
        print("Täna", str(i)  + ". kord tervitada, mõtiskleb võõrustaja.")
        print('Külaline: "Tere, suur tänu kutse eest!"')
arv = int(input("Sisestage külaliste arv: "))
tervitus(arv)