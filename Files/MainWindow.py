import customtkinter as ctk
import tkinter as tk

from Files.NewEntryWindow import NewEntWin
from Files.EntryManager import EntryManager
from Files.PingManager import PingManager
from Files.EntryInfo import EntryInfo
from Files.Serialization import Save, Load

class MainWindow(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.EntryManager = EntryManager()
        self.PingManager = PingManager()
        self.CreateMainWindow()
        self.CreateLayout()
        self.bind("<Button-1>", self.unselect_all)

    def unselect_all(self, event):
        window_y = self.winfo_rooty() 
        mouse_y = self.winfo_pointery()

        relative_mouse_y = mouse_y - window_y

        window_height = self.winfo_height()

        if relative_mouse_y > window_height / 3:
            return
        
        self.Listbox.selection_clear(0, tk.END)

    def MainLoop(self):
        self.PingManager.PingAll(self.EntryManager.Entry_list)
        self.Update_Sites()
        self.Update_listbox()
        Save(self.EntryManager.Entry_list)
        self.after(1000, self.MainLoop)

    def NewEntryPressed(self):
        self.AddWindow = NewEntWin(callback=self.EntryAdded)

    def DeleteEntryPressed(self):
        if len(self.Listbox.curselection()) == 0:
            return
        if self.EntryManager.DeleteEntry(self.Listbox.curselection()[0]):
            self.Listbox.delete(self.Listbox.curselection()[0])

    def EntryAdded(self, Site, IP, Radius):
        self.EntryManager.CreateNewEntry(Site, IP, Radius)

        self.Listbox.insert(tk.END, f"Name: {Site} | IP: {IP} | Radius: {Radius}")

    def OpenEntryInfo(self,event):
        try:
            index = self.Listbox.curselection()[0]
            site = self.EntryManager.Entry_list[index]
            EntryInfo(site)
            self.Listbox.selection_clear(0, tk.END)
        except:
            pass


    def CreateLayout(self):
        self.NewEntryButton = ctk.CTkButton(self, text="New +", command=self.NewEntryPressed)
        self.DeleteEntryButton = ctk.CTkButton(self, text="Delete -", command=self.DeleteEntryPressed)
        self.ClearEntryButton = ctk.CTkButton(self, text="Clear /", command=self.ClearEntryPressed)
        self.Listbox = tk.Listbox(self, font=("Arial", 14), bg="#242424", fg="white")
        self.Listbox.bind("<Double-1>", self.OpenEntryInfo)

        self.NewEntryButton.pack(pady=10)
        self.DeleteEntryButton.pack(pady=10)
        self.ClearEntryButton.pack(pady=10)
        self.Listbox.pack(fill=tk.BOTH, expand=True)

    def ClearEntryPressed(self):
        for site in self.EntryManager.Entry_list:
            if site["State"] == 2:
             site["State"] = 1
             site["Ping"] = 0

    def CreateMainWindow(self):
        self.geometry("800x400")
        self.title("IP Monitor")

    def Update_listbox(self):
        curserSelection = self.Listbox.curselection()[0] if len(self.Listbox.curselection()) > 0 else ""
        self.Listbox.delete(0, tk.END)

        for site in self.EntryManager.Entry_list:
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

            self.Listbox.insert(tk.END, f"Name: {site["Site"]} | IP: {site["IP"]} | Status: {State} | Drops: {site["Drops"]} | Time: {site["Time"]} s")
            self.Listbox.itemconfig(tk.END, color)

        if curserSelection == "":
            return
        
        self.Listbox.selection_set(curserSelection)
        self.Listbox.activate(curserSelection)

    def Update_Sites(self):
        for site in self.EntryManager.Entry_list:
            site["Time"] += 1