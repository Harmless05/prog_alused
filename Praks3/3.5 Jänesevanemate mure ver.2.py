arv = int(input("Sisestage ringide arv: "))
porgandid = 0
porgandid_karbis = 0
ring = 1
while ring <= arv:
    porgandid_karbis = porgandid_karbis + ring
    porgandid = porgandid + porgandid_karbis
    ring = ring + 1
print("Porgandite koguarv on " + str(porgandid))