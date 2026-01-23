import customtkinter as ctk
import requests
import threading
import subprocess
import time

# --- إعدادات المظهر الملكي لعام 2026 ---
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class LevantiUltimateMaster(ctk.CTk):
    def __init__(self):
        super().__init__()

        # إعدادات النافذة (محفوظة باسم الإمبراطور محمد حسن والأميرة علا)
        self.title("LEVANTI INFINITY OS V.12 - BROM & BOOTLOADER MASTER")
        self.geometry("1200x900")
        self.server_url = "https://himy26.pythonanywhere.com/generate_key"
        self.owner = "ENG. MOHAMED HASSAN & OLA MATAWIE"

        # نظام التقسيم
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # 1. الشريط الجانبي (Sidebar)
        self.sidebar = ctk.CTkFrame(self, width=300, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        
        ctk.CTkLabel(self.sidebar, text="LEVANTI COMMANDER", font=("Orbitron", 22, "bold")).pack(pady=20)

        # --- مجموعة الأوامر الأساسية ---
        self.create_sidebar_button("🔍 Check Connected Devices", "adb devices", "#2ecc71")
        self.create_sidebar_button("📱 Reboot to Recovery", "adb reboot recovery", "#3498db")
        self.create_sidebar_button("⚡ Reboot to Fastboot", "adb reboot bootloader", "#3498db")
        
        # --- قسم فك تشفير المعالجات (BROM & AUTH BYPASS) ---
        ctk.CTkLabel(self.sidebar, text="🧠 BROM & CPU BYPASS", font=("Arial", 12, "bold"), text_color="#f1c40f").pack(pady=10)
        self.create_sidebar_button("🔓 MTK Auth Bypass (BROM)", "python mtk_bypass.py", "#f39c12")
        self.create_sidebar_button("🔑 Unlock OEM Secret", "fastboot oem unlock-go", "#f1c40f")
        self.create_sidebar_button("🚫 Clear Orange State", "fastboot oem clear_warning", "#34495e")

        # --- قسم أوامر الانفجار وضبط المصنع الإجباري ---
        ctk.CTkLabel(self.sidebar, text="🧨 EXPLOSION & FORCE RESET", font=("Arial", 12, "bold"), text_color="#e74c3c").pack(pady=10)
        self.create_sidebar_button("🚀 Raw Format Userdata", "fastboot format userdata", "#c0392b")
        self.create_sidebar_button("🧨 Destroy FRP Lock", "fastboot erase persistent", "#c0392b")
        self.create_sidebar_button("💥 Force Format:ext4", "fastboot format:ext4 userdata", "#c0392b")
        self.create_sidebar_button("🛡️ Tecno Master Wipe", "fastboot oem format", "#c0392b")
        
        # --- قسم تخطي الحمايات المتقدم ---
        ctk.CTkLabel(self.sidebar, text="🔓 ADVANCED BYPASS", font=("Arial", 12, "bold"), text_color="cyan").pack(pady=10)
        self.create_sidebar_button("✨ Tecno / Infinix FRP", "fastboot erase frp", "#9b59b6")
        self.create_sidebar_button("✨ Kill Security Config", "fastboot erase config", "#9b59b6")
        self.create_sidebar_button("🔄 Reboot System", "fastboot reboot", "#1abc9c")

        # 2. منطقة العرض (Main Console)
        self.main_frame = ctk.CTkFrame(self, corner_radius=15)
        self.main_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        self.console = ctk.CTkTextbox(self.main_frame, font=("Consolas", 15), fg_color="#000000", text_color="#33ff33")
        self.console.pack(fill="both", expand=True, padx=15, pady=15)

        self.status_bar = ctk.CTkLabel(self, text=f"Authority: {self.owner} | BROM Mode: Integrated", font=("Arial", 10))
        self.status_bar.grid(row=1, column=0, columnspan=2, pady=5)

    def create_sidebar_button(self, text, command, color):
        btn = ctk.CTkButton(self.sidebar, text=text, fg_color=color, hover_color="#444444",
                            command=lambda: self.run_real_cmd(command))
        btn.pack(padx=20, pady=5, fill="x")

    def log(self, msg):
        timestamp = time.strftime("%H:%M:%S")
        self.console.insert("end", f"[{timestamp}] {msg}\n")
        self.console.see("end")

    def run_real_cmd(self, command):
        self.log(f"Sending Command: {command}")
        threading.Thread(target=self.execute, args=(command,), daemon=True).start()

    def execute(self, command):
        # إرسال تقرير فوري لهاتف الملك محمد حسن عبر السيرفر (محفوظ)
        try:
            requests.post(self.server_url, json={"device_id": "ULTIMATE_V12", "cpu_model": f"EXEC: {command}"}, timeout=5)
        except: pass

        try:
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = process.communicate()
            
            if stdout: self.log(f"System Output:\n{stdout}")
            if stderr: self.log(f"Console Message:\n{stderr}")
            
            if not stdout and not stderr:
                self.log("✅ Operation completed successfully.")
            
        except Exception as e:
            self.log(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    app = LevantiUltimateMaster()
    app.mainloop()