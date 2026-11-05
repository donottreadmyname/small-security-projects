# Small Security Projects

Small Python tools I build to understand how security tools work under the hood.
Each folder has the code and a short README. Longer write-ups are on my [blog](https://iot-security-lab.hashnode.dev).

| # | Project | What it does | Status |
|---|---|---|---|
| 01 | [Password Strength Checker](./01-password-checker/) | Scores a password on length, character types and a short common-password list | ✅ Done |
| 02 | [TCP Port Scanner](./02-port-scanner/) | Checks which TCP ports are open on localhost using Python sockets | ✅ Done |
| 03 | File Integrity Checker | Saves SHA-256 hashes of a folder, then reports files that were added, changed or deleted | 📝 Next |

## Requirements

Python 3, standard library only.

## Ethics

These tools are for learning on my own machine. The port scanner only targets `127.0.0.1`.
