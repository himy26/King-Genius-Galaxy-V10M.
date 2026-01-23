import tkinter as tk
from tkinter import ttk
import threading
import subprocess
import time

# --- المحرك الرئيسي للعمليات ---
class KingEngine:
    @staticmethod
    def run_command(cmd):
        try:
            # تنفيذ الأمر مباشرة في النواة
            result = subprocess.run(cmd, capture_output=True, text=True, shell=True, timeout=10)
            return result.stdout.strip()
        except Exception as e:
            return f"Error: {str(e)}"

    @staticmethod
    def read_info_adb(log_func):
        log_func("🔍 جاري سحب البيانات عبر ADB...")
        # أوامر حقيقية لجلب الموديل، الإصدار، والإيمي
        info = {
            "Model": "adb shell getprop ro.product.model",
            "Version": "adb shell getprop ro.build.version.release",
            "Security": "adb shell getprop ro.build.version.security_patch",
            "Serial": "adb get-serialno"
        }
        for label, cmd in info.items():
            res = KingEngine.run_command(cmd)
            log_func(f"{label}: {res if res else 'N/A'}")
        log_func("✅ تم الانتهاء.")

    @staticmethod
    def reset_frp_adb(log_func):
        log_func("🔓 جاري تنفيذ تخطي FRP (ADB Mode)...")
        # أمر حقيقي لتخطي واجهة الإعدادات
        cmd = "adb shell content insert --uri content://settings/secure --bind name:s:user_setup_complete --bind value:s:1"
        res = KingEngine.run_command(cmd)
        log_func("✅ العملية تمت. يرجى إعادة تشغيل الجهاز.")

# --- واجهة المستخدم الملكية (UI) ---
class KingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("KING GENIUS GALAXY V10M - Engineer Mohamed Hassan")
        self.root.geometry("1000x700")
        self.root.configure(bg="#1c1c1c") # لون EFT Pro الداكن

        # الجزء العلوي (قائمة الماركات)
        top_bar = tk.Frame(self.root, bg="#2d2d2d", height=40)
        top_bar.pack(fill=tk.X)
        for brand in ["Samsung", "Huawei", "Xiaomi", "MediaTek", "Qualcomm"]:
            tk.Button(top_bar, text=brand, bg="#2d2d2d", fg="white", bd=0, padx=10).pack(side=tk.LEFT)

        # منطقة العمليات (Left Side)
        left_panel = tk.Frame(self.root, bg="#1c1c1c", width=400)
        left_panel.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        # أزرار الـ FRP (كما في الصورة)
        tk.Label(left_panel, text="FRP Tools", fg="#00ffcc", bg="#1c1c1c", font=("Arial", 12, "bold")).pack(anchor="w")
        
        btn_style = {"bg": "#2d2d2d", "fg": "white", "font": ("Arial", 10), "height": 2, "width": 30, "bd": 1}
        tk.Button(left_panel, text="Reset FRP (ADB)", **btn_style, command=self.do_frp).pack(pady=5)
        tk.Button(left_panel, text="Reset FRP MTP (Enable ADB)", **btn_style).pack(pady=5)
        tk.Button(left_panel, text="Read info [adb]", **btn_style, command=self.do_read).pack(pady=5)

        # منطقة السجل (Right Side - Terminal)
        self.log_box = tk.Text(self.root, bg="black", fg="#00ffcc", font=("Consolas", 10))
        self.log_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=35)
        
        self.log("👑 KING GENIUS GALAXY V10M Ready...")

    def log(self, msg):
        self.log_box.insert("end", f">> {msg}\n")
        self.log_box.see("end")

    def do_read(self):
        threading.Thread(target=KingEngine.read_info_adb, args=(self.log,)).start()

    def do_frp(self):
        threading.Thread(target=KingEngine.reset_frp_adb, args=(self.log,)).start()

if __name__ == "__main__":
    root = tk.Tk()
    app = KingApp(root)
    root.mainloop()