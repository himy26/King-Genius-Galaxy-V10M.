import serial.tools.list_ports
print("--- LEVANTI PORT SCANNER ---")
ports = list(serial.tools.list_ports.comports())
if not ports:
    print("❌ NO DEVICE FOUND! Check Cable.")
for p in ports:
    print(f"✅ FOUND: {p.description}")