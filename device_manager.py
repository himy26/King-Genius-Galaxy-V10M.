import subprocess
import serial
import serial.tools.list_ports
import os

class AndroidTool:
    def __init__(self, log_callback=None):
        # تحديد مسار ADB النسبي (بجانب الملف التنفيذي)
        self.adb_path = os.path.join("adb", "adb.exe") 
        self.log_callback = log_callback

    def log(self, message, type="INFO"):
        if self.log_callback:
            self.log_callback(message, type)
        else:
            print(message)

    def run_command(self, command):
        try:
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            
            # تعديل الأمر لاستخدام المسار الصحيح لملف ADB
            if command[0] == "adb": 
                command[0] = self.adb_path
            
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False, startupinfo=startupinfo)
            output, error = process.communicate()
            return output.decode('utf-8', errors='ignore').strip()
        except Exception as e:
            return None

    def check_connection(self):
        output = self.run_command(["adb", "devices"])
        if output and "device" in output and len(output.split('\n')) > 1:
            return True
        return False

    def reboot_download_mtp(self):
        """تحويل لداونلود مود عبر منفذ المودم"""
        self.log("Scanning Samsung Modem Port...", "INFO")
        target_port = None
        
        # البحث عن بورت سامسونج
        for port in serial.tools.list_ports.comports():
            if "SAMSUNG" in port.description.upper() and "MODEM" in port.description.upper():
                target_port = port.device
                break
        
        if target_port:
            try:
                self.log(f"Port Found: {target_port}", "INFO")
                ser = serial.Serial(target_port, 9600, timeout=1)
                ser.write(b'AT+FUS?\r\n') # الأمر السحري
                ser.close()
                self.log("Command Sent via MTP. Rebooting...", "SUCCESS")
            except Exception as e:
                self.log(f"Port Access Error: {e}", "ERROR")
        else:
            self.log("Samsung Modem Port NOT Found (Check Drivers)", "ERROR")