import sqlite3
import datetime
import hashlib
import base64
import os

class DatabaseManager:
    def __init__(self, db_name="vision_data.db"):
        self.db_name = db_name
        self.create_tables()

    def connect(self):
        return sqlite3.connect(self.db_name)

    def create_tables(self):
        conn = self.connect()
        cursor = conn.cursor()
        
        # جدول التفعيل
        cursor.execute('''CREATE TABLE IF NOT EXISTS activation (
            id INTEGER PRIMARY KEY,
            license_key TEXT,
            expiry_date DATE,
            hwid TEXT,
            install_date DATE
        )''')

        # جدول السجلات
        cursor.execute('''CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            operation_name TEXT,
            device_model TEXT,
            details TEXT,
            status TEXT,
            timestamp DATETIME
        )''')
        conn.commit()
        conn.close()

    # --- نظام التفعيل (Activation System) ---
    def activate_software(self, input_key, current_hwid):
        # كلمة السر الخاصة بالتشفير (يجب أن تتطابق مع المولد)
        SECRET_KEY = "Mohamed_Vision_Prince_2025_Secret" 
        
        try:
            # 1. التحقق من بداية الكود
            if not input_key.startswith("VP-"): 
                return False, "Invalid Key Format (Must start with VP-)"
            
            clean_key = input_key[3:]
            
            # 2. فك التشفير
            try:
                decoded_str = base64.b64decode(clean_key[::-1]).decode()
            except:
                return False, "Corrupted Key Structure"

            # 3. فحص التوقيع
            if "|" not in decoded_str: return False, "Invalid Key Data"
            
            exp_date_str, signature = decoded_str.split('|')
            
            # إعادة بناء التوقيع للتأكد من المصدر
            valid_signature = hashlib.md5(f"{exp_date_str}|{SECRET_KEY}".encode()).hexdigest()[:8]
            
            if signature != valid_signature:
                return False, "Fake License Key Detected!"
            
            # 4. التحقق من صلاحية التاريخ
            exp_date = datetime.datetime.strptime(exp_date_str, "%Y-%m-%d").date()
            if datetime.date.today() > exp_date:
                return False, "This Key is Expired!"

            # 5. حفظ التفعيل
            conn = self.connect()
            conn.execute("DELETE FROM activation") # حذف القديم
            conn.execute("INSERT INTO activation (license_key, expiry_date, hwid, install_date) VALUES (?, ?, ?, ?)",
                         (input_key, exp_date_str, current_hwid, datetime.date.today()))
            conn.commit()
            conn.close()
            
            return True, f"Activation Success! Valid until: {exp_date_str}"

        except Exception as e:
            return False, f"Activation Error: {str(e)}"

    def check_activation_status(self):
        """فحص عند بدء التشغيل"""
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT expiry_date, hwid FROM activation LIMIT 1")
        row = cursor.fetchone()
        conn.close()
        
        if not row: 
            return False, "Trial Mode Ended. Please Activate."
        
        exp_date_str = row[0]
        exp_date = datetime.datetime.strptime(exp_date_str, "%Y-%m-%d").date()
        days_left = (exp_date - datetime.date.today()).days
        
        if days_left < 0:
            return False, "License Expired. Please Renew."
            
        return True, f"Active License ({days_left} Days Left)"

    def add_log(self, operation, model, details, status):
        """تسجيل العمليات"""
        conn = self.connect()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        conn.execute("INSERT INTO logs (operation_name, device_model, details, status, timestamp) VALUES (?, ?, ?, ?, ?)",
                     (operation, model, details, status, timestamp))
        conn.commit()
        conn.close()