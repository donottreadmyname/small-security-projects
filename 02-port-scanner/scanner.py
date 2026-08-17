import socket
from datetime import datetime

def scan_ports(target="127.0.0.1", start_port=1, end_port=1024):
    print(f"Scanning {target} from {start_port} to {end_port}")
    print(f"Started at {datetime.now()}")
    print("-" * 40)
    
    open_ports = []
    
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        # 0 = open
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port}: OPEN")
            open_ports.append(port)
        sock.close()
    
    print("-" * 40)
    print(f"Done. Found {len(open_ports)} open ports: {open_ports}")
    return open_ports

if __name__ == "__main__":
    # ETHICAL USE ONLY - localhost only
    scan_ports("127.0.0.1", 1, 1024)
