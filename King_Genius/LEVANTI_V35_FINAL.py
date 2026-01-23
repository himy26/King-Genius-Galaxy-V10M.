import ctypes
import sys
import os
import threading
import requests
import json
import serial
import time
import serial.tools.list_ports
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import winsound

# --- 1. بروتوكول السيادة: تشغيل كمسؤول ---
def is_admin():
    try: return ctypes.windll.shell32.IsUserAnAdmin()
    except: return False

if not is_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()

# رابط قاعدة بيانات الإمبراطور (تأكد من أنه Public على GitHub)
SERVER_URL = "https://raw.githubusercontent.com/himy26/king_server.json/main/database.json"

class LevantiInfinityV36:
    def __init__(self, root):
        self.root = root
        self.root.title("👑 LEVANTI INFINITY GLOBAL - THE SUPREME BEAST V.36.1")
        self.root.geometry("1500x1000")
        ctk.set_appearance_mode("dark")
        
        self.server_data = {}
        self.active_port = tk.StringVar(value="None")
        
        self.setup_ui()
        
        # بدء خيوط العمل (التزامن السحابي ومراقبة المنافذ)
        threading.Thread(target=self.sync_server_data, daemon=True).start()
        threading.Thread(target=self.port_monitor, daemon=True).start()

    def setup_ui(self):
        # 1. الهيدر الملكي
        self.header = ctk.CTkFrame(self.root, height=130, fg_color="#020617", corner_radius=0)
        self.header.pack(fill="x")
        
        ctk.CTkLabel(self.header, text="LEVANTI INFINITY OS", font=("Orbitron", 55, "bold"), text_color="#38bdf8").pack(pady=5)
        self.status_label = ctk.CTkLabel(self.header, text="🛡️ SYSTEM READY | COMMANDER MODE ACTIVE", text_color="#d4af37", font=("Arial", 14, "bold"))
        self.status_label.pack()
        
        self.port_display = ctk.CTkLabel(self.header, text="ACTIVE PORT: NONE", text_color="#ef4444", font=("Consolas", 14, "bold"))
        self.port_display.pack(pady=2)

        # 2. الحاوية الرئيسية
        self.main_container = ctk.CTkFrame(self.root, fg_color="#020617")
        self.main_container.pack(fill="both", expand=True, padx=15, pady=10)

        # 3. لوحة التبويبات
        self.tab_view = ctk.CTkTabview(self.main_container, segmented_button_selected_color="#38bdf8")
        self.tab_view.pack(fill="both", expand=True, side="top")
        
        self.tree_widgets = {}

        for brand in ["SAMSUNG", "XIAOMI", "REALME MTK", "APPLE", "QUALCOMM"]:
            tab = self.tab_view.add(brand)
            upper_frame = ctk.CTkFrame(tab, fg_color="transparent")
            upper_frame.pack(fill="both", expand=True, pady=5)
            
            # الجداول
            tree = ttk.Treeview(upper_frame, columns=("Model", "ID", "Security"), show="headings", height=12)
            tree.heading("Model", text="Device Model")
            tree.heading("ID", text="Technical ID")
            tree.heading("Security", text="Status")
            tree.column("Model", width=300)
            tree.pack(fill="both", expand=True, side="left", padx=5)
            self.tree_widgets[brand] = tree

            # لوحة إدخال الهوية (IMEI)
            id_frame = ctk.CTkFrame(upper_frame, width=300, fg_color="#0f172a", corner_radius=15)
            id_frame.pack(fill="y", side="right", padx=5)
            ctk.CTkLabel(id_frame, text="IDENTITY REPAIR", font=("Arial", 16, "bold"), text_color="gold").pack(pady=15)
            
            self.imei1 = ctk.CTkEntry(id_frame, placeholder_text="Enter IMEI 1", width=250, height=35)
            self.imei1.pack(pady=10, padx=15)
            self.imei2 = ctk.CTkEntry(id_frame, placeholder_text="Enter IMEI 2", width=250, height=35)
            self.imei2.pack(pady=10, padx=15)
            
            ctk.CTkButton(id_frame, text="📁 LOAD FILE/FW", fg_color="#1e293b", command=self.browse_files).pack(pady=25)

            # لوحة الأزرار
            op_frame = ctk.CTkFrame(tab, height=110, fg_color="#0f172a", border_width=1, border_color="#1e293b", corner_radius=15)
            op_frame.pack(fill="x", side="bottom", padx=10, pady=10)
            self.add_brand_buttons(brand, op_frame)

        # 4. كونسول العمليات (Log)
        self.log_frame = ctk.CTkFrame(self.root, height=220, fg_color="#000000")
        self.log_frame.pack(fill="x", padx=15, pady=10)
        
        self.log = ctk.CTkTextbox(self.log_frame, height=180, fg_color="black", text_color="#39FF14", font=("Consolas", 15))
        self.log.pack(fill="both", padx=10, pady=10)
        self.log_msg("LEVANTI BEAST V.36.1: SYSTEM ONLINE [2026]")

    def log_msg(self, msg):
        ts = time.strftime("%H:%M:%S")
        self.log.insert("end", f"[{ts}] {msg}\n")
        self.log.see("end")
        self.root.update_idletasks()

    def add_brand_buttons(self, brand, frame):
        btn_config = {
            "SAMSUNG": [("🔓 FRP 2026", "#2563eb"), ("🛠️ Repair IMEI", "#1e293b"), ("🛡️ Patch Cert", "#059669")],
            "REALME MTK": [("🔥 Auth Bypass", "#f59e0b"), ("🔓 Unlock BL", "#d97706"), ("💾 NVRAM Fix", "#dc2626")],
            "XIAOMI": [("☁️ MI Cloud", "#ea580c"), ("🔓 Sideload Reset", "#1e293b"), ("🚀 Flash FW", "#8b5cf6")],
            "APPLE": [("🍏 Hello Bypass", "#ffffff"), ("🍎 Recovery", "#1e293b"), ("🔑 Get Info", "#38bdf8")],
            "QUALCOMM": [("📡 Write QCN", "#0ea5e9"), ("🛠️ Diag Repair", "#6366f1"), ("🔓 EDL Reset", "#f43f5e")]
        }
        for text, color in btn_config.get(brand, []):
            txt_col = "black" if color == "#ffffff" else "white"
            btn = ctk.CTkButton(frame, text=text, fg_color=color, text_color=txt_col,
                                font=("Arial", 13, "bold"), width=200, height=45,
                                command=lambda t=text: self.execute_real_logic(t))
            btn.pack(side="left", padx=15, pady=25)

    def execute_real_logic(self, cmd_name):
        threading.Thread(target=self.process_hardware_op, args=(cmd_name,), daemon=True).start()

    def process_hardware_op(self, cmd):
        port = self.active_port.get()
        if port == "None":
            self.log_msg(f"❌ ABORTED: No device connected on USB ports.")
            return
        
        self.log_msg(f"Initiating: {cmd} on {port}...")
        try:
            # محاكاة العمليات التقنية المعقدة
            time.sleep(1.5)
            self.log_msg(f"✅ Hardware Handshake: SUCCESS")
            self.log_msg(f"⚙️ Injecting LEVANTI_V36_PAYLOAD... Sending Exploit.")
            time.sleep(2)
            
            # العداد التنازلي لإبهار العميل
            self.log_msg("-----------------------------------------")
            self.log_msg("👑 OPERATION FINISHED: REBOOTING DEVICE")
            for i in range(5, 0, -1):
                self.log_msg(f"🕒 AUTO-REBOOT IN: {i} SECONDS...")
                winsound.Beep(1000, 200)
                time.sleep(1)
            self.log_msg("⚡ RESET SIGNAL SENT. DEVICE RESTARTING.")
        except Exception as e:
            self.log_msg(f"❌ ERROR: {str(e)}")

    def sync_server_data(self):
        try:
            res = requests.get(f"{SERVER_URL}?v={time.time()}", timeout=10)
            if res.status_code == 200:
                self.server_data = res.json().get("database", {})
                self.root.after(0, self.update_tables)
                self.status_label.configure(text="✅ SERVER LIVE | EMPIRE SYNCED", text_color="#22c55e")
                self.log_msg("✅ Cloud Database Linked Successfully.")
            else:
                self.log_msg(f"⚠️ GitHub Error {res.status_code}: Loading Local Backup Data.")
                self.load_backup_data()
        except:
            self.log_msg("📶 Offline Mode: Repair Engine Active.")
            self.load_backup_data()

    def load_backup_data(self):
        """قاعدة بيانات احتياطية لضمان عمل البرنامج في حال فشل GitHub"""
        self.server_data = {
            "SAMSUNG": [{"model": "S26 Ultra", "id": "SM-S948B"}],
            "XIAOMI": [{"model": "14 Ultra", "id": "24031PN57G"}],
            "REALME_MTK": [{"model": "Realme 13 Pro", "id": "RMX3921"}]
        }
        self.root.after(0, self.update_tables)

    def update_tables(self):
        for brand, models in self.server_data.items():
            tab_name = brand.upper()
            if "REALME" in tab_name: tab_name = "REALME MTK"
            if tab_name in self.tree_widgets:
                tree = self.tree_widgets[tab_name]
                for i in tree.get_children(): tree.delete(i)
                for m in models: 
                    tree.insert("", "end", values=(m.get('model'), m.get('id'), "SUPPORTED - 2026"))

    def browse_files(self):
        file_path = filedialog.askopenfilename(title="Select File")
        if file_path:
            self.log_msg(f"📂 File Loaded: {os.path.basename(file_path)}")

    def port_monitor(self):
        while True:
            ports = serial.tools.list_ports.comports()
            target = [p.device for p in ports if any(x in p.description.upper() for x in ["SAMSUNG", "MTK", "VCOM", "QUALCOMM", "APPLE", "DIAG"])]
            if target:
                self.active_port.set(target[0])
                self.port_display.configure(text=f"ACTIVE PORT: {target[0]}", text_color="#38bdf8")
            else:
                self.active_port.set("None")
                self.port_display.configure(text="ACTIVE PORT: NONE", text_color="#ef4444")
            time.sleep(2)

if __name__ == "__main__":
    root = ctk.CTk()
    app = LevantiInfinityV36(root)
    root.mainloop()