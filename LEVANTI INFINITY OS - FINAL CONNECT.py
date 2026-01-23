import customtkinter as ctk
from tkinter import messagebox
import mysql.connector

class LevantiOS:
    def __init__(self):
        self.db = None
        self.connect_to_db()

    def connect_to_db(self):
        try:
            # محاولة الربط مع قاعدة البيانات التي ستنشئها في XAMPP
            self.db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="levanti_db"
            )
            print("Connected to Levanti Server Successfully! ✅")
        except:
            print("Server not ready yet. Please start MySQL in XAMPP. ⚠️")

    def register_serial(self, serial_num):
        if not self.db:
            self.connect_to_db() # محاولة إعادة الاتصال
        
        if self.db:
            try:
                cursor = self.db.cursor()
                sql = "INSERT INTO serial_numbers (serial_number, status) VALUES (%s, %s)"
                val = (serial_num, "Authorized")
                cursor.execute(sql, val)
                self.db.commit()
                return True
            except Exception as e:
                print(f"Error saving: {e}")
                return False
        return False

# --- واجهة المستخدم الملكية ---
app = ctk.CTk()
app.title("LEVANTI INFINITY OS - V10M")
app.geometry("600x400")

levanti = LevantiOS()

def handle_registration():
    sn = entry_sn.get()
    if sn:
        success = levanti.register_serial(sn)
        if success:
            messagebox.showinfo("King Shadi", f"Serial {sn} Registered! 👑\n1 Token Deducted.")
        else:
            messagebox.showerror("Error", "Server Offline! Start XAMPP first.")
    else:
        messagebox.showwarning("Warning", "Please enter a Serial Number!")

# عناصر الواجهة
label = ctk.CTkLabel(app, text="iCloud Serial Registration", font=("Arial", 20, "bold"))
label.pack(pady=20)

entry_sn = ctk.CTkEntry(app, placeholder_text="Enter Apple Serial (SN)...", width=300)
entry_sn.pack(pady=20)

btn = ctk.CTkButton(app, text="Register & Deduct Token", fg_color="darkred", command=handle_registration)
btn.pack(pady=20)

app.mainloop()