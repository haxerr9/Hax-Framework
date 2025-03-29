# Script Made By hax / haxer
import socket
import time

def portscan(host, ports):
    ctime = time.ctime()
    print(f"\n[?] Started Port Scan At {ctime}")
    for port in ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.2)

            result = s.connect_ex((host, port))

            if result == 0:
                print(f"[+] OPEN PORT (TCP) {port}")

        except KeyboardInterrupt:
            print("\n[!] Stopping Port Scan !")
            break
    
    print(f"\n[?] Port Scan Finished At {ctime}\n ")
