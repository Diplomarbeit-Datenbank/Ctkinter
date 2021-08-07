from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Scroolbar')
root.geometry('500x400')

# create a main Frame
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

# create a Canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Add a scrollbar to the Canvas
my_scroolbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scroolbar.pack(side=RIGHT, fill=Y)

# Configure the Canvas
my_canvas.configure(yscrollcommand=my_scroolbar.set, )
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

# Create another Frame inside the Canvas
second_frame = Frame(my_canvas)

# Add the new Frame to a Window in the Canvas
my_canvas.create_window((0, 0), window=second_frame, anchor='nw')


for thing in range(100):
    Button(second_frame, text=f'Button {thing} Yo!').grid(row=thing, column=0, padx=10, pady=10)

root.mainloop()