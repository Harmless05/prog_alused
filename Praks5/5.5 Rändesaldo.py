sisseränne = open("sisseranne.txt", encoding="UTF-8")
väljaränne = open("valjaranne.txt", encoding="UTF-8")

sisse = []
välja = []

for rida in sisseränne:

    sisse.append(int(rida.strip()))

for rida in väljaränne:

    välja.append(int(rida.strip()))

sisseränne.close()
väljaränne.close()

vahe = []

for i in range(len(sisse)):
    vahe.append(sisse[i] - välja[i])

print(vahe)

if max(vahe) > 0:
    print("Suurim positiivne rändesaldo oli " + str(vahe.index(max(vahe))+1) + ". aastal.")
else:
    print("Positiivse rändesaldoga aastaid ei ole.")