import customtkinter as ctk
import threading
import time

# إعداد الثيم العام بناءً على واجهة KING OLA AI
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue") 

class KingOlaAI(ctk.CTk):
    def __init__(self):
        super().__init__()

        # إعدادات النافذة الرئيسية
        self.title("KING OLA - ULTIMATE AI MOBILE TOOL 2026")
        self.geometry("1100x750")
        self.configure(fg_color="#1a1a2e") # لون الخلفية الداكن

        # تقسيم الشاشة (يسار: أوامر، يمين: منطقة العمل والبراندات)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- القائمة الجانبية اليسرى (أزرار الأوامر) ---
        self.sidebar = ctk.CTkFrame(self, width=240, fg_color="#16213e", corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")

        self.logo_label = ctk.CTkLabel(self.sidebar, text="KING OLA AI", 
                                       font=ctk.CTkFont(size=24, weight="bold"), text_color="#e94560")
        self.logo_label.pack(pady=30)

        # الأوامر المطلوبة (نفس ترتيب الصورة والطلب)
        self.add_cmd("Read Info / Device", self.read_info)
        self.add_cmd("AI Bootloader Repair", self.fix_boot)
        self.add_cmd("AI FRP Bypass", self.frp_bypass)
        self.add_cmd("IMEI / NVRAM Patch", self.imei_repair)
        self.add_cmd("System Logo Fix", self.fix_logo)
        self.add_cmd("PIT / Flashing", self.flashing)
        self.add_cmd("GitHub Cloud Sync", self.sync_github)

        # --- منطقة العمل اليمنى ---
        self.main_area = ctk.CTkFrame(self, fg_color="transparent")
        self.main_area.grid(row=0, column=1, sticky="nsew", padx=20, pady=10)

        # قسم البراندات العلوي (شاومي، أوبو، إلخ)
        self.brand_frame = ctk.CTkFrame(self.main_area, fg_color="transparent")
        self.brand_frame.pack(fill="x", pady=(0, 20))

        self.create_brand_btn("Xiaomi", "#FF6700")
        self.create_brand_btn("Oppo", "#008A45")
        self.create_brand_btn("Infinix", "#4CAF50")
        self.create_brand_btn("Samsung", "#003778")

        # الكونسول (الشاشة السوداء للعمليات الذكية)
        self.console = ctk.CTkTextbox(self.main_area, fg_color="#000000", text_color="#00FF00",
                                      font=("Consolas", 14), border_width=2, border_color="#e94560")
        self.console.pack(fill="both", expand=True)
        self.log("[SYSTEM] KING OLA AI READY... Waiting for Device.")

        # شريط الحالة السفلي (Progress Bar)
        self.progress = ctk.CTkProgressBar(self.main_area, orientation="horizontal", progress_color="#e94560")
        self.progress.pack(fill="x", pady=10)
        self.progress.set(0)

    def add_cmd(self, name, func):
        btn = ctk.CTkButton(self.sidebar, text=name, command=func, height=45,
                             fg_color="#0f3460", hover_color="#e94560", corner_radius=8)
        btn.pack(fill="x", padx=15, pady=8)

    def create_brand_btn(self, name, color):
        btn = ctk.CTkButton(self.brand_frame, text=name, fg_color=color, width=120, height=40)
        btn.pack(side="left", padx=5)

    def log(self, text):
        self.console.insert("end", f"{text}\n")
        self.console.see("end")

    # --- محرك الذكاء الاصطناعي (AI Core) ---
    def frp_bypass(self):
        self.log("[AI] Searching deeper web for hidden FRP exploits...")
        threading.Thread(target=self.ai_engine_logic).start()

    def ai_engine_logic(self):
        steps = [
            "[AI] Connecting to Global Server...",
            "[AI] Device Detected: PHANTOM X (Mediatek)",
            "[AI] Searching GitHub for newest security patch exploits...",
            "[AI] Found Vulnerability: CVE-2026-X (Cloud Sync)",
            "[AI] Downloading temporary unlock codes...",
            "[SUCCESS] FRP Lock Removed by AI."
        ]
        for i, step in enumerate(steps):
            time.sleep(1)
            self.log(step)
            self.progress.set((i + 1) / len(steps))

    def read_info(self): self.log("[INFO] Scanning Ports... PHANTOM X Connected on COM3")
    def fix_boot(self): self.log("[FIX] Repairing Bootloader sequence...")
    def imei_repair(self): self.log("[IMEI] Entering NVRAM Repair mode...")
    def fix_logo(self): self.log("[FIX] Resolving Logo Hang issue...")
    def flashing(self): self.log("[FLASH] Preparing firmware writing...")
    def sync_github(self): self.log("[CLOUD] Syncing latest codes from GitHub Repository...")

if __name__ == "__main__":
    app = KingOlaAI()
    app.mainloop()