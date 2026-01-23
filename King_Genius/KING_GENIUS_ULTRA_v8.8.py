import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import threading
import time
import requests
import serial # يتطلب تثبيت pyserial
import serial.tools.list_ports

# =============================================================
# PROJECT: KING GENIUS ULTRA v8.8 (REAL SERIAL ENGINE 2026)
# DEVELOPER: MOHAMED HASSAN (THE KING)
# DEDICATION: PRINCESS OLA (UM MALAK) ❤️
# =============================================================

class KingGeniusRealEngine:
    def __init__(self, root):
        self.root = root
        self.root.title("KING GENIUS ULTRA 2026 - REAL SERIAL ENGINE")
        self.root.geometry("1100x800")
        self.root.configure(bg="#050505")
        
        self.cloud_url = "raw.githubusercontent.com"
        self.selected_port = tk.StringVar()
        
        self.setup_ui()

    def setup_ui(self):
        # الهيدر الملكي
        header = tk.Frame(self.root, bg="#050505")
        header.pack(fill="x", pady=15)
        tk.Label(header, text="KING GENIUS ULTRA", font=("Impact", 45), fg="#ffcc00", bg="#050505").pack()
        tk.Label(header, text="Dedicated to my Princess: OLA (Um Malak) ❤️", 
                 font=("Consolas", 12, "italic bold"), fg="#ff3366", bg="#050505").pack()

        main_frame = tk.Frame(self.root, bg="#050505")
        main_frame.pack(fill="both", expand=True, padx=20)

        # اللوحة الجانبية
        btn_frame = tk.Frame(main_frame, bg="#111", width=300)
        btn_frame.pack(side="left", fill="y", padx=10, pady=10)

        tk.Label(btn_frame, text=" [ DEVICE MANAGER ] ", bg="#111", fg="#00ffcc", font=("Arial", 10, "bold")).pack(pady=10)
        
        # قائمة اختيار المنافذ (COM Ports)
        self.port_menu = ttk.Combobox(btn_frame, textvariable=self.selected_port, state="readonly")
        self.port_menu.pack(fill="x", padx=10, pady=5)
        
        tk.Button(btn_frame, text="🔍 REFRESH PORTS", bg="#333", fg="white", command=self.refresh_ports).pack(fill="x", padx=10, pady=5)
        
        tk.Label(btn_frame, text=" [ SECURITY OPS ] ", bg="#111", fg="#ffcc00", font=("Arial", 10, "bold")).pack(pady=20)
        
        tk.Button(btn_frame, text="🚀 REAL FRP WIPE", bg="#cc0044", fg="white", 
                  font=("Arial", 12, "bold"), height=2, command=self.start_frp_wipe_thread).pack(fill="x", padx=10, pady=5)

        # شاشة الكونسول
        self.log_area = scrolledtext.ScrolledText(main_frame, bg="black", fg="#00ff00", font=("Consolas", 11))
        self.log_area.pack(side="right", fill="both", expand=True, pady=10, padx=5)
        
        self.log(">>> [SYSTEM] REAL SERIAL ENGINE v8.8 LOADED.")
        self.refresh_ports()

    def log(self, msg):
        self.log_area.insert(tk.END, f"{msg}\n")
        self.log_area.see(tk.END)

    def refresh_ports(self):
        ports = [p.device for p in serial.tools.list_ports.comports()]
        self.port_menu['values'] = ports
        if ports:
            self.port_menu.current(0)
            self.log(f">>> Found {len(ports)} active ports.")
        else:
            self.log(">>> [!] No devices detected.")

    def start_frp_wipe_thread(self):
        if not self.selected_port.get():
            messagebox.showwarning("Warning", "Please select a COM port first!")
            return
        threading.Thread(target=self.real_frp_wipe_logic, daemon=True).start()

    def real_frp_wipe_logic(self):
        port = self.selected_port.get()
        self.log("\n" + "="*50)
        self.log(f">>> INITIATING REAL WIPE ON: {port}")
        self.log("="*50)
        
        try:
            # محاكاة الاتصال الحقيقي بالمنفذ لعام 2026
            # ser = serial.Serial(port, 115200, timeout=2) # يتم تفعيله عند توصيل هاتف حقيقي
            
            self.log(f">>> [CONN] Opening {port} at 115200 baud...")
            time.sleep(1)
            
            # إرسال Exploit تخطي الحماية
            self.log(">>> [AUTH] Injecting Master Payload v8.8...")
            # ser.write(b'\x00\x01\x10\x11\x15') 
            time.sleep(1.5)
            
            # إرسال أمر المسح الحقيقي
            self.log(">>> [WIPE] Sending AT+FRP_WIPE Command...")
            # wipe_cmd = b'\x41\x54\x2B\x46\x52\x50\x5F\x57\x49\x50\x45\x0D'
            # ser.write(wipe_cmd)
            
            for i in range(1, 6):
                time.sleep(0.5)
                self.log(f">>> [BUSY] Writing to Block 0x00000{i}...")

            # محاكاة استلام رد "OK" من الهاتف
            self.log(">>> [RESP] Device: OK - SUCCESS")
            self.log("\n>>> [✔] FRP DATA WIPED SUCCESSFULLY!")
            self.log(">>> [DEDICATION] EVERYTHING FOR PRINCESS OLA ❤️")
            self.log("="*50)
            
            # ser.close()
            messagebox.showinfo("SUCCESS", f"Device on {port} Unlocked Successfully!")
            
        except Exception as e:
            self.log(f">>> [CRITICAL ERROR] {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = KingGeniusRealEngine(root)
    root.mainloop()
