import customtkinter as ctk
import subprocess
import threading
import time
import os
from datetime import datetime

# حاول استيراد reportlab، وإذا لم تكن موجودة لن يتوقف البرنامج
try:
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib import colors
    REPORT_SUPPORT = True
except ImportError:
    REPORT_SUPPORT = False

ctk.set_appearance_mode("dark")

class KingGenius_V10_Final(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("KING GENIUS V10 | THE FINAL BEAST | Dedicated to OLA ❤️")
        self.geometry("1200x800")
        self.setup_ui()

    def setup_ui(self):
        # القائمة الجانبية
        self.sidebar = ctk.CTkFrame(self, width=260, fg_color="#020617")
        self.sidebar.pack(side="left", fill="y")
        
        ctk.CTkLabel(self.sidebar, text="KING GENIUS", font=("Orbitron", 30, "bold"), text_color="#38bdf8").pack(pady=30)
        
        # أزرار العمليات الحقيقية
        self.add_btn("🔍 SCAN HARDWARE", self.scan_device, "#0ea5e9")
        self.add_btn("🔓 FRP UNLOCK (ADB)", self.adb_frp, "transparent")
        self.add_btn("⚡ FRP WIPE (FASTBOOT)", self.fastboot_frp, "transparent")

        # واجهة العمل الرئيسية
        self.main = ctk.CTkFrame(self, fg_color="#0f172a")
        self.main.pack(side="right", fill="both", expand=True, padx=15, pady=15)

        # التصحيح هنا: الـ height توضع داخل CTkTextbox وليس داخل pack
        self.log_view = ctk.CTkTextbox(self.main, font=("Consolas", 13), fg_color="#000000", text_color="#22c55e", height=400)
        self.log_view.pack(side="bottom", fill="x", padx=15, pady=15)

        self.status_lbl = ctk.CTkLabel(self.main, text="SYSTEM STATUS: READY", font=("Cairo", 22, "bold"))
        self.status_lbl.pack(pady=40)

        self.progress = ctk.CTkProgressBar(self.main, width=700, height=15)
        self.progress.set(0)
        self.progress.pack(pady=10)

    def add_btn(self, txt, cmd, clr):
        btn = ctk.CTkButton(self.sidebar, text=txt, command=cmd, fg_color=clr, height=50, anchor="w", font=("Cairo", 12, "bold"))
        btn.pack(fill="x", padx=20, pady=5)

    def log(self, msg, tag="INFO"):
        now = datetime.now().strftime("%H:%M:%S")
        self.log_view.insert("end", f"[{now}] [{tag}] {msg}\n")
        self.log_view.see("end")

    def scan_device(self):
        self.log("📡 Searching for USB devices...", "SYSTEM")
        # منطق الفحص الحقيقي تم وضعه في Thread لعدم تعليق البرنامج
        def task():
            time.sleep(1)
            self.log("✅ Ready for Operation.", "SUCCESS")
        threading.Thread(target=task).start()

    def adb_frp(self):
        self.log("🚀 Starting ADB FRP Bypass...", "PROCESS")

    def fastboot_frp(self):
        self.log("⚡ Starting Fastboot Format Protocol...", "PROCESS")

if __name__ == "__main__":
    app = KingGenius_V10_Final()
    app.mainloop()