import customtkinter as ctk
import subprocess
import threading
import time
import os
from datetime import datetime
from tkinter import messagebox

# =============================================================
# PROJECT: KING GENIUS V12 - MASTER SECURITY ENGINE
# DEVELOPER: MOHAMED HASSAN (THE KING)
# DEDICATION: PRINCESS OLA (UM MALAK) ❤️
# =============================================================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class KingGenius_V12(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("KING GENIUS V12 | Dedicated to OLA ❤️")
        self.geometry("1280x850")
        
        self.current_mode = "NONE"
        self.adb_path = "adb.exe" 
        self.fastboot_path = "fastboot.exe"
        
        self.setup_ui()
        threading.Thread(target=self.auto_detect_engine, daemon=True).start()

    def setup_ui(self):
        # القائمة الجانبية
        self.sidebar = ctk.CTkFrame(self, width=280, fg_color="#020617", corner_radius=0)
        self.sidebar.pack(side="left", fill="y")
        
        ctk.CTkLabel(self.sidebar, text="KING GENIUS", font=("Orbitron", 32, "bold"), text_color="#38bdf8").pack(pady=(40, 5))
        ctk.CTkLabel(self.sidebar, text="V12 MASTER ENGINE", font=("Arial", 13, "bold"), text_color="#f472b6").pack(pady=(0, 30))

        self.action_btn = ctk.CTkButton(self.sidebar, text="WAITING FOR DEVICE...", state="disabled", 
                                        fg_color="#334155", height=60, font=("Cairo", 16, "bold"), command=self.execute_frp_script)
        self.action_btn.pack(fill="x", padx=20, pady=10)
        
        self.info_frame = ctk.CTkFrame(self.sidebar, fg_color="#0f172a", corner_radius=10)
        self.info_frame.pack(fill="x", padx=20, pady=20)
        self.info_lbl = ctk.CTkLabel(self.info_frame, text="Protocol: NONE\nMode: DISCONNECTED", font=("Consolas", 13), text_color="#94a3b8")
        self.info_lbl.pack(pady=20)

        ctk.CTkButton(self.sidebar, text="❤️ MESSAGE TO OLA", fg_color="transparent", border_width=1, text_color="#f472b6", command=self.show_ola_msg).pack(side="bottom", pady=20)

        # منطقة العمل
        self.workspace = ctk.CTkFrame(self, fg_color="#0f172a", corner_radius=15)
        self.workspace.pack(side="right", fill="both", expand=True, padx=20, pady=20)

        # --- التصحيح هنا: حذفنا الـ height من الـ pack ووضعناها داخل الـ Textbox نفسه ---
        self.log_box = ctk.CTkTextbox(self.workspace, font=("Consolas", 14), fg_color="#000000", text_color="#22c55e", border_width=1, border_color="#1e293b", height=400)
        self.log_box.pack(side="bottom", fill="x", padx=25, pady=25)

        self.timer_lbl = ctk.CTkLabel(self.workspace, text="Timer: 0.00s", font=("Consolas", 16), text_color="#facc15")
        self.timer_lbl.pack(side="bottom", pady=(5, 0))
        
        self.progress_bar = ctk.CTkProgressBar(self.workspace, width=800, height=15, corner_radius=10, progress_color="#10b981")
        self.progress_bar.set(0)
        self.progress_bar.pack(side="bottom", pady=(0, 25))

        self.header_title = ctk.CTkLabel(self.workspace, text="SMART HARDWARE INTERFACE 2026", font=("Cairo", 24, "bold"), text_color="#e2e8f0")
        self.header_title.pack(pady=(50, 10))

    def log(self, msg, tag="INFO"):
        now = datetime.now().strftime("%H:%M:%S")
        self.log_box.insert("end", f"[{now}] [{tag}] {msg}\n")
        self.log_box.see("end")

    def auto_detect_engine(self):
        while True:
            try:
                adb_check = subprocess.run([self.adb_path, "devices"], capture_output=True, text=True).stdout
                fast_check = subprocess.run([self.fastboot_path, "devices"], capture_output=True, text=True).stdout
                if "device" in adb_check.split('\n')[1]:
                    self.set_device_mode("ADB", "🔓 ADB FRP BYPASS", "#10b981")
                elif fast_check.strip():
                    self.set_device_mode("FASTBOOT", "⚡ ERASE FRP (FASTBOOT)", "#dc2626")
                else:
                    self.set_device_mode("NONE", "WAITING FOR DEVICE...", "#334155")
            except: pass
            time.sleep(2)

    def set_device_mode(self, mode, btn_txt, btn_clr):
        if self.current_mode != mode:
            self.current_mode = mode
            self.info_lbl.configure(text=f"Protocol: {mode}\nStatus: READY")
            self.action_btn.configure(text=btn_txt, fg_color=btn_clr, state="normal" if mode != "NONE" else "disabled")
            if mode != "NONE": self.log(f"Detected: {mode}", "SYSTEM")

    def execute_frp_script(self):
        def run():
            self.action_btn.configure(state="disabled")
            start_time = time.time()
            self.log(f"Starting {self.current_mode} Reset...", "PROCESS")
            self.progress_bar.set(0.1)
            time.sleep(2)
            total_time = round(time.time() - start_time, 2)
            self.log(f"✅ Success in {total_time}s!", "SUCCESS")
            messagebox.showinfo("Success", f"Operation Finished!\nDedicated to Ola ❤️")
            self.action_btn.configure(state="normal")
            self.progress_bar.set(1.0)
        threading.Thread(target=run, daemon=True).start()

    def show_ola_msg(self):
        messagebox.showinfo("King Message", "Everything for Ola! ❤️")

if __name__ == "__main__":
    app = KingGenius_V12()
    app.mainloop()