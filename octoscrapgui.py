import tkinter as tk
from octoscrap import scrapit, base_url


window = tk.Tk()
window.geometry("270x100")

folder = tk.StringVar(window, value="Octocats")
base_url = tk.StringVar(window, value=base_url)

fr1 = tk.Frame()
fr2 = tk.Frame()


tk.Label(fr1,text="Folder Name: ").grid(column=0,row=0,pady=2)
tk.Label(fr1,text="Url: ").grid(column=0,row=1,pady=2)


fol = tk.Entry(fr1, textvariable=folder)
url = tk.Entry(fr1, textvariable=base_url)

fol.grid(column=2, row=0, pady=2)
url.grid(column=2,row=1,pady=2)

submit = tk.Button(text="Download", command=lambda: scrapit(url.get(), fol.get()))

fr1.grid()
submit.grid(pady=6)

window.mainloop() 

