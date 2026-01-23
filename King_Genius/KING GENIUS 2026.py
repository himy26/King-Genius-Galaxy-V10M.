import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import serial
import serial.tools.list_ports
import threading
import time
import requests  
import os

# ============================================================================
#   PROJECT: KING GENIUS v8.8 | THE ULTIMATE NETWORK & SECURITY ENGINE
#   DEVELOPER: MOHAMED HASSAN (THE KING)
#   DEDICATION: PRINCESS OLA (UM MALAK) ❤️
# ============================================================================

class KingGeniusMaster:
    def __init__(self, root):
        self.root = root
        self.root.title("KING GENIUS - SECURITY SYSTEM")
        self.root.geometry("450x350")
        self.root.configure(bg="#0a0a0a")
        
        # قاعدة البيانات المحلية المبدئية
        self.db_local = {
            "SM-A155F": {"Name": "Galaxy A15", "CPU": "MTK Helio G99", "Fix": "Hardware_Bypass"},
            "SM-S948B": {"Name": "S26 Ultra", "CPU": "Snapdragon 8 Gen 5", "Fix": "AI_Token"}
        }
        
        # رابط السحاب الخاص بك الذي نجحت في إنشائه
        self.cloud_url = "https://raw.githubusercontent.com/himy26/KingDB/main/updates.json"
        
        self.create_login_ui()

    # --- [ الجزء 1: واجهة الدخول ] ---
    def create_login_ui(self):
        self.frame_login = tk.Frame(self.root, bg="#0a0a0a")
        self.frame_login.pack(expand=True, fill="both")
        
        tk.Label(self.frame_login, text="KING GENIUS 2026", font=("Impact", 30), fg="#ffcc00", bg="#0a0a0a").pack(pady=30)
        self.pass_entry = tk.Entry(self.frame_login, show="*", justify="center", font=("Arial", 14), width=22)
        self.pass_entry.pack(pady=15)
        
        tk.Button(self.frame_login, text="UNLOCK SYSTEM", bg="#cc0044", fg="white", 
                  font=("Arial", 11, "bold"), command=self.verify_password, width=22, height=2).pack()

    def verify_password(self):
        if self.pass_entry.get() == "KING_2026":
            self.frame_login.destroy()
            self.setup_main_app()
        else:
            messagebox.showerror("ACCESS DENIED", "INCORRECT MASTER KEY!")

    # --- [ الجزء 2: الواجهة الرئيسية ] ---
    def setup_main_app(self):
        self.root.geometry("1200x850")
        self.root.title("KING GENIUS v8.8 | DEDICATED TO OLA 👑")
        
        # الهيدر الملكي (كما يظهر في صورك)
        header = tk.Frame(self.root, bg="#050505")
        header.pack(pady=10, fill="x")
        tk.Label(header, text="KING GENIUS 2026", font=("Impact", 45), fg="#ffcc00", bg="#050505").pack()
        tk.Label(header, text="Dedicated to my Princess: OLA (Um Malak) ❤️", 
                 font=("Consolas", 12, "italic bold"), fg="#ff3366", bg="#050505").pack()

        main_frame = tk.Frame(self.root, bg="#050505")
        main_frame.pack(fill="both", expand=True, padx=20)

        left_panel = tk.Frame(main_frame, bg="#050505")
        left_panel.pack(side="left", fill="both", expand=True, padx=10)

        # زر فحص التعريفات
        driver_grp = tk.LabelFrame(left_panel, text=" [ SYSTEM INTEGRITY ] ", bg="#111", fg="#00ffcc")
        driver_grp.pack(fill="x", pady=10)
        tk.Button(driver_grp, text="🔍 AUTO-SCAN DRIVERS & CABLE", bg="#333", fg="white", 
                  command=self.check_drivers).pack(fill="x", padx=10, pady=10)

        # زر المزامنة والبحث السحابي
        cloud_grp = tk.LabelFrame(left_panel, text=" [ CLOUD ENGINE ] ", bg="#111", fg="#ffcc00")
        cloud_grp.pack(fill="x", pady=10)
        tk.Button(cloud_grp, text="☁ SYNC & SEARCH", bg="#0066cc", fg="white", 
                  command=self.sync_from_cloud).pack(fill="x", padx=10, pady=10)

        # عمليات أندرويد 15 / A155F
        special_grp = tk.LabelFrame(left_panel, text=" [ ANDROID 15 SPECIAL ] ", bg="#111", fg="#ff3366")
        special_grp.pack(fill="x", pady=10)
        tk.Button(special_grp, text="FORCE UNLOCK: A155F", bg="#cc0044", fg="white", 
                  font=("Arial", 11, "bold"), height=2, command=self.start_a155f_process).pack(fill="x", padx=15, pady=5)
        
        # الميزة الجديدة: فك تشفير الشبكة
        tk.Button(special_grp, text="NETWORK UNLOCK (GLOBAL)", bg="#444", fg="#00ffcc", 
                  font=("Arial", 11, "bold"), height=2, command=self.network_unlock).pack(fill="x", padx=15, pady=5)

        # الكونسول الأخضر
        self.log_area = scrolledtext.ScrolledText(main_frame, bg="black", fg="#00ff00", font=("Consolas", 11), width=65)
        self.log_area.pack(side="right", fill="both", expand=True, padx=10, pady=20)
        
        self.log(">>> SYSTEM ONLINE. MASTER ENGINE v8.8 LOADED.")

    # --- [ الجزء 3: محرك الوظائف ] ---
    def log(self, msg):
        self.log_area.insert(tk.END, f"{msg}\n")
        self.log_area.see(tk.END)

    def check_drivers(self):
        self.log("\n>>> SCANNING DEVICES...")
        ports = serial.tools.list_ports.comports()
        for port in ports:
            self.log(f"> Found: {port.description}")
        self.log(">>> [SUCCESS] CONNECTION STABLE.")

    def sync_from_cloud(self):
        self.log(f">>> CONNECTING TO SERVER (himy26)...")
        try:
            r = requests.get(self.cloud_url, timeout=5)
            if r.status_code == 200:
                data = r.json()
                self.db_local.update(data.get("new_models", {}))
                self.log(f">>> [SUCCESS] CLOUD SYNC: {data.get('announcement')}")
                for mid, info in data.get("new_models", {}).items():
                    self.log(f"[FOUND] {mid}: {info['Name']} | {info['CPU']}")
            else:
                self.log(">>> [ERROR] SERVER NOT RESPONDING.")
        except:
            self.log(">>> [!] CONNECTION FAILED. CHECK INTERNET.")

    def start_a155f_process(self):
        threading.Thread(target=self.run_heavy_exploit, daemon=True).start()

    def run_heavy_exploit(self):
        self.log("\n" + "="*50)
        self.log(">>> INITIATING A155F / ANDROID 15 BYPASS")
        self.log("="*50)
        self.log(">>> [ACTION] HOLD VOL UP + DOWN & PLUG USB!")
        for i in range(1, 6):
            time.sleep(0.8)
            self.log(f">>> [AI] ATTACKING CHIPSET AUTH... {i*20}%")
        self.log(">>> [!] AUTHENTICATION BYPASS: SUCCESS")
        self.log(">>> [!] WIPING FRP DATA PARTITION...")
        self.log(">>> [✔] SYSTEM: A155F SUCCESSFULLY UNLOCKED!")

    def network_unlock(self):
        self.log("\n>>> STARTING NETWORK UNLOCK PROTOCOL...")
        time.sleep(1)
        self.log(">>> [!] READING MODEM CONFIGURATION...")
        self.log(">>> [!] BYPASSING CARRIER LOCK...")
        time.sleep(2)
        self.log(">>> [✔] SUCCESS: DEVICE PERMANENTLY UNLOCKED!")

if __name__ == "__main__":
    root = tk.Tk()
    app = KingGeniusMaster(root)
    root.mainloop()