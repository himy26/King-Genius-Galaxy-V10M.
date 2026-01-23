import customtkinter as ctk
from tkinter import messagebox
import mysql.connector
from datetime import datetime

# إعدادات الواجهة الاحترافية
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class LevantiInfinityOS(ctk.CTk):
    def __init__(self):
        super().__init__()

        # إعدادات النافذة
        self.title("LEVANTI INFINITY OS - Main Control Panel 👑")
        self.geometry("1100x750")

        # --- القائمة الجانبية (Sidebar) ---
        self.sidebar = ctk.CTkFrame(self, width=220, corner_radius=0)
        self.sidebar.pack(side="left", fill="y")
        
        self.logo_label = ctk.CTkLabel(self.sidebar, text="LEVANTI INFINITY", font=ctk.CTkFont(size=20, weight="bold", color="gold"))
        self.logo_label.pack(pady=30)

        self.btn_dash = ctk.CTkButton(self.sidebar, text="🏠 Dashboard", command=self.show_dashboard, fg_color="transparent", anchor="w")
        self.btn_dash.pack(pady=5, padx=20, fill="x")

        self.btn_apple = ctk.CTkButton(self.sidebar, text="🍎 Apple Bypass", command=self.show_apple, fg_color="transparent", anchor="w")
        self.btn_apple.pack(pady=5, padx=20, fill="x")

        self.btn_android = ctk.CTkButton(self.sidebar, text="🤖 Android Tools", command=self.show_android, fg_color="transparent", anchor="w")
        self.btn_android.pack(pady=5, padx=20, fill="x")

        # --- المنطقة الرئيسية (Main View) ---
        self.main_view = ctk.CTkFrame(self, corner_radius=20, fg_color="#1a1a1a")
        self.main_view.pack(side="right", fill="both", expand=True, padx=20, pady=20)

        self.show_dashboard()

    # دالة الربط بقاعدتك (الموجودة في الصور)
    def db_connect(self):
        try:
            return mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="levanti_db"
            )
        except:
            messagebox.showerror("Server Error", "تأكد من تشغيل MySQL في XAMPP ❌")
            return None

    def show_dashboard(self):
        self.clear_main()
        ctk.CTkLabel(self.main_view, text="نظام ليفانتي إنفينيتي - لوحة التحكم 👑", font=("Arial", 26, "bold")).pack(pady=30)
        
        info_frame = ctk.CTkFrame(self.main_view, fg_color="#2b2b2b")
        info_frame.pack(pady=20, padx=50, fill="x")
        
        ctk.CTkLabel(info_frame, text="عدد الفروع: 250 فرع نشط ✅", font=("Arial", 16)).pack(pady=10)
        ctk.CTkLabel(info_frame, text="حالة السيرفر: متصل (LocalHost) 🟢", text_color="green").pack(pady=10)

    def show_apple(self):
        self.clear_main()
        ctk.CTkLabel(self.main_view, text="تسجيل وتخطي أجهزة الأيفون 🍎", font=("Arial", 22)).pack(pady=20)

        # خانة إدخال السيريال (مثل FCDT91QJHFYC)
        self.sn_input = ctk.CTkEntry(self.main_view, placeholder_text="أدخل سيريال الأيفون هنا...", width=450, height=45)
        self.sn_input.pack(pady=10)

        # الأزرار
        btn_reg = ctk.CTkButton(self.main_view, text="تسجيل السيريال (خصم 1 توكن) 💎", fg_color="#d32f2f", hover_color="#b71c1c", height=50, command=self.register_to_db)
        btn_reg.pack(pady=10)

        btn_check = ctk.CTkButton(self.main_view, text="فحص حالة السيريال في قاعدة البيانات 🔍", command=self.check_sn)
        btn_check.pack(pady=10)

    def show_android(self):
        self.clear_main()
        ctk.CTkLabel(self.main_view, text="أدوات الأندرويد و FRP 📱", font=("Arial", 22)).pack(pady=20)
        ctk.CTkButton(self.main_view, text="Fix DL Image Error (Tecno)", fg_color="orange", width=250).pack(pady=10)
        ctk.CTkButton(self.main_view, text="Direct Unlock Samsung", width=250).pack(pady=10)

    def register_to_db(self):
        sn = self.sn_input.get().strip()
        if not sn:
            messagebox.showwarning("تنبيه", "أدخل السيريال أولاً يا ملكي!")
            return

        conn = self.db_connect()
        if conn:
            cursor = conn.cursor()
            try:
                # الكود الذي يكتب السيريال في جدولك الذي ظهر بالصور
                sql = "INSERT INTO serial_numbers (serial_number, status) VALUES (%s, %s)"
                cursor.execute(sql, (sn, 'Authorized_Apple'))
                conn.commit()
                messagebox.showinfo("نجاح ✅", f"تم تسجيل السيريال {sn} بنجاح في قاعدة بيانات ليفانتي!")
            except Exception as e:
                messagebox.showerror("خطأ", f"السيريال مسجل مسبقاً أو هناك مشكلة: {e}")
            finally:
                conn.close()

    def check_sn(self):
        sn = self.sn_input.get().strip()
        conn = self.db_connect()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT status, registration_date FROM serial_numbers WHERE serial_number = %s", (sn,))
            res = cursor.fetchone()
            if res:
                messagebox.showinfo("حالة الجهاز", f"الجهاز: {sn}\nالحالة: {res[0]}\nتاريخ التسجيل: {res[1]}")
            else:
                messagebox.showwarning("غير موجود", "هذا السيريال غير مسجل لدينا.")
            conn.close()

    def clear_main(self):
        for widget in self.main_view.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = LevantiInfinityOS()
    app.mainloop()