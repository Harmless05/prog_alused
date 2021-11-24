aasta = int(input("Palun sisestage, millise aasta andmeid vajate: "))
fail = open("rebased.txt", encoding="UTF-8")
vastuvõetud = []
kokku = 0
for rida in fail:
    vastuvõetud.append(int(rida))
fail.close()

print(str(aasta) + " aastal oli vastuvõetuid " + str(vastuvõetud[aasta - 2011]))