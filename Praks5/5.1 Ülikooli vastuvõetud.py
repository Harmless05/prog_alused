aasta = int(input("Palun sisestage, millise aasta andmeid vajate: "))

vastuvõetud = []
fail = open("C:\\Users\\Kristjan\\Desktop\\rebased.txt", encoding="UTF-8")

kokku = 0
for rida in fail:
    vastuvõetud.append(int(rida))
fail.close()

print(str(aasta) + " aastal oli vastuvõetuid " + str(vastuvõetud[aasta - 2011]))