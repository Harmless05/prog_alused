def pronksikarva_arv(täisarvud):
    arv = 0
    for münt in täisarvud:
        if int(münt) <= 5:
            arv += int(münt)
    return arv
fail = str(input("Sisesta failinimi: "))
failinimi = open(fail, encoding="UTF-8")
print("Hoiupõrsasse läheb", pronksikarva_arv(failinimi), "senti.")