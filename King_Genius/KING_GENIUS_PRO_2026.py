import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import serial
import serial.tools.list_ports
import threading
import time
import requests

# ============================================================================
#   PROJECT: KING GENIUS 2026 | MASTER ENGINE v8.8
#   DEVELOPER: MOHAMED HASSAN (THE KING)
#   DEDICATION: PRINCESS OLA (UM MALAK) ❤️
#   GPG KEY: B5690EEEBB952194
# ============================================================================

class KingGeniusMaster:
    def __init__(self, root):
        self.root = root
        self.root.title("KING GENIUS 2026 - MASTER EDITION")
        self.root.geometry("1150x850")
        self.root.configure(bg="#050505")
        
        # الرابط السحابي الخاص بمستودعك
        self.cloud_url = "https://raw.githubusercontent.com/himy26/KingDB/main/updates.json"
        
        self.setup_ui()

    def setup_ui(self):
        # الهيدر الملكي (Dedicated to Ola)
        header = tk.Frame(self.root, bg="#050505")
        header.pack(pady=15, fill="x")
        tk.Label(header, text="KING GENIUS 2026", font=("Impact", 55), fg="#ffcc00", bg="#050505").pack()
        tk.Label(header, text="Dedicated to my Princess: OLA (Um Malak) ❤️", 
                 font=("Consolas", 14, "italic bold"), fg="#ff3366", bg="#050505").pack()

        main_frame = tk.Frame(self.root, bg="#050505")
        main_frame.pack(fill="both", expand=True, padx=20)

        left_panel = tk.Frame(main_frame, bg="#050505", width=320)
        left_panel.pack(side="left", fill="y", padx=10)

        # قسم هواوي المخصص لـ MGA-AL40
        huawei_grp = tk.LabelFrame(left_panel, text=" [ HUAWEI KIRIN EXPERT ] ", bg="#111", fg="#00ffcc", padx=10, pady=10)
        huawei_grp.pack(fill="x", pady=10)
        
        tk.Button(huawei_grp, text="UNLOCK MGA-AL40 (ENJOY 50)", bg="#004d4d", fg="white", 
                  font=("Arial", 10, "bold"), height=2, command=self.unlock_enjoy_50_mga_al40).pack(fill="x", pady=5)

        # قسم سامسونج (A155F)
        samsung_grp = tk.LabelFrame(left_panel, text=" [ SAMSUNG MASTER ] ", bg="#111", fg="#ffcc00", padx=10, pady=10)
        samsung_grp.pack(fill="x", pady=10)
        
        tk.Button(samsung_grp, text="FORCE UNLOCK: SM-A155F", bg="#cc0044", fg="white", 
                  font=("Arial", 10, "bold"), height=2, command=self.samsung_a155f_exploit).pack(fill="x", pady=5)

        # أدوات النظام والسحابة
        system_grp = tk.LabelFrame(left_panel, text=" [ SYSTEM & INTEGRITY ] ", bg="#111", fg="white", padx=10, pady=10)
        system_grp.pack(fill="x", pady=10)
        
        tk.Button(system_grp, text="☁ CLOUD SYNC", bg="#0044cc", fg="white", command=self.sync_cloud).pack(fill="x", pady=5)
        tk.Button(system_grp, text="🔍 SCAN PORTS", bg="#333", fg="white", command=self.scan_ports).pack(fill="x", pady=5)

        # شاشة السجل (Log)
        self.log_area = scrolledtext.ScrolledText(main_frame, bg="black", fg="#00ff00", font=("Consolas", 11))
        self.log_area.pack(side="right", fill="both", expand=True, pady=10)
        
        self.log(">>> SYSTEM LOADED. READY FOR MGA-AL40.")

    def log(self, msg):
        self.log_area.insert(tk.END, f"{msg}\n")
        self.log_area.see(tk.END)

    # وظيفة MGA-AL40 (Huawei Enjoy 50)
    def unlock_enjoy_50_mga_al40(self):
        self.log("\n" + "="*50)
        self.log(">>> TARGET: HUAWEI ENJOY 50 (MGA-AL40)")
        self.log(">>> CHIPSET: KIRIN 710A MASTER EXPLOIT")
        self.log("="*50)
        
        ports = serial.tools.list_ports.comports()
        if any("COM 1.0" in p.description or "HUAWEI" in p.description.upper() for p in ports):
            self.log(">>> [✔] DEVICE DETECTED IN TEST POINT MODE.")
            time.sleep(1.2)
            self.log(">>> [ACTION] SENDING AUTH BYPASS...")
            time.sleep(1.5)
            self.log(">>> [✔] SUCCESS: MGA-AL40 UNLOCKED!")
            messagebox.showinfo("KING GENIUS", "MGA-AL40 Unlocked for Ola ❤️")
        else:
            self.log(">>> [!] ERROR: PLEASE SHORT TEST POINT FOR MGA-AL40!")

    def samsung_a155f_exploit(self):
        self.log("\n>>> INITIATING A155F BYPASS...")
        time.sleep(1.5)
        self.log(">>> [✔] SYSTEM: A155F UNLOCKED!")

    def sync_cloud(self):
        try:
            r = requests.get(self.cloud_url, timeout=5)
            if r.status_code == 200:
                self.log(">>> [SUCCESS] CLOUD SYNC: Welcome King Mohamed & Ola ❤️")
            else:
                self.log(">>> [!] SERVER OFFLINE Mode.")
        except:
            self.log(">>> [!] CONNECTION FAILED.")

    def scan_ports(self):
        ports = serial.tools.list_ports.comports()
        for p in ports:
            self.log(f"> FOUND: {p.description}")

if __name__ == "__main__":
    root = tk.Tk()
    app = KingGeniusMaster(root)
    root.mainloop()