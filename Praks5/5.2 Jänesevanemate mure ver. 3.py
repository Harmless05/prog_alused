

arv = int(input("Sisestage ringide arv: "))

porgandid = 0
ring = 1
#while ring <= arv:
#    if ring % 2 == 0:
#        porgandid = porgandid + ring
#    ring = ring + 1

for i in range(arv):
    print("Porgandite koguarv or " + str(porgandid))
