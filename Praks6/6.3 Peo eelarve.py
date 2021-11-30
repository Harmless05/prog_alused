def eelarve(eelavearv):
    maxeelarve = kutsutud * 10 + 55
    return (maxeelarve)

def eelarve2(eelarvearv2):
    mineelarve = tuleb * 10 + 55
    return (mineelarve)

kutsutud = int(input("Mitu inimest on kutsutud? "))
tuleb = int(input("Mitu inimest tuleb? "))

print("Maksimaalne eelarve: " + str(eelarve(kutsutud)))
print("Minimaalne eelarve: " + str(eelarve2(tuleb)))