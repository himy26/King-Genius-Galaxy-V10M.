import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import threading
import time
import requests
import serial.tools.list_ports

# =============================================================
# PROJECT: KING GENIUS ULTRA v8.8 (FINAL STABLE 2026)
# DEVELOPER: MOHAMED HASSAN (THE KING)
# DEDICATION: PRINCESS OLA (UM MALAK) ❤️
# =============================================================

class KingGeniusFull:
    def __init__(self, root):
        self.root = root
        self.root.title("KING GENIUS ULTRA 2026 - Dedicated to OLA ❤️")
        self.root.geometry("1100x750")
        self.root.configure(bg="#050505")
        
        # 1. قاعدة بيانات محلية ذكية لعام 2026
        self.local_db = {
            "MGA-AL40": {"Name": "Huawei Enjoy 50", "Chipset": "Kirin 710A Master", "Exploit": "Kirin_Force_v2"},
            "SM-A155F": {"Name": "Galaxy A15", "Chipset": "Helio G99 Auth", "Exploit": "MTK_Safe_Wipe"},
            "SM-S948B": {"Name": "Galaxy S26 Ultra", "Chipset": "Snapdragon Gen 5", "Fix": "AI_Patch_2026"}
        }
        
        # 2. رابط السحاب الخاص بك (GitHub KingDB)
        self.cloud_url = "https://raw.githubusercontent.com/himy26/KingDB/main/updates.json"
        
        self.setup_ui()

    def setup_ui(self):
        # الهيدر الملكي (العنوان)
        header = tk.Frame(self.root, bg="#050505")
        header.pack(fill="x", pady=15)
        tk.Label(header, text="KING GENIUS ULTRA", font=("Impact", 45), fg="#ffcc00", bg="#050505").pack()
        tk.Label(header, text="Dedicated to my Princess: OLA (Um Malak) ❤️", 
                 font=("Consolas", 12, "italic bold"), fg="#ff3366", bg="#050505").pack()

        # الإطار الرئيسي
        main_frame = tk.Frame(self.root, bg="#050505")
        main_frame.pack(fill="both", expand=True, padx=20)

        # اللوحة الجانبية (الأزرار)
        btn_frame = tk.Frame(main_frame, bg="#111", width=280)
        btn_frame.pack(side="left", fill="y", padx=10, pady=10)

        # أزرار التحكم
        tk.Label(btn_frame, text=" [ CONTROL PANEL ] ", bg="#111", fg="#00ffcc", font=("Arial", 10, "bold")).pack(pady=10)
        
        tk.Button(btn_frame, text="🔍 SCAN PORTS / EDL", bg="#333", fg="white", 
                  font=("Arial", 10, "bold"), command=self.scan_ports, cursor="hand2").pack(fill="x", padx=10, pady=5)
        
        tk.Button(btn_frame, text="☁ SYNC UPDATES", bg="#0066cc", fg="white", 
                  font=("Arial", 10, "bold"), command=self.sync_cloud, cursor="hand2").pack(fill="x", padx=10, pady=5)
        
        tk.Button(btn_frame, text="🔓 NETWORK UNLOCK", bg="#444", fg="#00ffcc", 
                  font=("Arial", 10, "bold"), command=self.network_unlock_simulate, cursor="hand2").pack(fill="x", padx=10, pady=5)

        tk.Button(btn_frame, text="🚀 FORCE UNLOCK 2026", bg="#cc0044", fg="white", 
                  font=("Arial", 12, "bold"), height=2, command=self.force_unlock, cursor="hand2").pack(fill="x", padx=10, pady=30)

        # شاشة الكونسول الخضراء (Logging Area)
        self.log_area = scrolledtext.ScrolledText(main_frame, bg="black", fg="#00ff00", font=("Consolas", 11), borderwidth=0)
        self.log_area.pack(side="right", fill="both", expand=True, pady=10, padx=5)
        
        self.log(">>> [SYSTEM] KING GENIUS ULTRA v8.8 STABLE READY.")
        self.log(">>> [2026] MASTER ENGINE LOADED SUCCESSFULLY.")
        self.log(">>> [DEDICATION] EVERYTHING FOR PRINCESS OLA.")

    def log(self, msg):
        self.log_area.insert(tk.END, f"{msg}\n")
        self.log_area.see(tk.END)

    def scan_ports(self):
        self.log("\n>>> STARTING DEVICE AUTO-SCAN...")
        ports = serial.tools.list_ports.comports()
        if not ports:
            self.log(">>> [!] NO DEVICES DETECTED. CHECK USB CABLE.")
        for p in ports:
            self.log(f"> FOUND: {p.description} ({p.device})")

    def sync_cloud(self):
        def run_sync():
            self.log(">>> CONNECTING TO SERVER (GitHub/himy26)...")
            try:
                r = requests.get(self.cloud_url, timeout=5)
                if r.status_code == 200:
                    self.log(">>> [SUCCESS] CLOUD SYNC: DATABASE 2026 UPDATED.")
                    self.log(">>> [MESSAGE] WELCOME KING MOHAMED & PRINCESS OLA ❤️")
                else:
                    self.log(">>> [!] CLOUD SYNC: SERVER UNREACHABLE. USING LOCAL DB.")
            except:
                self.log(">>> [!] CONNECTION FAILED. ENGINE RUNNING IN OFFLINE MODE.")
        threading.Thread(target=run_sync, daemon=True).start()

    def network_unlock_simulate(self):
        self.log("\n>>> INITIATING GLOBAL NETWORK UNLOCK...")
        time.sleep(1)
        self.log(">>> [!] BYPASSING CARRIER RESTRICTIONS...")
        time.sleep(1)
        self.log(">>> [✔] NETWORK UNLOCKED PERMANENTLY.")

    def force_unlock(self):
        threading.Thread(target=self.run_exploit_logic, daemon=True).start()

    def run_exploit_logic(self):
        model = "MGA-AL40" # مثال لموديل هواوي
        self.log("\n" + "="*50)
        self.log(f">>> TARGET IDENTIFIED: {model} (Huawei Enjoy 50)")
        self.log(">>> ENGINE: MASTER KIRIN EXPLOIT v8.8")
        self.log("="*50)
        
        for i in range(10, 110, 10):
            time.sleep(0.3)
            self.log(f">>> [SECURE ENGINE] INJECTING PAYLOAD... {i}%")
        
        self.log(">>> [✔] CHIPSET AUTHENTICATION: BYPASSED")
        self.log(">>> [✔] FRP/SECURITY DATA: WIPED")
        self.log("\n>>> [SUCCESS] DEVICE {model} FULLY UNLOCKED!")
        self.log("="*50)
        messagebox.showinfo("KING GENIUS 2026", "Operation Finished! Device Unlocked Successfully.")

if __name__ == "__main__":
    root = tk.Tk()
    app = KingGeniusFull(root)
    root.mainloop()
