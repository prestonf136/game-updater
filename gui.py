import tkinter as tk
from updater import *

root = tk.Tk()
root.resizable(False, False)

version = "v0.0.0"

canvas = tk.Canvas(root,height=700,width=500,bg="#f39c12")
canvas.pack()



framebottom = tk.Frame(root,bg="#f39c12")
framebottom.place(relwidth=1,relheight=0.1,relx=0,rely=0.45)

def Dobutt(sversion):
    if (CheckVersion(sversion) == True):
        return "Play!"
    else:
        return "Download"

def Updater():
    global version
    if (CheckVersion(version) == True):
        PlayFiles()
    else:
        MainButt["state"] = "disabled"
        UpdateFiles()
        version = CheckVersion(version)
        MainButt["state"] = "normal"
        MainButt["text"] = "Play!"
        

MainButt = tk.Button(framebottom,text=Dobutt(version),padx=10,pady=25,command=Updater)
MainButt.pack()




root.mainloop()