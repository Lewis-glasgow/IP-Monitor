from Files.MainWindow import MainWindow
import customtkinter as ctk
import tkinter as tk


if __name__ == "__main__":
    Window = MainWindow()

    print(Window.EntryManager.Entry_list)

    for site in Window.EntryManager.Entry_list:
        State = ""
        color = {}
        match site["State"]:
            case 0: 
                State = "Offline"
                color = {'bg': "Red"}
            case 1: 
                State = "Online"
            case 2: 
                State = "Attention Required"
                color = {'bg': "Orange"}
        Window.Listbox.insert(tk.END, f"Name: {site["Site"]} | IP: {site["IP"]} | Status: {State} | Drops: {site["Drops"]} | Time: {site["Time"]} s")

    Window.after(1000, Window.MainLoop)
    Window.mainloop()