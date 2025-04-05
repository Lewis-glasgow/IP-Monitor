import customtkinter as ctk
import tkinter as tk
import pyperclip

from EntryManager import EntryManager

class EntryInfo(ctk.CTkToplevel):
    def __init__(self, site):
        super().__init__()

        self.geometry("800x400")
        self.title(site["Site"])
        self.attributes("-topmost", True)
        self.site = site
        self.Create_Layout(site)

    def Create_Layout(self, site):
        self.frame = ctk.CTkFrame(self)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")
        self.frame.pack()
        self.NameTitleLabel = ctk.CTkLabel(self.frame, text="Name:")
        self.NameLabel = ctk.CTkLabel(self.frame, text=site["Site"])
        self.IPTitleLabel = ctk.CTkLabel(self.frame, text="IP:")
        self.IPLabel = ctk.CTkLabel(self.frame, text=site["IP"])
        self.RadiusTitleLabel = ctk.CTkLabel(self.frame, text="Radius:")
        self.RadiusLabel = ctk.CTkLabel(self.frame, text=site["Radius"])

        self.NameTitleLabel.grid(column=0, row=0, pady=10, padx=20)
        self.NameLabel.grid(column=0, row=1, pady=10, padx=20)

        self.IPTitleLabel.grid(column=1, row=0, pady=10, padx=20)
        self.IPLabel.grid(column=1, row=1, pady=10, padx=20)

        self.RadiusTitleLabel.grid(column=2, row=0, pady=10, padx=20)
        self.RadiusLabel.grid(column=2, row=1, pady=10, padx=50)

        self.NameCopyButton = ctk.CTkButton(self.frame, text="📋", command=self.NameCopyPressed)
        self.NameCopyButton.grid(column=0, row=2, pady=10, padx=50)

        self.IPCopyButton = ctk.CTkButton(self.frame, text="📋", command=self.IPCopyPressed)
        self.IPCopyButton.grid(column=1, row=2, pady=10, padx=50)

        self.RadiusCopyButton = ctk.CTkButton(self.frame, text="📋", command=self.RadiusCopyPressed)
        self.RadiusCopyButton.grid(column=2, row=2, pady=10, padx=50)

    def NameCopyPressed(self):
        pyperclip.copy(self.site["Site"])

    def IPCopyPressed(self):
        pyperclip.copy(self.site["IP"])
        
    def RadiusCopyPressed(self):
        pyperclip.copy(self.site["Radius"])



