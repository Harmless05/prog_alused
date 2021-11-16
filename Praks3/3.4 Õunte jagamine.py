from random import randint

sum = 0
õunad = 14

arv = int(input("Mitu pöialpoissi tahab õuna (0-7): "))
while sum < arv:
    rand = randint(1,2)
    õunad = õunad - rand
    print(str(rand))
    sum = sum + 1
print("Lumivalgekesele jäi " + str(õunad) + " õuna.")