from datetime import *
failinimi = str(input("Palun sisestage "))
fail = open(failinimi, encoding="UTF-8")
õpilased = []
for rida in fail:
    õpilased.append((rida.strip()))
fail.close

kuupäev = datetime.now().day

print(str("Täna tuleb vastama: " + õpilased[kuupäev - 1]))