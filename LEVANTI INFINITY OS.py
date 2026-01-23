import customtkinter as ctk
from tkinter import messagebox
import mysql.connector # تأكد من تنصيبها عبر pip install mysql-connector-python

# --- إعدادات المظهر الملكي ---
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class LevantiInfinityOS(ctk.CTk):
    def __init__(self):
        super().__init__()

        # إعدادات النافذة الرئيسية
        self.title("LEVANTI INFINITY OS - Pro Edition 2026 👑")
        self.geometry("1200x800")

        # --- القائمة الجانبية (Sidebar) ---
        self.sidebar = ctk.CTkFrame(self, width=220, corner_radius=0)
        self.sidebar.pack(side="left", fill="y")
        
        self.logo_label = ctk.CTkLabel(self.sidebar, text="LEVANTI INFINITY", font=ctk.CTkFont(size=22, weight="bold", family="Orbitron"))
        self.logo_label.pack(pady=30)

        # أزرار التنقل
        self.btn_dash = self.create_sidebar_button("لوحة التحكم", self.show_dashboard)
        self.btn_apple = self.create_sidebar_button("Apple (iCloud)", self.show_apple)
        self.btn_samsung = self.create_sidebar_button("Samsung/Android", self.show_samsung)
        self.btn_settings = self.create_sidebar_button("إعدادات السيرفر", self.show_settings)

        # --- محتوى العرض الرئيسي ---
        self.main_frame = ctk.CTkFrame(self, corner_radius=20, fg_color="#1a1a1a")
        self.main_frame.pack(side="right", fill="both", expand=True, padx=20, pady=20)

        self.show_dashboard()

    def create_sidebar_button(self, text, command):
        btn = ctk.CTkButton(self.sidebar, text=text, command=command, height=45, corner_radius=10, font=("Arial", 14))
        btn.pack(pady=10, padx=20, fill="x")
        return btn

    def clear_main_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    # --- 1. واجهة لوحة التحكم ---
    def show_dashboard(self):
        self.clear_main_frame()
        title = ctk.CTkLabel(self.main_frame, text="مرحباً بك يا ملك شادي - حالة السيرفر الآن", font=("Arial", 24, "bold"))
        title.pack(pady=30)

        info_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        info_frame.pack(pady=20, fill="x", padx=50)

        # كروت المعلومات (Stats)
        self.create_stat_card(info_frame, "الوكلاء النشطون", "250", 0)
        self.create_stat_card(info_frame, "التوكن المتوفر", "15,400", 1)
        self.create_stat_card(info_frame, "حالة الربط", "ONLINE ✅", 2)

    def create_stat_card(self, parent, label, value, col):
        card = ctk.CTkFrame(parent, width=250, height=150, corner_radius=15, border_width=2, border_color="#3b3b3b")
        card.grid(row=0, column=col, padx=15, pady=10)
        ctk.CTkLabel(card, text=label, font=("Arial", 14)).pack(pady=10)
        ctk.CTkLabel(card, text=value, font=("Arial", 22, "bold"), text_color="gold").pack(pady=10)

    # --- 2. واجهة آبل (تسجيل وتخطي) ---
    def show_apple(self):
        self.clear_main_frame()
        ctk.CTkLabel(self.main_frame, text="🍎 iCloud Bypass & Serial Registration", font=("Arial", 22, "bold")).pack(pady=20)
        
        container = ctk.CTkFrame(self.main_frame, fg_color="#2b2b2b", corner_radius=15)
        container.pack(pady=20, padx=50, fill="both", expand=True)

        ctk.CTkLabel(container, text="أدخل الرقم التسلسلي (Serial Number):").pack(pady=10)
        self.sn_input = ctk.CTkEntry(container, width=450, height=45, placeholder_text="Ex: G0NXXXXXXX")
        self.sn_input.pack(pady=10)

        # أزرار العمليات
        ctk.CTkButton(container, text="تسجيل السيريال (خصم توكن)", fg_color="#800000", hover_color="#600000", 
                      command=self.server_register_action).pack(pady=15)
        
        ctk.CTkButton(container, text="بدء التخطي (Passcode With Signal)", fg_color="#2ecc71", text_color="black",
                      command=lambda: messagebox.showinfo("العملية", "بدأت عملية سحب ملفات الشبكة...")).pack(pady=10)

    # --- 3. واجهة سامسونج وأندرويد ---
    def show_samsung(self):
        self.clear_main_frame()
        ctk.CTkLabel(self.main_frame, text="📱 Samsung & Android Intelligence", font=("Arial", 22, "bold")).pack(pady=20)
        
        btns_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        btns_frame.pack(pady=20)

        ctk.CTkButton(btns_frame, text="Unlock FRP (Direct MTP)", width=300, height=50).grid(row=0, column=0, padx=10, pady=10)
        ctk.CTkButton(btns_frame, text="Fix DL Image Error", width=300, height=50, fg_color="orange").grid(row=0, column=1, padx=10, pady=10)
        ctk.CTkButton(btns_frame, text="Remove MDM Lock", width=300, height=50).grid(row=1, column=0, padx=10, pady=10)
        ctk.CTkButton(btns_frame, text="Factory Reset (Safe)", width=300, height=50).grid(row=1, column=1, padx=10, pady=10)

    # --- 4. إعدادات السيرفر (قاعدة البيانات) ---
    def show_settings(self):
        self.clear_main_frame()
        ctk.CTkLabel(self.main_frame, text="⚙️ إعدادات ربط السيرفر و MySQL", font=("Arial", 22, "bold")).pack(pady=20)
        
        form = ctk.CTkFrame(self.main_frame)
        form.pack(pady=10, padx=50, fill="x")

        self.db_host = ctk.CTkEntry(form, placeholder_text="Server IP (Host)")
        self.db_host.pack(pady=5, padx=20, fill="x")
        
        self.db_user = ctk.CTkEntry(form, placeholder_text="Database User")
        self.db_user.pack(pady=5, padx=20, fill="x")

        ctk.CTkButton(form, text="حفظ إعدادات الربط", command=lambda: messagebox.showinfo("Saved", "تم حفظ بيانات السيرفر")).pack(pady=20)

    # --- منطق الربط الفني (Logic) ---
    def server_register_action(self):
        sn = self.sn_input.get()
        if not sn:
            messagebox.showerror("خطأ", "يرجى إدخال السيريال أولاً!")
            return
        
        # هنا يتم استدعاء دالة MySQL التي شرحتها لك سابقاً
        # للتجربة الآن سنظهر رسالة نجاح
        messagebox.showinfo("LEVANTI Server", f"تم تسجيل السيريال {sn} بنجاح!\nتم خصم 1 توكن من رصيد الوكيل.")

if __name__ == "__main__":
    app = LevantiInfinityOS()
    app.mainloop()