import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import serial
import serial.tools.list_ports
import subprocess
import threading
import time
import os

# =====================================================
#   VISION PRINCE - THE ULTIMATE MOBILE UTILITY
#   Developer: Mohamed Hassan
#   Version: 3.0 (Samsung High-End & MTK Support)
# =====================================================

class VisionPrinceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("VISION PRINCE TOOL v3.0 - AI Powered")
        self.root.geometry("850x650")
        self.root.configure(bg="#1e1e1e")

        # --- Variables ---
        self.selected_port = tk.StringVar()
        self.adb_status = tk.StringVar(value="ADB: Disconnected")
        self.root_status = tk.StringVar(value="ROOT: No Access")

        # --- UI Setup ---
        self.create_header()
        self.create_connection_panel()
        self.create_operation_panel()
        self.create_log_panel()
        
        # Start Auto-Scan Thread
        self.monitoring = True
        self.scanner_thread = threading.Thread(target=self.auto_scan_devices)
        self.scanner_thread.daemon = True
        self.scanner_thread.start()

    def create_header(self):
        header_frame = tk.Frame(self.root, bg="#006400", height=80)
        header_frame.pack(fill="x", side="top")
        
        title_lbl = tk.Label(header_frame, text="VISION PRINCE", font=("Impact", 28), bg="#006400", fg="white")
        title_lbl.pack(pady=5)
        
        subtitle_lbl = tk.Label(header_frame, text="Samsung & MTK Professional Repair Agent", font=("Arial", 10), bg="#006400", fg="#dddddd")
        subtitle_lbl.pack()

    def create_connection_panel(self):
        conn_frame = tk.LabelFrame(self.root, text=" Connection Manager ", bg="#1e1e1e", fg="cyan", font=("Arial", 10, "bold"))
        conn_frame.pack(fill="x", padx=10, pady=10)

        # Port Selection
        lbl_port = tk.Label(conn_frame, text="Select Port:", bg="#1e1e1e", fg="white")
        lbl_port.grid(row=0, column=0, padx=5, pady=5)
        
        self.combo_ports = ttk.Combobox(conn_frame, textvariable=self.selected_port, width=40)
        self.combo_ports.grid(row=0, column=1, padx=5)
        self.refresh_ports()
        
        btn_refresh = tk.Button(conn_frame, text="Refresh Ports", command=self.refresh_ports, bg="#444", fg="white")
        btn_refresh.grid(row=0, column=2, padx=5)

        # Status Labels
        lbl_adb = tk.Label(conn_frame, textvariable=self.adb_status, fg="#00ff00", bg="#1e1e1e", font=("Consolas", 10, "bold"))
        lbl_adb.grid(row=1, column=0, columnspan=2, sticky="w", padx=5)
        
        lbl_root = tk.Label(conn_frame, textvariable=self.root_status, fg="orange", bg="#1e1e1e", font=("Consolas", 10, "bold"))
        lbl_root.grid(row=1, column=2, sticky="w", padx=5)

    def create_operation_panel(self):
        ops_frame = tk.LabelFrame(self.root, text=" Repair Operations ", bg="#1e1e1e", fg="cyan", font=("Arial", 10, "bold"))
        ops_frame.pack(fill="x", padx=10, pady=5)

        # IMEI Inputs
        tk.Label(ops_frame, text="IMEI 1:", bg="#1e1e1e", fg="white").grid(row=0, column=0, padx=5, pady=5)
        self.entry_imei1 = tk.Entry(ops_frame, width=25, bg="#333", fg="white", insertbackground="white", font=("Arial", 12))
        self.entry_imei1.grid(row=0, column=1, padx=5)

        tk.Label(ops_frame, text="IMEI 2:", bg="#1e1e1e", fg="white").grid(row=0, column=2, padx=5, pady=5)
        self.entry_imei2 = tk.Entry(ops_frame, width=25, bg="#333", fg="white", insertbackground="white", font=("Arial", 12))
        self.entry_imei2.grid(row=0, column=3, padx=5)

        # Buttons
        # زر الروت (للأجهزة الحديثة)
        btn_repair_root = tk.Button(ops_frame, text="REPAIR (ROOT/ADB Mode)\n[For Modern Samsung 2023+]", command=lambda: self.start_task("ROOT_REPAIR"), bg="#8B0000", fg="white", width=30, height=2, font=("Arial", 9, "bold"))
        btn_repair_root.grid(row=1, column=0, columnspan=2, padx=5, pady=10)

        # زر الكوم بورت (للأجهزة القديمة)
        btn_repair_at = tk.Button(ops_frame, text="REPAIR (AT/Modem Mode)\n[For Older Devices]", command=lambda: self.start_task("AT_REPAIR"), bg="#00008B", fg="white", width=30, height=2, font=("Arial", 9, "bold"))
        btn_repair_at.grid(row=1, column=2, columnspan=2, padx=5, pady=10)
        
        # زر تفعيل ADB
        btn_enable_adb = tk.Button(ops_frame, text="Help Enable ADB (*#0*# Guide)", command=lambda: self.start_task("ENABLE_ADB"), bg="#555", fg="white", width=50)
        btn_enable_adb.grid(row=2, column=0, columnspan=4, pady=5)

    def create_log_panel(self):
        log_frame = tk.LabelFrame(self.root, text=" System Log ", bg="#1e1e1e", fg="cyan")
        log_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.log_area = scrolledtext.ScrolledText(log_frame, bg="black", fg="#00ff00", font=("Consolas", 9))
        self.log_area.pack(fill="both", expand=True)

    # --- Core Logic Functions ---

    def log(self, message):
        timestamp = time.strftime("[%H:%M:%S]")
        self.log_area.insert(tk.END, f"{timestamp} {message}\n")
        self.log_area.see(tk.END)

    def refresh_ports(self):
        ports = serial.tools.list_ports.comports()
        port_list = []
        for p in ports:
            port_list.append(f"{p.device} - {p.description}")
        self.combo_ports['values'] = port_list
        if port_list:
            self.combo_ports.current(0)

    def auto_scan_devices(self):
        """Background thread to check ADB connection constantly"""
        while self.monitoring:
            try:
                # Check ADB
                startupinfo = subprocess.STARTUPINFO()
                startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                
                output = subprocess.check_output(["adb", "devices"], startupinfo=startupinfo).decode()
                if "device" in output.replace("List of devices attached", "").strip():
                    self.adb_status.set("ADB: CONNECTED [OK]")
                    
                    # Check Root if ADB is ok
                    try:
                        root_check = subprocess.check_output(["adb", "shell", "su", "-c", "id"], startupinfo=startupinfo).decode()
                        if "uid=0" in root_check:
                            self.root_status.set("ROOT: GRANTED [SUPERUSER]")
                        else:
                            self.root_status.set("ROOT: DENIED")
                    except:
                         self.root_status.set("ROOT: NO SU BINARY")
                else:
                    self.adb_status.set("ADB: Disconnected")
                    self.root_status.set("ROOT: --")
                
            except Exception:
                pass
            time.sleep(2)

    def start_task(self, task_name):
        # Run tasks in separate thread to prevent GUI freezing
        t = threading.Thread(target=self.execute_task, args=(task_name,))
        t.start()

    def execute_task(self, task_name):
        imei1 = self.entry_imei1.get()
        imei2 = self.entry_imei2.get()

        if task_name == "ROOT_REPAIR":
            self.log(">>> STARTING IMEI REPAIR (ROOT MODE) <<<")
            if "CONNECTED" not in self.adb_status.get():
                self.log("[Error] ADB not connected. Please enable USB Debugging.")
                return
            
            if "GRANTED" not in self.root_status.get():
                self.log("[Warning] Root not detected. Attempting anyway (Might fail on RZ serials)...")
                self.log("[Tip] Ensure Magisk is installed and Grant permission on phone screen.")

            # أوامر الروت القوية
            cmds = [
                'adb shell su -c "stop ril-daemon"',
                'adb shell su -c "stop cpboot-daemon"',
                f'adb shell su -c "echo -e \'AT+EGMR=1,7,\\"{imei1}\\"\' > /dev/ttyacm0"',
                f'adb shell su -c "echo -e \'AT+EGMR=1,10,\\"{imei2}\\"\' > /dev/ttyacm0"',
                f'adb shell su -c "echo -e \'AT+EGMR=1,7,\\"{imei1}\\"\' > /dev/smd0"',
                f'adb shell su -c "echo -e \'AT+EGMR=1,10,\\"{imei2}\\"\' > /dev/smd0"',
                'adb shell su -c "start ril-daemon"',
                'adb shell su -c "start cpboot-daemon"'
            ]
            
            for cmd in cmds:
                self.log(f"Executing: {cmd}")
                subprocess.call(cmd, shell=True)
                time.sleep(1)
            
            self.log("[DONE] Commands sent. Rebooting device to apply changes...")
            subprocess.call("adb reboot", shell=True)

        elif task_name == "AT_REPAIR":
            self.log(">>> STARTING IMEI REPAIR (AT/MODEM MODE) <<<")
            port_str = self.selected_port.get().split(" - ")[0]
            if not port_str:
                self.log("[Error] No Port Selected.")
                return

            try:
                ser = serial.Serial(port_str, 115200, timeout=1)
                self.log(f"Connected to {port_str}")
                
                # Handshake
                ser.write(b"AT\r\n")
                time.sleep(0.5)
                resp = ser.read_all().decode(errors='ignore')
                self.log(f"Response: {resp.strip()}")

                if "OK" in resp:
                    # Write IMEI
                    cmd = f'AT+EGMR=1,7,"{imei1}"\r\n'
                    self.log(f"Writing: {cmd.strip()}")
                    ser.write(cmd.encode())
                    time.sleep(1)
                    final_resp = ser.read_all().decode(errors='ignore')
                    self.log(f"Result: {final_resp.strip()}")
                    
                    if "ERROR" in final_resp:
                        self.log("[FAIL] Security Blocked. Try ROOT Mode (Red Button).")
                else:
                    self.log("[Error] Device not responding to AT. Check Drivers.")
                
                ser.close()

            except Exception as e:
                self.log(f"[Exception] {e}")

        elif task_name == "ENABLE_ADB":
            self.log(">>> GUIDE: HOW TO ENABLE ADB <<<")
            self.log("1. Disconnect USB Cable.")
            self.log("2. Open Phone Dialpad.")
            self.log("3. Type *#0*# to enter Test Mode.")
            self.log("4. Connect USB Cable again.")
            self.log("5. If tool supports exploit, it will trigger now.")
            self.log("[Note] For RZ Serial, please use Manual Root (Magisk) method.")

# --- Main Loop ---
if __name__ == "__main__":
    root = tk.Tk()
    app = VisionPrinceApp(root)
    root.mainloop()