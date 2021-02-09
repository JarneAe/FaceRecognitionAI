import tkinter as tk

def InitializeMainGUI():
    window = tk.Tk()

    newwindow = tk.Toplevel(window)

    labelExample = tk.Label(newwindow, text = "New Window")

    labelExample.pack()

    window.mainloop()




   

