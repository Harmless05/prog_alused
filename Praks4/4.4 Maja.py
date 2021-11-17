from tkinter import *

raam = Tk()
raam.title("Maja")

#x1 (liigutab parempoolt)
#y1 (liigutab üles)
#x2 (liigutab vasakult)
#y2 (liigutab alla)

tahvel = Canvas(raam, width=1000, height = 1000)
tahvel.create_rectangle(4500, 0, 0, 3000, fill="lightskyblue", outline="lightskyblue")
tahvel.create_rectangle(1000, 1000, 0, 600, fill="#66CD00", outline="#66CD00")
tahvel.create_rectangle(800, 700, 200, 300, fill="brown", outline="brown")
tahvel.create_rectangle(300, 700, 400, 500, fill="brown4", outline="brown4")
tahvel.create_rectangle(200, 100, 300, 300, fill="#8A3324", outline="#8A3324")
tahvel.create_polygon(850,300,150,300,500,0, fill="#8A360F",outline="#8A360F")
tahvel.create_rectangle(500, 600, 700, 400, fill="#8EE5EE", outline="#8EE5EE")

tahvel.pack()
raam.mainloop()