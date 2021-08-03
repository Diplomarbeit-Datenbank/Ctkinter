# show Ctkinter Canvas

import Ctkinter as Ctk
import tkinter as tk


root = tk.Tk()
root.title('Demonstration Ctkinter Canvas')

canvas_rounded = Ctk.CCanvas(master=root, bg='blue', size=(400, 150), corners='rounded', max_rad=40,
                             outline=('white', 2), dash=None)

canvas_round = Ctk.CCanvas(master=root, bg='blue', size=(400, 150), corners='round', max_rad=None,
                             outline=('white', 2), dash=None)

canvas_angular = Ctk.CCanvas(master=root, bg='blue', size=(400, 150), corners='angular', max_rad=20,
                             outline=('white', 2), dash=None)

canvas_rounded.place(x=0, y=2)
canvas_round.place(x=410, y=2)
canvas_angular.place(x=160, y=180)

root.mainloop()

