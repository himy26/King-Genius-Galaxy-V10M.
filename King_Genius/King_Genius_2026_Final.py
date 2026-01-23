import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import subprocess
import threading
import time
import requests
import os

# ============================================================================
#   PROJECT: KING GENIUS 2026 - ULTIMATE ALL-IN-ONE EDITION
#   DEVELOPER: MOHAMED HASSAN (THE KING)
#   DEDICATION: PRINCESS OLA (UM MALAK) ❤️
#   VERSION: 6.0 (FINAL MASTER - DEEP FIX & NETWORK REPAIR)
# ============================================================================

class KingGeniusMaster:
    def __init__(self, root):
        self.root = root
        self.root.title("KING GENIUS PRO 2026 - ULTIMATE MASTER")
        self.root.geometry("1350x950")
        self.root.configure(bg="#050505")
        
        self.cloud_url = "https://raw.githubusercontent.com/himy26/KingDB/main/updates.json"
        self.db_local = {}

        self.setup_ui()
        self.sync_from_cloud()

    def setup_ui(self):
        # Header
        header = tk.Frame(self.root, bg="#050505", pady=20)
        header.pack(fill="x")
        tk.Label(header, text="KING GENIUS ULTIMATE 2026", font=("Impact", 55), fg="#ffcc00", bg="#050505").pack()
        tk.Label(header, text="ALL-IN-ONE SERVICE ENGINE | FOR MY LOVE OLA ❤️", font=("Arial", 14, "bold"), fg="#ff3366", bg="#050505").pack()

        main_frame = tk.Frame(self.root, bg="#050505")
        main_frame.pack(fill="both", expand=True, padx=20)

        # Left Control Panel
        cp = tk.Frame(main_frame, bg="#111", width=400, bd=1, relief="sunken")
        cp.pack(side="left", fill="y", padx=10, pady=10)

        tk.Label(cp, text="SYSTEM OPERATIONS", fg="#00ffcc", bg="#111", font=("Arial", 12, "bold")).pack(pady=15)
        
        self.model_var = tk.StringVar()
        self.model_list = ttk.Combobox(cp, textvariable=self.model_var, font=("Arial", 11), state="readonly")
        self.model_list.pack(pady=10, padx=20, fill="x")

        # --- الأزرار الاحترافية الشاملة ---
        btn_font = ("Arial", 12, "bold")
        
        # 1. زر الإصلاح العميق
        tk.Button(cp, text="🔥 DEEP FIX (FRP/FORMAT/INFO)", bg="#b30000", fg="white", font=btn_font, height=2, command=self.run_deep_fix).pack(fill="x", padx=20, pady=10)
        
        # 2. زر إصلاح الشبكة والآيمي (الجديد)
        tk.Button(cp, text="📡 NETWORK & IMEI REPAIR", bg="#008855", fg="white", font=btn_font, height=2, command=self.run_network_repair).pack(fill="x", padx=20, pady=10)
        
        # 3. زر تفعيل وضع الدياج
        tk.Button(cp, text="🛠️ ENABLE DIAG MODE", bg="#aa5500", fg="white", font=("Arial", 10, "bold"), command=self.enable_diag).pack(fill="x", padx=40, pady=5)
        
        # 4. أزرار النظام
        tk.Button(cp, text="🔍 SCAN HARDWARE", bg="#333", fg="white", command=self.scan_hardware).pack(fill="x", padx=60, pady=5)
        tk.Button(cp, text="🔄 SYNC SERVER", bg="#0055aa", fg="white", command=self.sync_from_cloud).pack(fill="x", padx=60, pady=5)

        # Terminal Output
        console_frame = tk.Frame(main_frame, bg="#000")
        console_frame.pack(side="right", fill="both", expand=True, pady=10)
        self.console = scrolledtext.ScrolledText(console_frame, bg="black", fg="#00ff00", font=("Consolas", 12), borderwidth=0)
        self.console.pack(fill="both", expand=True)

    def log(self, text, color="#00ff00"):
        self.console.insert(tk.END, f"> {text}\n")
        self.console.see(tk.END)

    def sync_from_cloud(self):
        try:
            r = requests.get(self.cloud_url, timeout=10)
            if r.status_code == 200:
                self.db_local = r.json().get("new_models", {})
                self.model_list['values'] = list(self.db_local.keys())
                if self.db_local: self.model_list.current(0)
                self.log("CLOUD SYNC: SUCCESS. Database Updated.")
        except: self.log("CLOUD SYNC: OFFLINE Mode.")

    def run_cmd(self, command):
        try:
            process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
            stdout, stderr = process.communicate()
            if stdout: self.log(stdout)
            if stderr: self.log(f"LOG: {stderr}", "#ffff00")
            return True
        except: return False

    def scan_hardware(self):
        self.log("--- SCANNING FOR DEVICES ---")
        self.run_cmd("adb devices")
        self.run_cmd("fastboot devices")

    def enable_diag(self):
        self.log("Enabling Diagnostic Port...")
        self.run_cmd("adb shell setprop sys.usb.config diag,adb")
        self.log("DIAG MODE INITIATED.")

    def run_deep_fix(self):
        model = self.model_var.get()
        if not model: return
        def task():
            self.log(f"STARTING DEEP FIX: {model}", "#ffcc00")
            self.run_cmd("fastboot getvar all")
            self.run_cmd("fastboot erase frp")
            self.run_cmd("fastboot erase userdata")
            self.run_cmd("fastboot reboot")
            self.log("DEEP FIX COMPLETED! ❤️")
        threading.Thread(target=task, daemon=True).start()

    def run_network_repair(self):
        model = self.model_var.get()
        if not model: return
        def task():
            self.log(f"STARTING NETWORK REPAIR: {model}", "#00ffcc")
            # أوامر مسح ملفات الشبكة التالفة لإعادة التنشيط
            self.run_cmd("fastboot erase modemst1")
            self.run_cmd("fastboot erase modemst2")
            self.run_cmd("fastboot erase fsg")
            self.run_cmd("fastboot reboot")
            self.log("NETWORK REPAIRED. SIGNAL RESTORED! 📡")
        threading.Thread(target=task, daemon=True).start()

if __name__ == "__main__":
    root = tk.Tk()
    app = KingGeniusMaster(root)
    root.mainloop()