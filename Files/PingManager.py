import subprocess
import customtkinter as ctk
import tkinter as tk
import threading
from Files.EntryManager import EntryManager
from datetime import datetime

class PingManager():
    def ping_host(self, site, callback):
        def ping():
            try:
                output = subprocess.run(
                    ["ping", "-n", "1", site["IP"]],  # Use "-c" instead of "-n" on Linux/macOS
                    capture_output=True,
                    text=True,
                    timeout=3
                )
                
                Errors = ["Request timed out.", "Destination host unreachable.", "General failure", "Ping request could not find host"]

                print(output.stdout)
                for error in Errors:
                    if error in output.stdout or error in output.stderr:
                        callback(site, False)  # Pass False to callback
                        return
                
                callback(site, True)  # Pass True to callback

            except subprocess.TimeoutExpired:
                callback(site, False)

        # Start the ping operation in a separate thread
        threading.Thread(target=ping, daemon=True).start()

    def PingAll(self, Sites):
        for site in Sites:
            # Call ping_host in a separate thread
            self.ping_host(site, self.update_site_status)

    def update_site_status(self, site, status):
        # This method updates the site status (called from the background thread)
        if status:
            if site["State"] == 0:
                site["State"] = 2
                site["Ping"] = 0
                site["Sessions"]["Up"].append(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))  # Track "Up" event
        else:
            site["Ping"] += 1
            if site["Ping"] > 5 and site["State"] != 0:
                site["State"] = 0
                site["Drops"] += 1
                site["Sessions"]["Down"].append(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))  # Track "Down" event
                AlertWindow(site["Site"])

class AlertWindow(ctk.CTkToplevel):
    def __init__(self, name):
        super().__init__()

        w = 300
        h = 100
        x = self.winfo_screenwidth()/2 - w
        y = self.winfo_screenheight()/2 - h
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.attributes("-topmost", True)
        self.title(name+" Down!!!")

        self.label = ctk.CTkLabel(self, text="SITE OFFLINE:", text_color="Red")
        self.sitename = ctk.CTkLabel(self, text=name)

        self.label.pack()
        self.sitename.pack()
