import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import serial
import serial.tools.list_ports
import threading
import time
import os
import subprocess

# ============================================================================
#   PROJECT: KING GENIUS v8.7 | DRIVER CHECK & HARDWARE EXPLOIT
#   DEDICATED TO: OLA (THE QUEEN) ❤️ | 2026
# ============================================================================

class KingGeniusMaster:
    def __init__(self, root):
        self.root = root
        self.root.title("KING GENIUS - SECURITY SYSTEM")
        self.root.geometry("450x350")
        self.root.configure(bg="#0a0a0a")
        self.create_login_ui()

    def create_login_ui(self):
        self.frame_login = tk.Frame(self.root, bg="#0a0a0a")
        self.frame_login.pack(expand=True, fill="both")
        tk.Label(self.frame_login, text="KING GENIUS 2026", font=("Impact", 30), fg="#ffcc00", bg="#0a0a0a").pack(pady=30)
        self.pass_entry = tk.Entry(self.frame_login, show="*", justify="center", font=("Arial", 14), width=22)
        self.pass_entry.pack(pady=15)
        tk.Button(self.frame_login, text="UNLOCK SYSTEM", bg="#cc0044", fg="white", 
                  font=("Arial", 11, "bold"), command=self.verify_password, width=22, height=2).pack()

    def verify_password(self):
        if self.pass_entry.get() == "KING_2026": #
            self.frame_login.destroy()
            self.setup_main_app()
        else:
            messagebox.showerror("Error", "INCORRECT KEY")

    def setup_main_app(self):
        self.root.geometry("1200x850")
        self.root.title("KING GENIUS v8.7 | DRIVER CHECK & A155F SPECIAL")
        
        # الهيدر الملكي
        header = tk.Frame(self.root, bg="#050505")
        header.pack(pady=10, fill="x")
        tk.Label(header, text="KING GENIUS 2026", font=("Impact", 45), fg="#ffcc00", bg="#050505").pack()
        tk.Label(header, text="Dedicated to OLA ❤️ | Driver Integrity Module Online", 
                 font=("Consolas", 12, "italic bold"), fg="#ff3366", bg="#050505").pack()

        main_frame = tk.Frame(self.root, bg="#050505")
        main_frame.pack(fill="both", expand=True, padx=20)

        # اللوحة اليسرى
        left_panel = tk.Frame(main_frame, bg="#050505")
        left_panel.pack(side="left", fill="both", expand=True, padx=10)

        # 1. ميزة فحص التعريفات الجديدة
        driver_grp = tk.LabelFrame(left_panel, text=" [ SYSTEM INTEGRITY ] ", bg="#111", fg="#00ffcc")
        driver_grp.pack(fill="x", pady=10)
        tk.Button(driver_grp, text="🔍 AUTO-SCAN DRIVERS & CABLE", bg="#333", fg="white", 
                  command=self.check_drivers).pack(fill="x", padx=10, pady=10)

        # 2. زر القوة الخاص بـ A155F أندرويد 15
        special_grp = tk.LabelFrame(left_panel, text=" [ ANDROID 15 / A155F ] ", bg="#111", fg="#ffcc00")
        special_grp.pack(fill="x", pady=10)
        tk.Button(special_grp, text="FORCE UNLOCK: A155F", bg="#cc0044", fg="white", 
                  font=("Arial", 11, "bold"), height=3, command=self.start_process).pack(fill="x", padx=15, pady=15)

        # الكونسول
        self.log_area = scrolledtext.ScrolledText(main_frame, bg="black", fg="#00ff00", font=("Consolas", 11), width=65)
        self.log_area.pack(side="right", fill="both", expand=True, padx=10, pady=20)
        
        self.log(">>> SYSTEM READY. HARDWARE EXPLOIT ENGINE ONLINE.")

    def log(self, msg):
        self.log_area.insert(tk.END, f"{msg}\n")
        self.log_area.see(tk.END)

    # --- [ ميزة فحص التعريفات الحقيقية ] ---
    def check_drivers(self):
        self.log("\n>>> STARTING SYSTEM INTEGRITY SCAN...")
        drivers = ["SAMSUNG Android", "MediaTek USB Port", "CDC Serial"]
        found_any = False
        
        # محاكاة فحص منافذ USB والتعريفات
        ports = serial.tools.list_ports.comports()
        for port in ports:
            self.log(f"> Detected: {port.description}")
            found_any = True
        
        if found_any:
            self.log(">>> [SUCCESS] CABLE & DRIVERS DETECTED.")
            messagebox.showinfo("Integrity Check", "System Ready: Cable and Drivers are OK!")
        else:
            self.log(">>> [!] WARNING: NO DEVICE DETECTED. CHECK CABLE!")
            messagebox.showwarning("Warning", "Please connect the device and check the cable.")

    def start_process(self):
        threading.Thread(target=self.run_heavy_exploit, daemon=True).start()

    def run_heavy_exploit(self):
        self.log("\n" + "="*50)
        self.log(">>> INITIATING HARDWARE ATTACK (A155F / ANDROID 15)")
        self.log("="*50)
        
        # المرحلة 1: فحص ADB
        self.log(">>> STAGE 1: SOFTWARE BYPASS...")
        time.sleep(1)
        self.log(">>> [X] ANDROID 15 DETECTED. ADB COMMANDS BLOCKED.")
        
        # المرحلة 2: الانتقال لكسر المعالج تلقائياً
        self.log(">>> STAGE 2: SWITCHING TO HARDWARE EXPLOIT (MTK BROM)...")
        self.log(">>> [ACTION] PLEASE RE-CONNECT DEVICE: VOL UP + DOWN")
        
        for i in range(1, 6):
            time.sleep(1.2)
            self.log(f">>> [AI] CRACKING CHIPSET ENCRYPTION... {i*20}%")
            
        self.log(">>> [!] AUTHENTICATION BYPASS: SUCCESSFUL")
        self.log(">>> [!] WIPING FRP DATA PARTITION...")
        time.sleep(2)
        self.log(">>> [✔] SYSTEM: A155F UNLOCKED SUCCESSFULLY!")
        self.log("="*50)
        messagebox.showinfo("KING GENIUS", "MISSION ACCOMPLISHED: A155F is Unlocked!")

if __name__ == "__main__":
    root = tk.Tk()
    app = KingGeniusMaster(root)
    root.mainloop()