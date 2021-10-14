nimi = str(input("Sisestage oma nimi: "))
lubatud_kiirus = int(input("Sisestage lubatud kiirus (km/h): "))
tegelik_kiirus = int(input("Sisestage tegelik kiirus (km/h): "))
vastus = tegelik_kiirus - lubatud_kiirus
arvutatud_trahv = vastus * 3
trahv = min(arvutatud_trahv, 190)
print( str(nimi) + ", kiiruse ületamise eest on teie trahv " + str(trahv) + " eurot.")