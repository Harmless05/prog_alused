arv = int(input("Sisestage ringide arv: "))
porgandid = 0
ring = 1
while ring <= arv:
    porgandid = porgandid + ring
    ring = ring + 1
print("Porgandite koguarv or " + str(porgandid))