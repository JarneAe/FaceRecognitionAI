import tkinter as tk
from VideoRecognition import VidRecognition, name


name = VidRecognition()
def InitializeMainGUI():

    print("name")

    window =tk.Tk()

    screenheight = window.winfo_screenheight()
    screenwidth = window.winfo_screenwidth()
    
    window.attributes("-fullscreen", True)
    
    label = tk.Label(
    text=("Welcome: {}".format(name)),
    font=("Courier", 44),
    fg="white",
    bg="#017835",
    width=screenwidth,
    height=screenheight
    )

    label.pack()
    
    window.mainloop()



   

