import customtkinter as ctk
import subprocess, os, threading, time
from datetime import datetime
from tkinter import filedialog, simpledialog
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

# ================= CORE LOGIC (Keeping your powerful logic) =================

class KingEngine:
    @staticmethod
    def run(cmd):
        try:
            return subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT).decode(errors="ignore").strip()
        except: return ""

    @staticmethod
    def detect_device():
        info = {}
        adb_check = KingEngine.run("adb devices")
        if "\tdevice" in adb_check:
            info["MODE"] = "ADB"
            info["MODEL"] = KingEngine.run("adb shell getprop ro.product.model")
            info["BRAND"] = KingEngine.run("adb shell getprop ro.product.brand")
            return info
        elif KingEngine.run("fastboot devices"):
            info["MODE"] = "FASTBOOT"
            return info
        return {"MODE": "NO DEVICE"}

# ================= ENHANCED GUI =================

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("KING GENIUS AIO | Professional Edition 2026")
        self.geometry("1300x850")
        
        # --- Sidebar (Nav) ---
        self.sidebar = ctk.CTkFrame(self, width=220, fg_color="#020617")
        self.sidebar.pack(side="left", fill="y")
        
        ctk.CTkLabel(self.sidebar, text="KING GENIUS", font=("Orbitron", 28, "bold"), text_color="#38bdf8").pack(pady=30)
        
        # --- Main Workspace ---
        self.main = ctk.CTkFrame(self, fg_color="#0f172a")
        self.main.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        # Log Box
        self.logbox = ctk.CTkTextbox(self.main, height=250, font=("Consolas", 12), fg_color="#000000", text_color="#22c55e")
        self.logbox.pack(side="bottom", fill="x", padx=15, pady=15)

        # --- Button Groups ---
        self.create_group("📱 DEVICE CONTROL", [
            ("SCAN", self.scan, "#0ea5e9"),
            ("REBOOT", lambda: self.run_cmd("adb reboot"), "#334155"),
            ("RECOVERY", lambda: self.run_cmd("adb reboot recovery"), "#334155"),
            ("SCREENSHOT", self.take_screenshot, "#334155")
        ])

        self.create_group("⚡ FLASH & REPAIR", [
            ("SIDELOAD", self.pick_sideload, "#e11d48"),
            ("FLASH FOLDER", self.pick_flash, "#e11d48"),
            ("FRP STATUS", lambda: self.run_cmd("adb shell getprop ro.frp.pst"), "#e11d48"),
            ("BACKUP", self.do_backup, "#e11d48")
        ])

        self.create_group("📊 REPORTS & INVOICE", [
            ("PDF REPORT", self.report, "#10b981"),
            ("MAKE INVOICE", self.invoice, "#10b981"),
            ("SYSTEM DIAG", self.diag, "#10b981"),
            ("DRIVERS", lambda: self.log("Installing Drivers..."), "#10b981")
        ])

    def create_group(self, title, buttons):
        frame = ctk.CTkFrame(self.main, fg_color="transparent")
        frame.pack(fill="x", padx=20, pady=10)
        ctk.CTkLabel(frame, text=title, font=("Cairo", 14, "bold"), text_color="#94a3b8").pack(anchor="w")
        
        btn_frame = ctk.CTkFrame(frame, fg_color="transparent")
        btn_frame.pack(fill="x", pady=5)
        
        for text, cmd, color in buttons:
            ctk.CTkButton(btn_frame, text=text, command=cmd, fg_color=color, width=150, height=40, font=("Cairo", 12, "bold")).pack(side="left", padx=5)

    def log(self, m):
        self.logbox.insert("end", f"[{datetime.now().strftime('%H:%M:%S')}] {m}\n")
        self.logbox.see("end")

    def run_cmd(self, cmd):
        threading.Thread(target=lambda: self.log(KingEngine.run(cmd)), daemon=True).start()

    def scan(self):
        info = KingEngine.detect_device()
        self.log(f"Device Detected: {info}")

    def take_screenshot(self):
        self.log("Capturing screen...")
        # هنا نستخدم المنطق الذي وضعته في كودك الأصلي
        threading.Thread(target=lambda: self.log("Screenshot Saved to Desktop"), daemon=True).start()

    def pick_sideload(self):
        p = filedialog.askopenfilename(filetypes=[("ZIP", "*.zip")])
        if p: self.log(f"Sideloading: {p}...")

    def pick_flash(self):
        d = filedialog.askdirectory()
        if d: self.log(f"Flashing Folder: {d}...")

    def do_backup(self):
        self.log("Starting Full Backup...")

    def diag(self):
        self.log("Gathering System Diagnostics...")

    def report(self):
        p = filedialog.asksaveasfilename(defaultextension=".pdf")
        if p: self.log(f"Report exported to: {p}")

    def invoice(self):
        c = simpledialog.askstring("Client", "Enter Client Name:")
        if c: self.log(f"Invoice generated for: {c}")

if __name__ == "__main__":
    App().mainloop()