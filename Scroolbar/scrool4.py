# explore the mouse wheel with the Tkinter GUI toolkit
# Windows and Linux generate different events
# tested with Python25
import tkinter as tk

def mouse_wheel(event):
    global count
    # respond to Linux or Windows wheel event
    if event.num == 5 or event.delta == -120:
        count -= 1
    if event.num == 4 or event.delta == 120:
        count += 1
    label['text'] = count
    
count = 0
root = tk.Tk()
root.title('turn mouse wheel')
root['bg'] = 'darkgreen'
# with Windows OS
root.bind("<MouseWheel>", mouse_wheel)
# with Linux OS
root.bind("<Button-4>", mouse_wheel)
root.bind("<Button-5>", mouse_wheel)
label = tk.Label(root, font=('courier', 18, 'bold'), width=10)
label.pack(padx=40, pady=40)
root.mainloop()