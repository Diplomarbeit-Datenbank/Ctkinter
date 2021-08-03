# show Ctkinter Canvas

import Ctkinter as Ctk
import tkinter as tk


root = tk.Tk()
root.title('Demonstration Ctkinter CLabel')

label_rounded = Ctk.CLabel(master=root, bg='blue', size=(400, 150), text='Hello World', fg='black', font=('Sans', 40),
                 corner='rounded', max_rad=None, outline=('', 0), anchor='CENTRE', variable_text=False,
                 enter_hit=(False, None), text_place=(10, 10))

label_round = Ctk.CLabel(master=root, bg='blue', size=(400, 150), text='Hello World', fg='black', font=('Sans', 40),
                 corner='round', max_rad=None, outline=('', 0), anchor='CENTRE', variable_text=False,
                 enter_hit=(False, None), text_place=(10, 10))

label_angular = Ctk.CLabel(master=root, bg='blue', size=(400, 150), text='Hello World', fg='black', font=('Sans', 40),
                 corner='angular', max_rad=None, outline=('', 0), anchor='CENTRE', variable_text=False,
                 enter_hit=(False, None), text_place=(10, 10))

label_rounded.place(x=4, y=2)
label_round.place(x=414, y=2)
label_angular.place(x=164, y=180)

root.mainloop()