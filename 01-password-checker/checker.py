import re

def check_password_strength(password):
    score = 0
    feedback = []

    # 1. Length >= 8
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("At least 8 characters")

    # 2. Uppercase, lowercase, digit, special
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letter (A-Z)")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letter (a-z)")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add a number (0-9)")

    if re.search(r"[#?!@$%^&*\-]", password):
        score += 1
    else:
        feedback.append("Add special character (#?!@$%^&*-)")

    # 3. Common password check
    common = ["password", "123456", "qwerty", "admin"]
    if password.lower() in common:
        score = 0
        feedback.append("Too common, easily guessed")

    # Result
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, score, feedback


if __name__ == "__main__":
    pwd = input("Enter password: ")
    strength, score, feedback = check_password_strength(pwd)
    print(f"\nStrength: {strength} ({score}/5)")
    if feedback:
        print("Fix:")
        for f in feedback:
            print(f"  - {f}")
