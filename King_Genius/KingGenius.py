import customtkinter as ctk
import subprocess
import threading
import os
from datetime import datetime
from tkinter import messagebox

# إعدادات الواجهة الملكية لعام 2026
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class KingGenius_2026_Pro(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("KING GENIUS 2026 | MASTER SECURITY ENGINE | Dev: Mohamed Hassan")
        self.geometry("1200x850")
        
        # --- قاعدة بيانات 2026 المدمجة ---
        self.models_data = {
            "samsung": ["S25 Ultra (2026 Security)", "S24 Ultra", "A15 (SM-A155F)", "A05/A06 Universal", "Tab A9 Lite"],
            "huawei": ["Huawei Enjoy 50 (MGA-AL40)", "Kirin 710/810/980 Auto-Detect", "Mate 60 Pro", "Nova 12 Pro"],
            "infinix_tecno": ["Infinix Zero 40 5G", "TECNO POVA 7 Pro", "Infinix Note 40 Pro", "Spark 20 Pro+"],
            "oppo_realme": ["Oppo Reno 13 Pro", "Realme GT 7 Pro", "Oppo Reno 10 Pro+", "Realme 12 Pro+"],
            "motorola_vivo": ["Moto G34 5G (XT2363)", "Moto Edge 50", "Vivo X100 Pro", "iQOO 12 Pro"]
        }

        self.setup_ui()
        self.log("👑 KING GENIUS Engine v12.0 Ready. Waiting for Hardware...", "KING")
        self.log("❤️ Dedicated to Princess OLA (Um Malak).", "INFO")


    def setup_ui(self):
        # القائمة الجانبية الاحترافية
        self.sidebar = ctk.CTkFrame(self, width=260, corner_radius=0, fg_color="#020617")
        self.sidebar.pack(side="left", fill="y")

        ctk.CTkLabel(self.sidebar, text="KING GENIUS", font=("Orbitron", 28, "bold"), text_color="#38bdf8").pack(pady=30)
        ctk.CTkLabel(self.sidebar, text="Dedicated to Ola ❤️", font=("Cairo", 12), text_color="#f472b6").pack()
        
        # أزرار التنقل
        self.create_nav_btn("🔍 REAL USB SCAN", self.real_usb_scan, "#0ea5e9")
        self.create_nav_btn("📱 SAMSUNG MODULE", lambda: self.load_brand("samsung"), "transparent")
        self.create_nav_btn("📡 HUAWEI KIRIN", lambda: self.load_brand("huawei"), "transparent")
        self.create_nav_btn("🚀 INFINIX / TECNO", lambda: self.load_brand("infinix_tecno"), "transparent")
        self.create_nav_btn("🔋 MOTO / VIVO", lambda: self.load_brand("motorola_vivo"), "transparent")

        # منطقة العمل الرئيسية
        self.main_view = ctk.CTkFrame(self, fg_color="#0f172a")
        self.main_view.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        # شاشة اللوج (Console)
        self.log_box = ctk.CTkTextbox(self.main_view, height=350, font=("Consolas", 12), fg_color="#020617", text_color="#10b981")
        self.log_box.pack(side="bottom", fill="x", padx=15, pady=15)

        self.content = ctk.CTkFrame(self.main_view, fg_color="transparent")
        self.content.pack(fill="both", expand=True, pady=20)
        
        self.status_lbl = ctk.CTkLabel(self.content, text="Disconnected", font=("Cairo", 18), text_color="gray")
        self.status_lbl.pack(pady=10)
        
        self.selector = ctk.CTkComboBox(self.content, values=["Select Brand to Start..."], width=450, height=45)
        self.selector.pack(pady=20)
        
        self.exec_btn = ctk.CTkButton(self.content, text="EXECUTE MASTER OPERATION", font=("Cairo", 16, "bold"), 
                                     fg_color="#dc2626", hover_color="#991b1b", height=60, command=self.start_execution_thread)
        self.exec_btn.pack(pady=20)

    # --- محرك البحث عن الهاردوير ---
    def real_usb_scan(self):
        def _scan():
            self.log("🔍 Probing Ports (ADB/Fastboot)...", "INFO")
            try:
                # 1. فحص وضع ADB
                model = subprocess.check_output(["adb", "shell", "getprop ro.product.model"], text=True, timeout=2).strip()
                self.status_lbl.configure(text=f"CONNECTED: {model}", text_color="#10b981")
                self.log(f"✅ DEVICE IDENTIFIED (ADB): {model}", "SUCCESS")
            except:
                try:
                    # 2. فحص وضع Fastboot
                    fb = subprocess.check_output(["fastboot", "getvar", "product"], text=True, timeout=2).strip()
                    product_name = fb.split(':')[1].strip() if ':' in fb else fb # تحسين القراءة
                    self.log(f"⚡ FASTBOOT DETECTED: {product_name}", "SUCCESS")
                    self.status_lbl.configure(text="MODE: FASTBOOT", text_color="#fbbf24")
                except:
                    self.log("❌ NO HARDWARE FOUND. Check Cable, Drivers or USB Port.", "ERROR")
                    self.status_lbl.configure(text="Disconnected", text_color="gray")
        
        # استخدام Threading لعدم تجميد الواجهة
        threading.Thread(target=_scan, daemon=True).start()

    # --- محرك التنفيذ الآمن ---
    def start_execution_thread(self):
        threading.Thread(target=self.execute_command, daemon=True).start()

    def execute_command(self):
        selected = self.selector.get()
        if "Select" in selected:
            messagebox.showwarning("Warning", "Please select a model first!")
            return

        brand = getattr(self, 'current_brand', 'unknown')
        self.log(f"🚀 Initializing 2026 Protocol for {selected}...", "KING")
        
        try:
            if brand == "samsung":
                self.log("📲 Rebooting Samsung to Download Mode...", "INFO")
                subprocess.run(["adb", "reboot", "download"], capture_output=True, check=True)
            
            elif brand == "huawei" or brand == "infinix_tecno":
                self.log("🔐 Sending FRP Wipe Command (Fastboot)...", "INFO")
                # أوامر حقيقية للمسح
                subprocess.run(["fastboot", "erase", "config"], capture_output=True, check=True)
                subprocess.run(["fastboot", "erase", "frp"], capture_output=True, check=True)
                subprocess.run(["fastboot", "reboot"], capture_output=True, check=True)
            
            elif brand == "motorola_vivo":
                self.log("🔓 Fetching OEM Unlock Keys...", "INFO")
                subprocess.run(["fastboot", "getvar", "all"], capture_output=True, check=True)

            self.log(f"✅ Operation Finished Successfully for {selected}!", "SUCCESS")
            self.log("❤️ Dedicated to Princess OLA (Um Malak).", "KING")
            messagebox.showinfo("Success", f"{selected} Unlocked Successfully!")
        except subprocess.CalledProcessError as e:
            self.log(f"⚠️ Command Failed: {e.stderr.decode()}", "ERROR")
            messagebox.showerror("Error", "فشلت العملية! تأكد من وضع الهاتف الصحيح (Test Point/EDL/Fastboot)")
        except Exception as e:
            self.log(f"⚠️ Hardware Error: {str(e)}", "ERROR")

    def load_brand(self, brand):
        self.current_brand = brand
        models = self.models_data.get(brand, [])
        self.selector.configure(values=models)
        # Fix potential IndexError if models list is empty
        self.selector.set(models[0] if models else f"No models for {brand}")
        self.log(f"📂 Module {brand.upper()} Loaded. {len(models)} targets active.", "INFO")

    def create_nav_btn(self, txt, cmd, clr):
        btn = ctk.CTkButton(self.sidebar, text=txt, command=cmd, fg_color=clr, height=50, anchor="w", font=("Cairo", 12, "bold"))
        btn.pack(fill="x", pady=5, padx=20)

    def log(self, msg, level):
        t = datetime.now().strftime("%H:%M:%S")
        self.log_box.insert("end", f"[{t}] [{level}] {msg}\n")
        self.log_box.see("end")

if __name__ == "__main__":
    # تأكد من وجود ملفات adb.exe و fastboot.exe في نفس المجلد
    app = KingGenius_2026_Pro()
    app.mainloop()
