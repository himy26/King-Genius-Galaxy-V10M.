import os
import requests

# --- إعدادات الملك محمد حسن الخاصة ---
LOCAL_ARCHIVE_PATH = r"C:\Hydra Tool\Boot\DA"  # المسار اللي فيه ملفاتك (تأكد منه)
SERVER_UPLOAD_URL = "https://your-king-server.com/upload" # رابط سيرفرك
ADMIN_KEY = "MOHAMED_HASSAN_KING_2026" # مفتاح الأمان الخاص بك

def start_upload():
    print("👑 جاري تشغيل أداة الرفع الملكية...")
    
    # فحص المجلدات والملفات
    for root, dirs, files in os.walk(LOCAL_ARCHIVE_PATH):
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, LOCAL_ARCHIVE_PATH)
            
            print(f"🚀 جاري تأمين ورفع: {relative_path}...")
            
            # إرسال الملف للسيرفر
            with open(file_path, 'rb') as f:
                files_data = {'file': (relative_path, f)}
                data = {'admin_key': ADMIN_KEY, 'path': relative_path}
                
                try:
                    # هذه العملية ترفع الملفات لـ 7 تيرابايت في سيرفرك
                    response = requests.post(SERVER_UPLOAD_URL, files=files_data, data=data)
                    if response.status_code == 200:
                        print(f"✅ تم الرفع بنجاح: {file}")
                    else:
                        print(f"❌ فشل الرفع: {file} - سبب: {response.text}")
                except Exception as e:
                    print(f"❌ خطأ في الاتصال بالسيرفر: {str(e)}")

if __name__ == "__main__":
    start_upload()