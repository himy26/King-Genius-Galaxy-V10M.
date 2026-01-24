import smtplib
import os
import glob
from email.message import EmailMessage

def mine_tokens_and_files():
    # 1. إحصاء الملفات والحصيلة تقنياً
    all_files = glob.glob('**/*', recursive=True)
    frp_files = [f for f in all_files if 'FRP' in f or f.endswith('.bin')]
    total_tokens = len(all_files) * 1250  # معادلة ملكية لحساب الحصيلة البرمجية
    
    # 2. إعداد تقرير السيادة المطور
    report_content = f"""
    مولاي الملك محمد حسن،
    
    تم انتهاء عملية التنقيب بنجاح بـ "سرعة البرق":
    
    📊 حصيلة الـ Tokens المكتشفة: {total_tokens:,} Token
    📁 عدد ملفات السيادة المكتشفة: {len(all_files)} ملف
    🔐 ملفات الـ FRP والملفات الحساسة: {len(frp_files)} ملف
    
    إمبراطورية V10M تحت الحراسة التقنية المطلقة.
    """
    return report_content

def send_royal_report():
    APP_PASSWORD = os.environ.get('ROYAL_APP_PASSWORD')
    SENDER_EMAIL = "himy26@gmail.com"
    RECEIVER_EMAIL = "himy26@gmail.com"

    if not APP_PASSWORD:
        return

    msg = EmailMessage()
    msg.set_content(mine_tokens_and_files())
    msg['Subject'] = "💎 تقرير التنقيب الملكي: حصيلة Tokens V10M"
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(SENDER_EMAIL, APP_PASSWORD)
            smtp.send_message(msg)
            print("تم إرسال تقرير التنقيب بنجاح!")
    except Exception as e:
        print(f"عطل تقني: {e}")

if __name__ == "__main__":
    send_royal_report()
