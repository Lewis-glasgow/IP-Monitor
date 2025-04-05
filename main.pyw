from  Files.MainWindow import MainWindow
import customtkinter as ctk
import tkinter as tk
import pickle
import os


if __name__ == "__main__":
    Window = MainWindow()

    if os.path.exists('data.pkl'):
        with open('data.pkl', 'rb') as f:
            Window.EntryManager.Entry_list = pickle.load(f)

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

    with open('data.pkl', 'wb') as f:
        pickle.dump(Window.EntryManager.Entry_list, f)