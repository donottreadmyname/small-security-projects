# 01 — Password Strength Checker

My first small security tool. It scores a password from 0 to 5 and tells you what to fix.

## What it checks

- Length of at least 8 characters
- Uppercase, lowercase, digit and special character
- Not in a short list of common passwords

## How to run

```bash
python3 checker.py
```

```text
Enter password: hello123

Strength: Medium (3/5)
Fix:
  - Add uppercase letter (A-Z)
  - Add special character (#?!@$%^&*-)
```

## What I learned

Regular expressions and building a simple scoring system.

## Ideas to improve

- Hide the input with `getpass` so the password is not shown on screen
- Load common passwords from a larger list file instead of four hard-coded ones

**Full write-up:** [iot-security-lab.hashnode.dev/password-checker-python](https://iot-security-lab.hashnode.dev/password-checker-python)
