from random import randint

suurus = float(input("Sisestage kirja suurus (MB): "))
pealkiri = str(input("Sisestage kirja teema pealkiri: "))
fail_kaasas = str(input("Kas kirjaga on kaasas file? "))

if suurus < 1.0 and fail_kaasas == "jah" :
    print("Kiri ei ole spämm")
elif pealkiri == "":
    print("Kiri on spämm")
else:
    print("Kiri on spämm")