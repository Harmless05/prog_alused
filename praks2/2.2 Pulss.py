vanus = int(input("Sisesta enda vanus: "))
sugu = str(input("Sisesta enda sugu: "))
if sugu == "m" or sugu == "M":
    max_plusi_sagedus = 220 - vanus
if sugu == "n" or sugu == "N":
    max_plusi_sagedus = 206 - vanus * 0.88
treening = int(input("Sisesta treeningu tüüp: "))
if treening == 1:
    min_puls = max_plusi_sagedus * 0.5
    max_puls = max_plusi_sagedus * 0.7
elif treening == 2:
    min_puls = max_plusi_sagedus * 0.7
    max_puls = max_plusi_sagedus * 0.8
elif treening == 3:
    min_puls = max_plusi_sagedus * 0.8
    max_puls = max_plusi_sagedus * 0.87
#ümardamine
min_puls = round(min_puls)
max_puls = round(max_puls)
#vastus
print("Pulsisagedus peaks olema vahemikus " + str(min_puls) + " kuni " + str(max_puls) + ".")