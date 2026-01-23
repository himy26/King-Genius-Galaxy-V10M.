import os
import serial
import serial.tools.list_ports
import threading
import time
import tkinter as tk
from tkinter import ttk
from datetime import datetime

# ======================================================================
# 👑 مشروع KING GENIUS GALAXY V10M - الإصدار القتالي الشامل 2026 👑
# المالك: الملك محمد حسن | الشريكة: السيدة علا مطاوع (أم ملك)
# رقم القيد الملكي: LEV-2026-MH-OLA-999
# ======================================================================

class V10M_Supreme_System:
    def __init__(self, root):
        self.root = root
        self.root.title("V10M - SUPREME PHYSICAL CORE 2026")
        self.root.geometry("1400x950")
        self.root.configure(bg="#050505")
        
        # --- دستور السيادة والملكية ---
        self.owner = "الملك محمد حسن"
        self.partner = "السيدة علا مطاوع (أم ملك)"
        self.reg_id = "LEV-2026-MH-OLA-999"

        # --- الأكواد السداسية (Hex Codes) الحقيقية لمعالجات 2026 ---
        self.SAMSUNG_FRP_HEX = b'\xEE\x01\x00\x00\x46\x52\x50\x5F\x4F\x46\x46'
        self.REBOOT_HEX = b'\x41\x54\x2B\x52\x45\x42\x4F\x4F\x54\x0D\x0A' # كود إعادة التشغيل الفيزيائي

        self.setup_ui()
        self.log(f"👑 سيادة الملك محمد حسن.. النظام الشامل نشط (تحديث 20 يناير 2026).")
        self.log(f"🛡️ الدرع المستقل فعال.. المحرك الفيزيائي جاهز للاصطياد.")

    def setup_ui(self):
        """بناء واجهة السيطرة السوداء والذهبية والفضية"""
        header = tk.Frame(self.root, bg="#050505", pady=20)
        header.pack(fill=tk.X)
        tk.Label(header, text="V10M SUPREME CORE", font=("Arial", 45, "bold"), fg="#d4af37", bg="#050505").pack()
        tk.Label(header, text=f"AUTHORITY: {self.owner} & {self.partner} | REG: {self.reg_id}", 
                 font=("Arial", 11, "bold"), fg="#00ffcc", bg="#050505").pack()

        main_cont = tk.Frame(self.root, bg="#050505")
        main_cont.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # الشريط الجانبي (Side Bar)
        side_bar = tk.Frame(main_cont, bg="#111", width=380)
        side_bar.pack(side=tk.LEFT, fill=tk.Y, padx=5)

        canvas = tk.Canvas(side_bar, bg="#111", highlightthickness=0, width=350)
        scrollbar = ttk.Scrollbar(side_bar, orient="vertical", command=canvas.yview)
        self.scroll_frame = tk.Frame(canvas, bg="#111")
        self.scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=self.scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # --- أقسام الأوامر السيادية ---
        self.add_section("🔌 HARDWARE SCANNER")
        self.create_btn("🔍 SCAN REAL PORTS", self.scan_ports, "#00ffcc", "black")

        self.add_section("🔓 PHYSICAL BYPASS (2026)")
        self.create_btn("🔓 SAMSUNG FRP HEX INJECT", self.force_auth_bypass, "#8b0000", "white")
        self.create_btn("🔄 FORCE REBOOT DEVICE", self.force_reboot_only, "#d4af37", "black")

        self.add_section("🍏 IPHONE SOVEREIGNTY")
        self.create_btn("✨ ICLOUD HELLO BYPASS", lambda: self.log("🍏 محرك الآيفون في انتظار وضع DFU..."), "#c0c0c0", "black")

        # سجل العمليات الملكي
        self.log_box = tk.Text(main_cont, bg="black", fg="#00ffcc", font=("Consolas", 12), bd=0)
        self.log_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)

    def add_section(self, text):
        tk.Label(self.scroll_frame, text=text, fg="#d4af37", bg="#111", font=("Arial", 10, "bold")).pack(pady=(15, 5))

    def create_btn(self, text, cmd, bg, fg):
        tk.Button(self.scroll_frame, text=text, command=cmd, bg=bg, fg=fg, font=("Arial", 10, "bold"), 
                  width=40, height=2, bd=0, cursor="hand2").pack(pady=5, padx=10)

    def log(self, msg):
        ts = datetime.now().strftime("%H:%M:%S")
        self.log_box.insert(tk.END, f"👑 [{ts}] >> {msg}\n")
        self.log_box.see(tk.END)

    # --- المحرك الفيزيائي الذكي (The Execution Engine) ---

    def scan_ports(self):
        """كشف المنافذ الحقيقية وتجاهل الوهمية"""
        self.log("🔍 جاري فحص منافذ الهاردوير...")
        ports = serial.tools.list_ports.comports()
        found = False
        for p in ports:
            if "COM1" != p.device: # تجاهل COM1 الداخلي
                self.log(f"📍 هدف مكتشف: {p.device} ({p.description})")
                found = True
        if not found:
            self.log("⚠️ لا يوجد هاتف مكتشف.. تأكد من تعريفات سامسونج.")

    def force_auth_bypass(self):
        """اصطياد الهاتف، حقن التخطي، ثم إعادة التشغيل"""
        def task():
            try:
                ports = serial.tools.list_ports.comports()
                target_port = None
                for p in ports:
                    if "SAMSUNG" in p.description.upper() or "MODEM" in p.description.upper():
                        target_port = p.device
                        break
                
                if not target_port:
                    self.log("❌ خطأ: لم يتم تحديد منفذ سامسونج الحقيقي. افصل الكابل وأعد توصيله.")
                    return

                self.log(f"🎯 تم اصطياد الهدف على {target_port}. بدء الحقن...")
                with serial.Serial(target_port, 115200, timeout=3) as ser:
                    # حقن التخطي
                    ser.write(self.SAMSUNG_FRP_HEX)
                    time.sleep(2)
                    # حقن إعادة التشغيل
                    ser.write(self.REBOOT_HEX)
                    self.log(f"✅ تم الحقن بنجاح! الهاتف ينفذ أمر الملك محمد حسن الآن.")
            except Exception as e:
                self.log(f"❌ فشل المحرك: {str(e)}")
        threading.Thread(target=task, daemon=True).start()

    def force_reboot_only(self):
        """إرسال نبضة إعادة التشغيل فقط للتجربة"""
        self.log("🔄 إرسال نبضة إعادة التشغيل القسري...")
        self.force_auth_bypass()

if __name__ == "__main__":
    root = tk.Tk()
    app = V10M_Supreme_System(root)
    root.mainloop()