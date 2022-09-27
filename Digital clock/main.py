import tkinter as tk

import time


window = tk.Tk()
window.title("Digi_clock")
window.config(background="Black")

def clock():
    hours = time.strftime("%I")
    minutes = time.strftime("%M")
    seconds = time.strftime("%S")
    am_or_pm = time.strftime("%p")
    clock_time = hours + ":" + minutes + ":" + seconds + " " + am_or_pm
    digital_clock_label.config(text= clock_time,background="Black",foreground="White")
    digital_clock_label.after(1000,clock)


digital_clock_label = tk.Label(window,text=" ",
                               font="Hellvatica 69 bold")
digital_clock_label.pack()

clock()

window.mainloop()