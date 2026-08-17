# 02 - TCP Port Scanner (localhost only)

Scans TCP ports on localhost using Python socket.

**How to run:**

**What it checks:**
- Tries to connect to 127.0.0.1:1-1024
- Uses socket.connect_ex() - 0 = open

**Full write-up:** https://iot-security-lab.hashnode.dev/port-scanner-python-localhost

**What I learned:** socket, TCP, connect_ex, timeout
**Ethical note:** Only scan 127.0.0.1
