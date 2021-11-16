from tkinter import *

raam = Tk()
raam.title("Märk")

tahvel = Canvas(raam, width=500, height = 500)
tahvel.create_rectangle(4500, 0, 0, 3000, fill="white", outline="white")
tahvel.create_oval(5,5,500,500, fill="red", outline="red")
tahvel.create_rectangle(450, 200, 50, 300, fill="white", outline="white")

tahvel.pack()
raam.mainloop()