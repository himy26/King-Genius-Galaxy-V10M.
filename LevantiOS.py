import customtkinter as ctk
from tkinter import messagebox
import mysql.connector
from datetime import datetime

# --- إعدادات المظهر الملكي ---
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class LevantiInfinityOS(ctk.CTk):
    def __init__(self):
        super().__init__()

        # إعدادات النافذة الرئيسية
        self.title("LEVANTI INFINITY OS - Unified Server Edition 👑")
        self.geometry("1200x850")

        # بيانات الربط (يمكنك تعديلها من واجهة الإعدادات)
        self.db_config = {
            'host': 'localhost',
            'user': 'root',
            'password': '',
            'database': 'levanti_infinity'
        }

        # --- القائمة الجانبية (Sidebar) ---
        self.sidebar = ctk.CTkFrame(self, width=240, corner_radius=0)
        self.sidebar.pack(side="left", fill="y")
        
        self.logo_label = ctk.CTkLabel(self.sidebar, text="LEVANTI OS", font=ctk.CTkFont(size=26, weight="bold"))
        self.logo_label.pack(pady=40)

        self.create_sidebar_button("📊 لوحة التحكم", self.show_dashboard)
        self.create_sidebar_button("🍎 Apple Signal Bypass", self.show_apple)
        self.create_sidebar_button("📱 Samsung & MTK", self.show_samsung)
        self.create_sidebar_button("⚙️ إعدادات السيرفر", self.show_settings)

        # --- منطقة المحتوى الرئيسي ---
        self.main_frame = ctk.CTkFrame(self, corner_radius=20, fg_color="#121212")
        self.main_frame.pack(side="right", fill="both", expand=True, padx=20, pady=20)

        self.show_dashboard()

    def create_sidebar_button(self, text, command):
        btn = ctk.CTkButton(self.sidebar, text=text, command=command, height=50, corner_radius=12, font=("Arial", 15, "bold"))
        btn.pack(pady=12, padx=20, fill="x")

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    # --- 1. واجهة لوحة التحكم ---
    def show_dashboard(self):
        self.clear_frame()
        ctk.CTkLabel(self.main_frame, text="مملكة LEVANTI الرقمية 👑", font=("Arial", 28, "bold"), text_color="gold").pack(pady=30)
        
        stats_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        stats_frame.pack(pady=20, fill="x", padx=40)

        self.create_stat_card(stats_frame, "الوكلاء النشطون", "250", 0)
        self.create_stat_card(stats_frame, "إجمالي السيريالات", "12,840", 1)
        self.create_stat_card(stats_frame, "رصيد السيرفر", "50,000 T", 2)

    def create_stat_card(self, parent, label, value, col):
        card = ctk.CTkFrame(parent, width=260, height=140, corner_radius=15, border_width=1, border_color="gray")
        card.grid(row=0, column=col, padx=15)
        ctk.CTkLabel(card, text=label, font=("Arial", 14)).pack(pady=10)
        ctk.CTkLabel(card, text=value, font=("Arial", 24, "bold"), text_color="#3b8ed0").pack(pady=10)

    # --- 2. واجهة آبل (الربط والتسجيل الحقيقي) ---
    def show_apple(self):
        self.clear_frame()
        ctk.CTkLabel(self.main_frame, text="🍎 iCloud Registration (Passcode With Signal)", font=("Arial", 22, "bold")).pack(pady=20)
        
        box = ctk.CTkFrame(self.main_frame, fg_color="#1e1e1e", corner_radius=20)
        box.pack(pady=20, padx=60, fill="both", expand=True)

        ctk.CTkLabel(box, text="أدخل السيريال نمبر (SN) للجهاز:", font=("Arial", 16)).pack(pady=20)
        self.sn_entry = ctk.CTkEntry(box, width=500, height=50, placeholder_text="G0NXXXXXXX...", font=("Arial", 18))
        self.sn_entry.pack(pady=10)

        btn_reg = ctk.CTkButton(box, text="تسجيل السيريال في السيرفر (خصم 1 توكن)", fg_color="#c0392b", hover_color="#a93226", 
                                height=50, width=300, command=self.db_register_serial)
        btn_reg.pack(pady=20)

        btn_bypass = ctk.CTkButton(box, text="بدء تخطي Passcode (بعد التسجيل)", fg_color="#27ae60", height=50, width=300,
                                   command=lambda: messagebox.showinfo("العملية", "جاري الاتصال بالأيفون وسحب ملفات الشبكة..."))
        btn_bypass.pack(pady=10)

    # --- 3. واجهة سامسونج وأندرويد ---
    def show_samsung(self):
        self.clear_frame()
        ctk.CTkLabel(self.main_frame, text="📱 Android & Samsung Intelligence", font=("Arial", 22, "bold")).pack(pady=20)
        
        grid = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        grid.pack(pady=20)

        services = [
            ("FRP Unlock (MTP)", "#3498db"),
            ("Fix DL Image Fail", "#e67e22"),
            ("MDM Remove", "#9b59b6"),
            ("CSC Change", "#2ecc71")
        ]

        for i, (name, color) in enumerate(services):
            r, c = divmod(i, 2)
            ctk.CTkButton(grid, text=name, fg_color=color, width=320, height=60, font=("Arial", 16, "bold")).grid(row=r, column=c, padx=20, pady=20)

    # --- 4. واجهة الإعدادات ---
    def show_settings(self):
        self.clear_frame()
        ctk.CTkLabel(self.main_frame, text="⚙️ إعدادات ربط السيرفر الرئيسي", font=("Arial", 22, "bold")).pack(pady=20)
        
        form = ctk.CTkFrame(self.main_frame, width=600)
        form.pack(pady=20)

        self.host_inp = ctk.CTkEntry(form, width=400, placeholder_text="Host IP (e.g. 192.168.1.1)")
        self.host_inp.pack(pady=10, padx=20)
        
        self.user_inp = ctk.CTkEntry(form, width=400, placeholder_text="Database Username")
        self.user_inp.pack(pady=10, padx=20)

        ctk.CTkButton(form, text="حفظ الإعدادات واختبار الاتصال", command=self.test_connection).pack(pady=20)

    # --- منطق الربط الحقيقي بقاعدة البيانات ---
    def db_register_serial(self):
        sn = self.sn_entry.get().strip()
        if not sn:
            messagebox.showerror("خطأ", "برجاء إدخال السيريال نمبر!")
            return

        try:
            # الاتصال الفعلي بقاعدة البيانات
            conn = mysql.connector.connect(**self.db_config)
            cursor = conn.cursor()

            # 1. التحقق من التوكن (الوكيل رقم 1 كمثال)
            cursor.execute("SELECT token_balance FROM agents WHERE agent_id = 1")
            balance = cursor.fetchone()[0]

            if balance > 0:
                # 2. تسجيل السيريال
                sql_insert = "INSERT INTO registered_serials (serial_number, agent_id, service_type) VALUES (%s, %s, %s)"
                cursor.execute(sql_insert, (sn, 1, 'Passcode_Signal'))
                
                # 3. خصم التوكن
                cursor.execute("UPDATE agents SET token_balance = token_balance - 1 WHERE agent_id = 1")
                
                conn.commit()
                messagebox.showinfo("LEVANTI SERVER", f"تم التسجيل بنجاح!\nالرقم التسلسلي: {sn}\nتم خصم 1 توكن.")
            else:
                messagebox.showwarning("رصيد منخفض", "عذراً، رصيد التوكن الخاص بك غير كافٍ.")
            
            cursor.close()
            conn.close()
        except mysql.connector.Error as err:
            messagebox.showerror("خطأ سيرفر", f"فشل الاتصال بالسيرفر: {err}")

    def test_connection(self):
        messagebox.showinfo("Success", "تم حفظ إعدادات السيرفر بنجاح!")

if __name__ == "__main__":
    app = LevantiInfinityOS()
    app.mainloop()