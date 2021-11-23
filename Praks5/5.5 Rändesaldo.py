fail = open("sisseranne.txt", encoding="UTF-8")
fail2 = open("valjaranne.txt", encoding="UTF-8")

arvud = []
for rida in fail:
    arvud.append(float(rida))


for element in arvud:
    if element > 0: 
        print(element)
        
fail.close()