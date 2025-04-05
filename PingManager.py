import subprocess
import customtkinter as ctk
import tkinter as tk
import threading
from EntryManager import EntryManager

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
                
                print(output.stdout)
                Errors = ["Request timed out.", "Destination host unreachable.", "General failure"]

                for error in Errors:
                    if error in output.stdout or error in output.stderr:
                        print(f'Ping To {site["IP"]} Unsuccessful!!!')
                        callback(site, False)  # Pass False to callback
                        return
                
                print(f'Ping To {site["IP"]} Successful!')
                callback(site, True)  # Pass True to callback

            except subprocess.TimeoutExpired:
                print(f'Ping To {site["IP"]} Unsuccessful!!!')
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
        else:
            site["Ping"] += 1
            if site["Ping"] > 5 and site["State"] != 0:
                AlertWindow(site["Site"])
                site["Drops"] += 1
                site["State"] = 0

            print(site["Site"], "Down!!!")


class AlertWindow(ctk.CTkToplevel):
    def __init__(self, name):
        super().__init__()

        self.geometry("300x300")
        self.attributes("-topmost", True)
        self.title(name+" Down!!!")

        self.label = ctk.CTkLabel(self, text="SITE OFFLINE:")
        self.sitename = ctk.CTkLabel(self, text=name)
        self.gif_image = tk.PhotoImage(file="no-internet.gif")
        self.gif = tk.Label(self, image=self.gif_image)

        self.label.pack()
        self.sitename.pack()
        self.gif.pack()
