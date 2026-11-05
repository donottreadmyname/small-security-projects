# 02 — TCP Port Scanner (localhost only)

Checks which TCP ports are open on my own machine using Python's `socket` module.

## How it works

- Tries to connect to `127.0.0.1` on ports 1–1024
- `socket.connect_ex()` returns `0` when the port is open
- Each attempt has a 0.5 s timeout

## How to run

```bash
python3 scanner.py
```

Example output (open ports depend on your machine):

```text
Scanning 127.0.0.1 from 1 to 1024
Started at 2026-11-05 20:15:42.118205
----------------------------------------
Port 22: OPEN
----------------------------------------
Done. Found 1 open ports: [22]
```

## What I learned

Sockets, the TCP connection, `connect_ex` and timeouts.

## Ideas to improve

- Command-line arguments for the port range (`argparse`)
- Scan faster with threads

**Ethical note:** this tool only scans `127.0.0.1`, my own machine.

**Full write-up:** [iot-security-lab.hashnode.dev/port-scanner-python-localhost](https://iot-security-lab.hashnode.dev/port-scanner-python-localhost)
