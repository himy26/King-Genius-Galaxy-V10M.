import smtplib
import threading
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# --- الإعدادات الملكية ---
SENDER_EMAIL = "himy26@gmail.com"
RECEIVER_EMAIL = "himy26@gmail.com"
APP_PASSWORD = "ضع_هنا_كلمة_سر_التطبيقات" # كلمة سر التطبيقات من جوجل

def royal_report_delivery():
    """عملية التسليم الملكي للتقارير"""
    try:
        # إنشاء الرسالة السيادية
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECEIVER_EMAIL
        msg['Subject'] = "تقرير السيادة والتدفق المالي (LEVANTI V10M - Official)"

        body = """
        بأمر الملك محمد حسن، إليك تقرير جرد السيرفر:
        ------------------------------------------
        1. واجهة V10M: نـشطة وبقوة.
        2. حصيلة الـ Tokens: تجاوزت 9,600,000.
        3. ملفات FRP (الـ 500): جاهزة للضخ في المستودع.
        4. مشروع برنسيسا: محمي بكلمة سر "ملك".
        
        تم الإرسال بـ "سرعة البرق" عبر رادار V10M.
        """
        msg.attach(MIMEText(body, 'plain', 'utf-8'))

        # الاتصال بسيرفر البريد بـ "سرعة الرعد"
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(SENDER_EMAIL, APP_PASSWORD)
            server.send_message(msg)
            
        print("⚡ تم الإرسال بنجاح يا مولاي المهندس محمد حسن!")
    except Exception as e:
        print(f"❌ عائق تقني: {e}")

# --- تفعيل الرادار في الخلفية بنظام Threading ---
def start_royal_threading():
    royal_thread = threading.Thread(target=royal_report_delivery, name="Royal_Flash_Sender")
    royal_thread.start()

if __name__ == "__main__":
    start_royal_threading()
