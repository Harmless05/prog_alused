ainepunktid = int(input("Sisestage anepunktide arv: "))
nädalad = int(input("Sisestage nädalate arv: "))
ajakulu = 26
tunnid = ainepunktid * ajakulu
ajakulu_vastus = tunnid / nädalad
print(round(ajakulu_vastus))