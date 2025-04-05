import customtkinter as ctk
import tkinter as tk

class NewEntWin(ctk.CTkToplevel):
    def __init__(self, callback):
        super().__init__()

        self.geometry("300x280")
        self.attributes("-topmost", True)

        self.Callback = callback
        self.CreateLayout()

    def AddEntry(self, event=0):
        if self.SiteEntry.get() == "":
            return
        if self.IPEntry.get() == "":
            return
        if self.RadiusEntry.get() == "":
            return
        
        self.Callback(self.SiteEntry.get(), self.IPEntry.get(), self.RadiusEntry.get())
        self.destroy()

    def CreateLayout(self):
        frame = ctk.CTkFrame(self)
        frame.pack()
        self.SiteLabel = ctk.CTkLabel(frame, text="Site name: ")
        self.SiteEntry = ctk.CTkEntry(frame)
        self.IPLabel = ctk.CTkLabel(frame, text="IP: ")
        self.IPEntry = ctk.CTkEntry(frame)
        self.RadiusLabel = ctk.CTkLabel(frame, text="Radius: ")
        self.RadiusEntry = ctk.CTkEntry(frame)
        self.AddButton = ctk.CTkButton(self, text="Add +", command=self.AddEntry)

        self.RadiusEntry.bind("<Return>", self.AddEntry)

        self.SiteLabel.grid(column=0, row=0, pady=20, padx=10)
        self.SiteEntry.grid(column=1, row=0, pady=20, padx=10)
        self.IPLabel.grid(column=0, row=1, pady=20, padx=10)
        self.IPEntry.grid(column=1, row=1, pady=20, padx=10)
        self.RadiusLabel.grid(column=0, row=2, pady=20, padx=10)
        self.RadiusEntry.grid(column=1, row=2, pady=20, padx=10)

        self.AddButton.pack(pady=20, padx=10)