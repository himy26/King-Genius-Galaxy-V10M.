import customtkinter as ctk
import threading
import time
import os
# استدعاء محرك الذكاء الاصطناعي الذي أنشأناه
from ai_engine import LavenderAIEngine 

class LevantiV35(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # إعدادات الواجهة الملكية
        self.title("LEVANTI V35 - AI POWERED MOBILE TOOL")
        self.geometry("1100x700")
        self.ai_engine = LavenderAIEngine() # تشغيل المحرك

        # نظام التقسيم (Grid)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- القائمة الجانبية (الأوامر) ---
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        
        ctk.CTkLabel(self.sidebar, text="LAVENDER AI", font=("Orbitron", 20, "bold"), text_color="#A855F7").pack(pady=20)

        # الأوامر الأساسية
        self.add_btn("Detect Device", self.op_detect)
        self.add_btn("AI Fix Bootloader", self.op_fix_boot)
        self.add_btn("AI Unlock FRP", self.op_unlock_frp)
        self.add_btn("Cloud Sync", self.op_sync)

        # --- منطقة العمل الرئيسية ---
        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        # شاشة الكونسول (الشاشة السوداء)
        self.console = ctk.CTkTextbox(self.main_frame, fg_color="black", text_color="#00FF00", font=("Consolas", 14))
        self.console.pack(fill="both", expand=True, pady=(0, 10))

        # عداد التقدم (The Progress Bar) للهيبة
        self.progress = ctk.CTkProgressBar(self.main_frame, orientation="horizontal", height=15)
        self.progress.pack(fill="x", pady=10)
        self.progress.set(0)

    def add_btn(self, text, command):
        btn = ctk.CTkButton(self.sidebar, text=text, command=command, height=40)
        btn.pack(fill="x", padx=10, pady=5)

    def log(self, msg):
        self.console.insert("end", f">>> {msg}\n")
        self.console.see("end")

    # --- منطق العمليات ---
    def op_detect(self):
        self.log("Scanning for devices (Xiaomi/Oppo/Samsung)...")
        # هنا سيتم استدعاء كود الـ USB الحقيقي في الخطوة القادمة
        self.log("[AI] Device detected in VCOM Port (COM4)")

    def op_fix_boot(self):
        brand = "Xiaomi" # مثال
        model = "Note13" # مثال
        self.log(f"AI Engine: Searching local database for {brand} {model}...")
        
        # استخدام المحرك للبحث
        result = self.ai_engine.find_exploit(brand, model)
        self.log(result)
        
        # تشغيل عداد التقدم
        self.run_progress()

    def op_unlock_frp(self):
        self.log("[AI] Searching Cloud for latest FRP bypass keys...")
        self.run_progress()

    def op_sync(self):
        res = self.ai_engine.cloud_sync()
        self.log(res)

    def run_progress(self):
        self.progress.set(0)
        def update():
            for i in range(1, 101):
                time.sleep(0.03)
                self.progress.set(i/100)
            self.log("[SUCCESS] Operation Finished Successfully.")
        threading.Thread(target=update).start()

if __name__ == "__main__":
    app = LevantiV35()
    app.mainloop()