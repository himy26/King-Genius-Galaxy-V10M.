import os
import subprocess

def king_genius_wipe():
    print("--- 👑 LEVANTI MASTER WIPE START 👑 ---")
    try:
        # الأمر الأول: مسح البيانات (Factory Reset)
        os.system("adb shell recovery --wipe_data")
        
        # الأمر الثاني: مسح الكاش
        os.system("adb shell am broadcast -a android.intent.action.MASTER_CLEAR")
        
        # الأمر الثالث: إعادة تشغيل إجبارية للتنفيذ
        subprocess.run(["adb", "reboot", "recovery"], shell=True)
        
        print("✅ Done! The phone should start Wiping now.")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    king_genius_wipe()