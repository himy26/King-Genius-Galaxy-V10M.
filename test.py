import subprocess

def debug_fastboot():
    print("--- LEVANTI DIAGNOSTIC ---")
    # التأكد هل الويندوز يرى أي منافذ USB مرتبطة بالهاتف
    try:
        check = subprocess.run(["fastboot", "devices"], capture_output=True, text=True, shell=True)
        if not check.stdout.strip():
            print("❌ الويندوز لا يرى الهاتف. السبب: (إما الكابل سيء، أو التعريف ناقص).")
        else:
            print(f"✅ تم العثور على الجهاز: {check.stdout.strip()}")
            print("الآن يمكنك استخدام البرنامج الأصلي للفورمات!")
    except Exception as e:
        print(f"خطأ في النظام: {e}")

debug_fastboot()