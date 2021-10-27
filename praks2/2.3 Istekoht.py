from random import randint
istekoht = str(input("Kas soovite istekohta ise valida (ise) või loosida (loos)? "))
if istekoht == "ise":
    laused = "Valisite ise."
    aken = str(input("Kas soovite istuda akna ääres (aken) või mitte (muu)? "))
elif istekoht == "loos":
    laused = "Istekoht loositi."

if istekoht == "ise":
    if aken == "aken":
        sõnad = "Aknakoht"
    elif aken == "muu":
        sõnad = "Vahekäigukoht"
elif istekoht == "loos":
    arv = randint(1, 3)
    if arv == 1:
        sõnad = "Aknakoht"
    elif arv == 2 or 3:
        sõnad = "Vahekäigukoht"
print(laused + " " + sõnad)