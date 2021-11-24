sisseränne = open("sisseranne.txt", encoding="UTF-8")
väljaränne = open("valjaranne.txt", encoding="UTF-8")

sisse = []
välja = []
max = 0

for rida in sisseränne:
    sisse.append(int(rida))
for rida1 in väljaränne:
        välja.append(int(rida1))
        
#lahutaja
for i in range(len(sisse)):
    sisse[i] = sisse[i] - välja[i]
    #sisse.append(sisse)
    
print(sisse)

maxsisse = max(sisse)

nrrida = sisse.index(sisse)

if maxsisse >= 0:
    print("Suurim positiivne rändesaldo oli " + str(nrrida) + ". aastal.")
else:
    print("Positiivse rändesaldoga aastaid ei ole.")

#close
sisseränne.close()
väljaränne.close()
