from tkinter import *
 
raam = Tk()
raam.title("Maardu lipp")
tahvel = Canvas(raam, width=600, height = 300)
kõrgus = 100
i = 0
while i < 3:
    if i == 0 or i == 2:
        tahvel.create_rectangle(0, i * kõrgus, 600, (i + 1) * kõrgus, fill="deepskyblue1", outline="deepskyblue1")
    else:
        tahvel.create_rectangle(0, i * kõrgus, 600, (i + 1) * kõrgus, fill="white", outline="white")
    i += 1
tahvel.pack()
raam.mainloop()