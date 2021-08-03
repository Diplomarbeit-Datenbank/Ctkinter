# show Ctkinter CButton

import Ctkinter as Ctk
import tkinter as tk


root = tk.Tk()
root.title('Demonstration Ctkinter CButton')

button_rounded = Ctk.CButton(master=root, bg='blue', highlight_color='gray', pressing_color='white', width=400,
                             height=150, text='Press Me', font=('Sans', 40), fg='black', courser="hand2",
                             outline=('', 1), rounded_corners='rounded', image=None, command=None, max_rad=None,
                             dash=None)

button_round = Ctk.CButton(master=root, bg='blue', highlight_color='gray', pressing_color='white', width=400,
                             height=150, text='Press Me', font=('Sans', 40), fg='black', courser="hand2",
                             outline=('', 1), rounded_corners='round', image=None, command=None, max_rad=None,
                             dash=None)

button_angular = Ctk.CButton(master=root, bg='blue', highlight_color='gray', pressing_color='white', width=400,
                             height=150, text='Press Me', font=('Sans', 40), fg='black', courser="hand2",
                             outline=('', 1), rounded_corners='angular', image=None, command=None, max_rad=None,
                             dash=None)

button_rounded.place(x=0, y=2)
button_round.place(x=410, y=2)
button_angular.place(x=160, y=180)

root.mainloop()
