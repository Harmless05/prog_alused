from tkinter import *

raam = Tk()
raam.title("Malelaud")

#x1 (liigutab parempoolt)
#y1 (liigutab üles)
#x2 (liigutab vasakult)
#y2 (liigutab alla)

tahvel = Canvas(raam, width=800, height = 800)
#taust
tahvel.create_rectangle(1000, 0, 0, 1000, fill="white", outline="white")
#1 rida
tahvel.create_rectangle(100, 100, 0, 200, fill="black", outline="black")
tahvel.create_rectangle(100, 300, 0, 400, fill="black", outline="black")
tahvel.create_rectangle(100, 500, 0, 600, fill="black", outline="black")
tahvel.create_rectangle(100, 700, 0, 800, fill="black", outline="black")

#2 rida
tahvel.create_rectangle(200, 100, 100, 0, fill="black", outline="black")
tahvel.create_rectangle(200, 300, 100, 200, fill="black", outline="black")
tahvel.create_rectangle(200, 400, 100, 500, fill="black", outline="black")
tahvel.create_rectangle(200, 600, 100, 700, fill="black", outline="black")

#3 rida
tahvel.create_rectangle(300, 100, 200, 200, fill="black", outline="black")
tahvel.create_rectangle(300, 300, 200, 400, fill="black", outline="black")
tahvel.create_rectangle(300, 500, 200, 600, fill="black", outline="black")
tahvel.create_rectangle(300, 700, 200, 800, fill="black", outline="black")

#4 rida
tahvel.create_rectangle(400, 100, 300, 0, fill="black", outline="black")
tahvel.create_rectangle(400, 300, 300, 200, fill="black", outline="black")
tahvel.create_rectangle(400, 400, 300, 500, fill="black", outline="black")
tahvel.create_rectangle(400, 600, 300, 700, fill="black", outline="black")

#5 rida
tahvel.create_rectangle(500, 100, 400, 200, fill="black", outline="black")
tahvel.create_rectangle(500, 300, 400, 400, fill="black", outline="black")
tahvel.create_rectangle(500, 500, 400, 600, fill="black", outline="black")
tahvel.create_rectangle(500, 700, 400, 800, fill="black", outline="black")

#6 rida
tahvel.create_rectangle(600, 100, 500, 0, fill="black", outline="black")
tahvel.create_rectangle(600, 300, 500, 200, fill="black", outline="black")
tahvel.create_rectangle(600, 400, 500, 500, fill="black", outline="black")
tahvel.create_rectangle(600, 600, 500, 700, fill="black", outline="black")

#7 rida
tahvel.create_rectangle(700, 100, 600, 200, fill="black", outline="black")
tahvel.create_rectangle(700, 300, 600, 400, fill="black", outline="black")
tahvel.create_rectangle(700, 500, 600, 600, fill="black", outline="black")
tahvel.create_rectangle(700, 700, 600, 800, fill="black", outline="black")

#8 rida
tahvel.create_rectangle(800, 100, 700, 0, fill="black", outline="black")
tahvel.create_rectangle(800, 300, 700, 200, fill="black", outline="black")
tahvel.create_rectangle(800, 400, 700, 500, fill="black", outline="black")
tahvel.create_rectangle(800, 600, 700, 700, fill="black", outline="black")


tahvel.pack()
raam.mainloop()
