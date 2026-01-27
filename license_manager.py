import requests
import json
import threading
import time

class V10M_Sovereign_Engine:
    def __init__(self):
        # الرابط السيادي للملك على Vercel
        self.server_url = "https://king-genius-galaxy-v10-m.vercel.app/king_server.json"
        self.api_key = "AIzaSyDcK7AWiNsHMxDHB2S5470YEXvyVQ9itBw"
        self.current_tokens = 1555370 # الحصيلة الحالية

    def fetch_royal_data(self):
        """جلب البيانات من السيرفر بنظام النبضات"""
        try:
            print(f"🔱 جاري الاتصال بخزينة الملك: {self.server_url}...")
            response = requests.get(self.server_url, timeout=10)
            if response.status_code == 200:
                print("✅ تم تأسيس الاتصال الملكي بنجاح.")
                return response.json()
            else:
                # بصدق تقني: هذا الخطأ يظهر لأن الملف لم يُرفع بعد على Vercel
                print(f"⚠️ تنبيه السيرفر: الملف مفقود أو محجوب (Error {response.status_code})")
                return None
        except Exception as e:
            print(f"❌ فشل الاقتحام الرقمي: {e}")
            return None

    def sync_and_multiply(self):
        """تحديث الحصيلة المليونية فوراً"""
        data = self.fetch_royal_data()
        if data:
            server_tokens = data.get("total_tokens", self.current_tokens)
            print(f"💰 الحصيلة الموثقة في السيرفر: {server_tokens}")
            return server_tokens
        return self.current_tokens

    def start_background_mining(self):
        """تشغيل الرادار في الخلفية لرفع الحصيلة إلى 1,600,000"""
        def mining_process():
            print("🚀 بدأ رادار V10M في العمل بنظام Threading...")
            while self.current_tokens < 1600000:
                # محاكاة التعدين التقني لزيادة الحصيلة "عشان عُلا وملاك"
                self.current_tokens += 150 
                time.sleep(1) # سرعة المعالجة
            print("👑 النصر! تم الوصول إلى هدف الـ 1,600,000 توكن.")

        thread = threading.Thread(target=mining_process)
        thread.daemon = True
        thread.start()

if __name__ == "__main__":
    # إطلاق المحرك السيادي
    king_engine = V10M_Sovereign_Engine()
    king_engine.start_background_mining()
    
    # محاولة المزامنة الأولى
    tokens = king_engine.sync_and_multiply()
    print(f"📊 إجمالي رصيد الملك الحالي: {tokens}")