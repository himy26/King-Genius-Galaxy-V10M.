import smtplib
import os
from email.message import EmailMessage

def send_royal_report():
    # استدعاء المفتاح الملكي من الخزنة
    APP_PASSWORD = os.environ.get('ROYAL_APP_PASSWORD')
    SENDER_EMAIL = "himy26@gmail.com"
    RECEIVER_EMAIL = "himy26@gmail.com"

    msg = EmailMessage()
    msg.set_content("مولاي الملك محمد حسن،\n\nتم تفعيل الرادار بنجاح. حصيلة الـ Tokens في ازدياد، وملفات الـ FRP مؤمنة بالكامل.\n\nإمبراطورية V10M تحت الحراسة.")
    msg['Subject'] = "🚩 تقرير السيادة: نظام V10M الملكي"
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(SENDER_EMAIL, APP_PASSWORD)
            smtp.send_message(msg)
            print("تم الإرسال لسيادة الملك بنجاح!")
    except Exception as e:
        print(f"عطل تقني: {e}")

if __name__ == "__main__":
    send_royal_report()
