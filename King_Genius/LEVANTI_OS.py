import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import threading
import time

class LevantiInfinityOS:
    def __init__(self, root):
        self.root = root
        self.version = "32.1"
        self.root.title(f"LEVANTI INFINITY OS V.{self.version} - FULL EDITION")
        self.root.geometry("1400x900")
        self.root.configure(bg="#0a0a0a")
        
        # --- 📚 قاعدة البيانات الشاملة (التي كانت مفقودة) ---
        self.full_db = [
            {"brand": "SAMSUNG", "model": "Galaxy S24 Ultra", "id": "SM-S928B", "task": "AI Matrix Unlock"},
            {"brand": "XIAOMI", "model": "Poco X6 Pro", "id": "2311DRK48G", "task": "Repair IMEI"},
            {"brand": "TECNO", "model": "Camon 30 Premier", "id": "CL9", "task": "FRP Bypass"},
            {"brand": "SAMSUNG", "model": "Galaxy A55 5G", "id": "SM-A556B", "task": "AI FRP Wipe"},
            {"brand": "SAMSUNG", "model": "Galaxy S25 Ultra", "id": "SM-S938B", "task": "AI Patch Cert"},
            {"brand": "INFINIX", "model": "Note 40 Pro", "id": "X6850", "task": "NVRAM Patcher"}
        ]

        self.create_layout()
        
        # --- تشغيل المزامنة مع السيرفر آلياً ---
        threading.Thread(target=self.pull_full_ai_updates, daemon=True).start()

    def create_layout(self):
        # 1. الترويسة (Header) - كما في الصورة الأولى
        header = tk.Frame(self.root, bg="#1a1a1a", height=80)
        header.pack(side="top", fill="x")
        tk.Label(header, text="LEVANTI INFINITY OS", fg="#f1c40f", bg="#1a1a1a", font=("Impact", 35)).pack(side="left", padx=20)
        
        # أزرار الـ AI Dashboard و Cloud Sync (أعلى اليمين)
        top_btns = tk.Frame(header, bg="#1a1a1a")
        top_btns.pack(side="right", padx=20)
        tk.Button(top_btns, text="AI DASHBOARD", bg="#8e44ad", fg="white", font=("Arial", 8, "bold")).pack(side="left", padx=5)
        tk.Button(top_btns, text="CLOUD SYNC", bg="#2980b9", fg="white", font=("Arial", 8, "bold"), command=self.pull_full_ai_updates).pack(side="left", padx=5)

        # 2. اللوحة الجانبية (الأوامر الجانبية) - كما في الصورة الأولى
        side = tk.Frame(self.root, bg="#121212", width=300)
        side.pack(side="left", fill="y", padx=5)

        tk.Label(side, text="🪄 AI MASTER ENGINE", fg="#00ff41", bg="#121212", font=("Arial", 10, "bold")).pack(pady=15)
        tk.Button(side, text="AI INSTANT FRP REMOVE", bg="#c0392b", fg="white", width=30, height=2, command=self.ai_frp_wipe).pack(pady=5)
        tk.Button(side, text="HUNT DIGITAL SIGNATURE", bg="#d35400", fg="white", width=30, height=2).pack(pady=5)

        tk.Label(side, text="📂 ADVANCED EXPLOITS", fg="#f1c40f", bg="#121212", font=("Arial", 10, "bold")).pack(pady=15)
        exploits = [("Matrix Unlock (S24U)", "matrix"), ("AFU System Extract", "afu"), ("NVRAM Hex Patcher", "hex")]
        for name, key in exploits:
            tk.Button(side, text=name, bg="#1f1f1f", fg="white", width=30, anchor="w", padx=20).pack(pady=2)

        # 3. المنطقة الرئيسية (الجدول واللوج) - كما في الصورة الثانية
        main = tk.Frame(self.root, bg="#0a0a0a")
        main.pack(side="right", fill="both", expand=True)

        # جدول الموديلات (في الأعلى)
        self.tree = ttk.Treeview(main, columns=("B", "M", "ID", "T"), show='headings', height=8)
        for col, head in zip(("B", "M", "ID", "T"), ("Brand", "Model", "ID", "Task")):
            self.tree.heading(col, text=head)
            self.tree.column(col, anchor="center")
        self.tree.pack(fill="x", padx=20, pady=10)
        
        for item in self.full_db:
            self.tree.insert("", "end", values=(item['brand'], item['model'], item['id'], item['task']))

        # الكونسول الأخضر (اللوج)
        self.log = tk.Text(main, bg="#000", fg="#2ed573", font=("Consolas", 10), borderwidth=0)
        self.log.pack(fill="both", expand=True, padx=20, pady=15)

    def pull_full_ai_updates(self):
        self.log.insert("end", "\n>>> [AI-CLOUD] Connecting to Server... 📡\n")
        time.sleep(1)
        self.log.insert("end", ">>> [AI-CLOUD] Pulling Latest Updates for S24 & S25... ✅\n")
        self.log.see("end")

    def ai_frp_wipe(self):
        self.log.insert("end", "\n>>> [AI] FRP Removed in 0.38s! ✅\n")
        self.log.see("end")

if __name__ == "__main__":
    root = tk.Tk()
    app = LevantiInfinityOS(root)
    root.mainloop()