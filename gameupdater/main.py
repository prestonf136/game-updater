import tkinter as tk
import requests
import thread6



datavars = {
    "versionurl":"http://localhost:8000/build/version.txt",
    #this wont exist create it
    "dataurl":"http://localhost:800/build/100MB.bin",
    "fversionurl":"http://localhost:8001/build/version.txt",
    #this wont exist create it
    "fdataurl":"http://localhost:8001/build/100MB.bin",
    #this file wont exist create it aswell
    "writefilename":"./old.txt"
}
currentbuild = "v0.0.0"

root = tk.Tk()
root.resizable(False, False)


def ifneedupdate():
    global currentbuild
    try:
        r = requests.get(datavars["versionurl"])
        data = r.text
        data = data.strip()
        if data == currentbuild:
            return "Play!"
        else:
            return "Download"
    except:
        r = requests.get(datavars["fversionurl"])
        data = r.text
        data = data.strip()
        if data == currentbuild:
            return "Play!"
        else:
            return "Download"

def Update():
    thread6.run_threaded(tUpdate)

@thread6.threaded()
def tUpdate():
    global currentbuild
    try:

        r = requests.get(datavars["versionurl"])
        data = r.text
        data = data.strip()
        if data == currentbuild:
            print("versequal")
        else:
            MainButt["state"] = "disabled"
            MainButt["text"] = "Downloading...."
            r = requests.get(datavars["dataurl"], stream=True)
            with open(datavars["writefilename"], 'wb') as fd:
                for chunk in r.iter_content(chunk_size=128):
                    fd.write(chunk)
                currentbuild = data
                MainButt["state"] = "normal"
                MainButt["text"] = "Play!"

    except:
            r = requests.get(datavars["fversionurl"])
            data = r.text
            data = data.strip()
            if data == currentbuild:
                print("versequal")
            else:
                MainButt["state"] = "disabled"
                MainButt["text"] = "Downloading...."
                r = requests.get(datavars["fdataurl"], stream=True)
                with open(datavars["writefilename"], 'wb') as fd:
                    for chunk in r.iter_content(chunk_size=128):
                        fd.write(chunk)
                    currentbuild = data
                    MainButt["state"] = "normal"
                    MainButt["text"] = "Play!"

canvas = tk.Canvas(root,height=700,width=500,bg="#f39c12")
canvas.pack()


framebottom = tk.Frame(root,bg="#f39c12")
framebottom.place(relwidth=1,relheight=0.1,relx=0,rely=0.45)

MainButt = tk.Button(framebottom,text=ifneedupdate(),padx=10,pady=25,command=Update)
MainButt.pack()

root.mainloop()