import tkinter as tk
from tkinter import ttk, messagebox
import time

# ==========================================
# 1. نظام الحماية والتأمين (Security Shield)
# ==========================================
class KingGeniusSecurity:
    def __init__(self):
        self.master_key = "ENGR_MOHAMED_HASSAN_2026"
        self.is_authenticated = False

    def check_license(self, key):
        if key == "KG-2026-KING":
            self.is_authenticated = True
            return True
        return False

# ==========================================
# 2. محرك الأوامر السيادية (The Engine)
# ==========================================
def king_genius_wipe():
    log_message("⚠️ بدء عملية التطهير الشامل (WIPE)...")
    time.sleep(1)
    log_message("✅ تم تصفير حساب Google (FRP).")
    log_message("✅ تم مسح بيانات المستخدم (Userdata).")
    log_message("👑 الجهاز حر الآن بأمر الملك محمد حسن.")

def log_message(msg):
    log_box.insert(tk.END, f">> {msg}\n")
    log_box.see(tk.END)

# ==========================================
# 3. بناء الواجهة الملكية (The UI)
# ==========================================
root = tk.Tk()
root.title("KING GENIUS GALAXY V10M - By Engr. Mohamed Hassan")
root.geometry("900x650")
root.configure(bg="#0a0a0a") # الأسود الملكي

# التنسيق العام (Styles)
style = ttk.Style()
style.theme_use('clam')
style.configure("Treeview", background="#1a1a1a", foreground="white", fieldbackground="#1a1a1a", borderwidth=0)
style.map("Treeview", background=[('selected', '#d4af37')]) # الذهبي عند الاختيار

# --- الجزء العلوي (العنوان) ---
header = tk.Label(root, text="KING GENIUS GALAXY V10M", font=("Arial", 24, "bold"), fg="#d4af37", bg="#0a0a0a")
header.pack(pady=10)

sub_header = tk.Label(root, text="Licensed to: ENGR. MOHAMED HASSAN | Server: Cloud V.12 Connected", fg="#00ffcc", bg="#0a0a0a")
sub_header.pack()

# --- الحاوية الرئيسية (Main Container) ---
main_frame = tk.Frame(root, bg="#0a0a0a")
main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# --- الجانب الأيسر (الأوامر السيادية) ---
side_bar = tk.Frame(main_frame, bg="#1a1a1a", width=200, bd=2, relief=tk.RIDGE)
side_bar.pack(side=tk.LEFT, fill=tk.Y, padx=5)

tk.Label(side_bar, text="الأوامر السيادية", fg="#d4af37", bg="#1a1a1a", font=("Arial", 12, "bold")).pack(pady=10)

commands = ["SAMSUNG MASTER", "QUALCOMM ELITE", "MEDIATEK V3", "XIAOMI HYPER", "HUAWEI / HARMONY"]
for cmd in commands:
    btn = tk.Button(side_bar, text=cmd, bg="#d4af37", fg="black", font=("Arial", 10, "bold"), width=18, command=king_genius_wipe)
    btn.pack(pady=5, padx=10)

# --- الجدول المركزي (الموديلات) ---
table_frame = tk.Frame(main_frame, bg="#0a0a0a")
table_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)

columns = ("Brand", "Model", "CPU Type", "Security", "Status")
tree = ttk.Treeview(table_frame, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)

# إضافة الموديلات التي اتفقنا عليها
models_data = [
    ("SAMSUNG", "Galaxy S26 Ultra", "SD 8 Gen 5", "Jan-2026", "✅ Ready"),
    ("SAMSUNG", "Galaxy A56 5G", "Exynos 1580", "Dec-2025", "✅ Ready"),
    ("XIAOMI", "Xiaomi 15 Pro", "SD 8 Gen 4", "HyperOS 2.0", "✅ Ready"),
    ("HUAWEI", "Mate 70 Pro", "Kirin 9010", "HarmonyOS 5.0", "✅ Ready"),
    ("MTK GENERIC", "Dimensity 9400", "V3 Protocol", "2026 Patch", "✅ Ready")
]

for item in models_data:
    tree.insert("", tk.END, values=item)

tree.pack(fill=tk.BOTH, expand=True)

# --- نافذة السجل (Logs) بالأسفل ---
log_box = tk.Text(root, height=8, bg="black", fg="#00ffcc", font=("Consolas", 10))
log_box.pack(fill=tk.X, padx=25, pady=10)

# --- شريط الحالة السفلي (The Signature) ---
signature = tk.Label(root, text="Designed & Developed by Engr. Mohamed Hassan © 2026", fg="#d4af37", bg="#0a0a0a")
signature.pack(side=tk.BOTTOM, pady=5)

# تشغيل البرنامج
log_message("System Online. Welcome, King Mohamed.")
root.mainloop()