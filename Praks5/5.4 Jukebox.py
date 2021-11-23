failinimi = str(input("Palun sisestage failinimi: "))
fail = open(failinimi, encoding="UTF-8")

vastuvõetud = []
loend = 0
for rida in fail:
    loend += 1
    vastuvõetud.append(str(rida))
    print(str(round(loend)) + ". " + rida)

failirida = int(input("Valige laulu järjekorranumber: "))
print("Mängitav muusika on " + str(vastuvõetud[-1 + failirida]))
fail.close()