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

        self.Table = ctk.CTkFrame(self)
        self.Table.place(relx=0.5, rely=0.5, anchor="center")

        self.LoadSessions(site)

    def LoadSessions(self, site):
        x_padding = 100
        y_padding = 1

        # Create header labels
        start_label = ctk.CTkLabel(self.Table, text="Start")
        start_label.grid(row=0, column=0, padx=x_padding, pady=y_padding)

        down_label = ctk.CTkLabel(self.Table, text="Down")
        down_label.grid(row=0, column=1, padx=x_padding, pady=y_padding)

        # Populate "Up" session times
        row_index = 2
        for start_time in site["Sessions"]["Up"][::-1]:
            session_label = ctk.CTkLabel(self.Table, text=start_time)
            session_label.grid(row=row_index, column=0, padx=x_padding, pady=y_padding)
            print("Session loaded:", start_time)
            row_index += 1

        row_index = 2
        if len(site["Sessions"]["Down"]) != len(site["Sessions"]["Up"]):
            row_index = 3

        for start_time in site["Sessions"]["Down"][::-1]:
            session_label = ctk.CTkLabel(self.Table, text=start_time)
            session_label.grid(row=row_index, column=1, padx=x_padding, pady=y_padding)
            print("Session loaded:", start_time)
            row_index += 1


    def NameCopyPressed(self):
        pyperclip.copy(self.site["Site"])

    def IPCopyPressed(self):
        pyperclip.copy(self.site["IP"])
        
    def RadiusCopyPressed(self):
        pyperclip.copy(self.site["Radius"])



