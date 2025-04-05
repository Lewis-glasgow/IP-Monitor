import customtkinter as ctk
import tkinter as tk

from  MainWindow import MainWindow

if __name__ == "__main__":
    Window = MainWindow()

    for site in Window.EntryManager.Entry_list:
        Window.Listbox.insert(tk.END, f"Name: {site["Site"]} | IP: {site["IP"]} | Radius: {site["Radius"]}")

    Window.after(1000, Window.MainLoop)
    Window.mainloop()