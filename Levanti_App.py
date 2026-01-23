import customtkinter as ctk
import subprocess
import os

class LevantiFinalFix(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("LEVANTI V.12 - THE REAL ENGINE")
        self.geometry("800x600")
        ctk.set_appearance_mode("dark")

        # العنوان
        ctk.CTkLabel(self, text="LEVANTI REAL POWER 👑", font=("Orbitron", 24, "bold"), text_color="#3498db").pack(pady=20)

        # منطقة النتائج
        self.console = ctk.CTkTextbox(self, font=("Consolas", 16), fg_color="#000000", text_color="#00FF00")
        self.console.pack(fill="both", expand=True, padx=20, pady=10)

        # الأزرار التنفيذية
        self.btn_check = ctk.CTkButton(self, text="🔍 TEST CONNECTION", command=self.test_conn, fg_color="#2ecc71", height=45)
        self.btn_check.pack(pady=10, padx=20, fill="x")

        self.btn_format = ctk.CTkButton(self, text="🧹 REAL FORMAT (USERDATA)", command=lambda: self.run_action("erase userdata"), fg_color="#e74c3c", height=45)
        self.btn_format.pack(pady=10, padx=20, fill="x")

    def log(self, msg):
        self.console.insert("end", f">>> {msg}\n")
        self.console.see("end")

    def test_conn(self):
        self.log("Searching for device in Fastboot mode...")
        # التأكد من وجود ملف fastboot في نفس المجلد
        if not os.path.exists("fastboot.exe"):
            self.log("❌ ERROR: fastboot.exe MISSING in this folder!")
            return

        try:
            # تشغيل الفحص
            res = subprocess.run(["fastboot.exe", "devices"], capture_output=True, text=True, shell=True)
            if res.stdout.strip():
                self.log(f"✅ DEVICE DETECTED: {res.stdout.strip()}")
            else:
                self.log("❌ STILL NO DEVICE. (Check Cable & Fastboot Screen on Phone)")
        except Exception as e:
            self.log(f"❌ CRITICAL ERROR: {str(e)}")

    def run_action(self, cmd):
        self.log(f"Initiating: fastboot {cmd}...")
        try:
            res = subprocess.run(["fastboot.exe"] + cmd.split(), capture_output=True, text=True, shell=True)
            if res.stderr: self.log(f"Output: {res.stderr}")
            if "finished" in res.stderr.lower():
                self.log("👑 SUCCESS! King Mohamed Power executed.")
        except Exception as e:
            self.log(f"❌ FAILED: {str(e)}")

if __name__ == "__main__":
    app = LevantiFinalFix()
    app.mainloop()