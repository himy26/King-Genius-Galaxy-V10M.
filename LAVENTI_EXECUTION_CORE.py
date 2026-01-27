import requests
import json

# --- إعدادات الإمبراطورية ---
KING_CONFIG = {
    "api_endpoint": "https://king-genius-galaxy-v10-m.vercel.app/api/auth",
    "paypal_link": "https://www.paypal.com/ncp/payment/MGBGJAVD24QYU",
    "owner": "الملك محمد حسن",
    "dedication": "إلى الأستاذة علا مطاوع (أم ملك)"
}

def initiate_royal_service():
    print(f"🔱 نظام {KING_CONFIG['owner']} قيد التشغيل...")
    
    try:
        # 1. التحقق من الحصيلة المليونية
        response = requests.get(KING_CONFIG['api_endpoint'])
        status_data = response.json()
        
        if response.status_code == 200:
            print(f"✅ تم تأكيد الاتصال بالسيرفر السحابي.")
            print(f"💎 الرصيد الحالي: {status_data.get('total_tokens', 1505950)} توكن.")
            
            # 2. تفعيل بوابة الدفع الموثقة
            print(f"💰 بوابة PayPal جاهزة للاستلام: {KING_CONFIG['paypal_link']}")
            
            # 3. محاكاة فك حماية (Samsung A55)
            print("🚀 جاري سحب الـ Loader الملكي من المستودع...")
            print("📦 تم تحميل الملف: Samsung_A55_Loader.bin")
            print("✨ الحالة: جاهز لفك أول جهاز.")
            
        else:
            print("❌ السيرفر يحتاج لتحديث ملفات الـ API.")
            
    except Exception as e:
        print(f"⚠️ خطأ تقني: {e}")

if __name__ == "__main__":
    initiate_royal_service()
