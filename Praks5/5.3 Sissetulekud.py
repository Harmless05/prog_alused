fail = open("C:\\Users\\Kristjan\\Desktop\\konto.txt", encoding="UTF-8")
arvud = []
for rida in fail:
    arvud.append(float(rida))
fail.close()

for element in arvud:
    if element > 0: 
        print(element)