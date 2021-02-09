import tkinter as tk



def InitializeTkinter():

    window = tk.Tk()
    screenheight = window.winfo_screenheight()
    screenwidth = window.winfo_screenwidth()
    
    window.attributes("-fullscreen", True)

    button = tk.Button(
    text="Continue",
    width=screenwidth,
    height=5,
    bg="#017835",
    fg="white",
    )

    label = tk.Label(
        text="ACCESS GRANTED!",
        font=("Courier", 44),
        fg="white",
        bg="#017835",
        width=screenwidth,
        height=screenheight
    )

    
    button.pack(side=tk.BOTTOM)
    label.pack()
    
    window.mainloop()