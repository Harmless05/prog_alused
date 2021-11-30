def banner(lause):
    return lause.upper()

banner2 = int(input("Mitu korda soovite reklaamlauset kuvada? "))
bannerlause = str(input("Sisestage reklaamlause: "))
kord = 1
while kord <= banner2:
    tulemus = banner(bannerlause)
    print(tulemus)
    kord = kord + 1
#for i in range(banner2):
#     print(banner(bannerlause))