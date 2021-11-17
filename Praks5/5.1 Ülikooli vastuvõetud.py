aasta = int(input("Palun sisestage, millise aasta andmeid vajate: "))

fail = open("C:\\Users\\Kristjan\\Desktop\\rebased.txt", encoding="UTF-8")

loend = 0
vastuvõetud = []
for rida in fail:
    vastuvõetud.append(int(rida))
print(str(aasta) + " aastal oli vastuvõetuid " + str(vastuvõetud))

fail.close()