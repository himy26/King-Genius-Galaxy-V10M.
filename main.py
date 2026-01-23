import customtkinter as ctk
import threading
import time
import winsound
import subprocess
import os
import requests
from tkinter import filedialog

# --- إعدادات المظهر النيوني ---
ctk.set_appearance_mode("dark")

class LevantiInfinitySupreme(ctk.CTk):
    def __init__(self):
        super().__init__()

        # 1. إعدادات النافذة
        self.title("LEVANTI INFINITY AI - V.61 FINAL POWER")
        self.geometry("1450x950")
        self.configure(fg_color="#0b0f19")

        # 2. مسارات المحرك والأدوات
        self.adb_path = "adb"
        self.fastboot_path = "fastboot"
        self.connected_serial = None
        self.mode = "Searching..."

        # 3. بناء الهيكل
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.setup_sidebar()
        self.setup_main_area()
        
        # 4. تشغيل الرادار الثلاثي
        self.start_triple_monitor()

    # ================== محرك العمليات القتالية (The Real Actions) ==================

    def force_wipe_mtk_brom(self):
        """الضربة القاضية لمعالجات MTK (تكنو، إنفينيكس، شاومي) - BROM Mode"""
        self.log_msg("🛡️ AI: WAITING FOR MTK DEVICE IN BROM MODE...")
        self.log_msg("💡 INSTRUCTION: 1. Power OFF. 2. Hold Vol+ & Vol-. 3. Connect USB.")
        
        def run_mtk_engine():
            try:
                # هذا الأمر يكسر الحماية ويمسح البيانات والـ FRP معاً
                cmd = "python -m mtk rf frp,userdata" 
                self.log_msg("🔥 AI: Injecting Exploit... Sending Payload.")
                
                process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                stdout, stderr = process.communicate(timeout=60)
                
                if "Success" in stdout or "Writing" in stdout:
                    self.log_msg("✅ SUCCESS: DEVICE UNLOCKED & WIPED!")
                    winsound.Beep(2000, 1000)
                else:
                    self.log_msg("❌ FAIL: Payload Rejected. Check Zadig Filter.")
                    self.log_msg(f"📝 LOG: {stdout[:50]}")
            except Exception as e:
                self.log_msg(f"❌ ERROR: {str(e)}")

        threading.Thread(target=run_mtk_engine, daemon=True).start()

    def frp_kill_samsung_adb(self):
        """تخطي FRP لسامسونج (بعد تفعيل ADB عبر *#0*#)"""
        if self.mode != "ADB":
            self.log_msg("❌ ERROR: Please enable ADB (Test Mode *#0*#) first!")
            return
        self.log_msg("🚀 AI: Killing FRP Lock via ADB...")
        try:
            subprocess.run([self.adb_path, "shell", "settings", "put", "secure", "user_setup_complete", "1"], check=True)
            self.log_msg("✅ SUCCESS: Home Screen Bypassed!")
        except: self.log_msg("❌ FAILED: Security block.")

    def fastboot_erase_action(self):
        """مسح البيانات عبر وضع فاست بوت (Fastboot)"""
        self.log_msg("⚠️ AI: INITIATING FASTBOOT WIPE...")
        try:
            subprocess.run([self.fastboot_path, "erase", "userdata"], check=True)
            subprocess.run([self.fastboot_path, "reboot"], check=True)
            self.log_msg("✅ SUCCESS: Fastboot Wipe Complete.")
        except: self.log_msg("❌ FAIL: Device not in Fastboot or locked.")

    # ================== واجهة المستخدم (The UI) ==================

    def setup_sidebar(self):
        self.sidebar = ctk.CTkFrame(self, width=280, fg_color="#111827", corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        
        ctk.CTkLabel(self.sidebar, text="👑 LEVANTI FORCE", font=("Orbitron", 22, "bold"), text_color="gold").pack(pady=30)

        # الأزرار القتالية
        self.add_side_btn("⚡ FORCE WIPE (MTK/BROM)", self.force_wipe_mtk_brom)
        self.add_side_btn("🔓 FRP KILL (ADB)", self.frp_kill_samsung_adb)
        self.add_side_btn("♻️ FASTBOOT ERASE", self.fastboot_erase_action)
        self.add_side_btn("🌐 MTP BROWSER OPEN", lambda: subprocess.run([self.adb_path, "shell", "am", "start", "-a", "android.intent.action.VIEW", "-d", "https://google.com"]))
        self.add_side_btn("❌ CLOSE TOOL", self.quit)

    def add_side_btn(self, text, command):
        btn = ctk.CTkButton(self.sidebar, text=text, fg_color="transparent", border_width=2, 
                            border_color="#38bdf8", text_color="#38bdf8", height=50,
                            font=("Arial", 12, "bold"), hover_color="#1e293b", command=command)
        btn.pack(fill="x", padx=20, pady=10)

    def setup_main_area(self):
        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        # Header
        header = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        header.pack(fill="x")
        ctk.CTkLabel(header, text="SUPREME UNLOCK ENGINE", font=("Orbitron", 26, "bold"), text_color="white").pack(side="left")
        ctk.CTkLabel(header, text="👑", font=("Arial", 50)).pack(side="right")

        # Status
        self.status_bar = ctk.CTkFrame(self.main_frame, height=45, fg_color="#1e293b", border_width=1, border_color="#38bdf8")
        self.status_bar.pack(fill="x", pady=15)
        self.status_text = ctk.CTkLabel(self.status_bar, text="📶 READY: SEARCHING FOR CPU...", font=("Consolas", 15))
        self.status_text.pack(pady=5)

        # Console
        self.terminal = ctk.CTkTextbox(self.main_frame, height=450, fg_color="black", text_color="#39FF14", font=("Consolas", 14))
        self.terminal.pack(fill="x", side="bottom")
        self.terminal.insert("0.0", ">>> [SYSTEM] LEVANTI AI ONLINE. READY FOR ACTION.")

    # ================== الرادار الثلاثي المطور ==================

    def start_triple_monitor(self):
        def monitor():
            while True:
                # فحص Fastboot
                fb = subprocess.run([self.fastboot_path, "devices"], capture_output=True, text=True)
                # فحص ADB
                adb = subprocess.run([self.adb_path, "devices"], capture_output=True, text=True)
                
                if fb.stdout.strip():
                    self.mode = "FASTBOOT"
                    self.status_text.configure(text=f"🔥 MODE: FASTBOOT (Bootloader)", text_color="#ef4444")
                elif "device" in adb.stdout and len(adb.stdout.strip().split('\n')) > 1:
                    self.mode = "ADB"
                    self.status_text.configure(text=f"📶 MODE: ADB ACTIVE (Online)", text_color="#39FF14")
                else:
                    self.mode = "Searching"
                    self.status_text.configure(text="📶 WAITING FOR USB (ADB/FASTBOOT/BROM)...", text_color="#38bdf8")
                time.sleep(3)
        threading.Thread(target=monitor, daemon=True).start()

    def log_msg(self, msg):
        self.terminal.insert("end", f"\n>>> {msg}")
        self.terminal.see("end")
        winsound.Beep(1000, 100)

if __name__ == "__main__":
    app = LevantiInfinitySupreme()
    app.mainloop()