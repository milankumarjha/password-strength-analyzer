import re
import getpass

# A list of very common, weak passwords.
# Using a set makes checking (lookup) much faster than a list.
COMMON_PASSWORDS = {
    "password", "123456", "qwerty", "admin", "123456789",
    "12345", "111111", "pass", "letmein", "secret"
}

def check_password_strength(password):
    score = 0
    feedback = []

    # --- Criterion 1: Length (Min 12 chars) ---
   
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 12 characters long.")

    # --- Criterion 2: Uppercase Letter ---
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append(" Add at least one uppercase letter (A-Z).")

    # --- Criterion 3: Lowercase Letter ---
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append(" Add at least one lowercase letter (a-z).")

    # --- Criterion 4: Number ---
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append(" Add at least one number (0-9).")

    # --- Criterion 5: Symbol ---
    # \W matches any "non-word" character.
    if re.search(r"\W", password):
        score += 1
    else:
        feedback.append(" Add at least one symbol (e.g., !, @, #, $).")

    # --- Criterion 6: Check against common password list ---
   
    if password.lower() in COMMON_PASSWORDS:
        feedback.append(" CRITICAL: This is a very common and weak password.")
        score = 0  # Reset score to 0 if it's a common password

    return score, feedback

def get_strength_level(score):
    if score <= 2:
        return "🟥 Very Weak"
    elif score == 3:
        return "🟧 Weak"
    elif score == 4:
        return "🟨 Medium"
    elif score == 5:
        return "🟩 Strong"
    else:  # Score is 6
        return "🟦 Very Strong"

def main():
    try:
        # Use getpass.getpass() instead of input()
        password = getpass.getpass("Enter a password to check (MK will hide your input): ")
        
        # If the user just hits Enter, we stop.
        if not password:
            print("No password entered. Exiting.")
            return

        score, feedback = check_password_strength(password)
        strength = get_strength_level(score)

        print("\n--- Password Analysis ---")
        print(f"Overall Strength: {strength} (Score: {score}/6)")
        
        if feedback:
            print("\nAdvice to improve:")
            for item in feedback:
                print(f"  - {item}")
        else:
            print("\n✅ Excellent! This is a strong password.")

    except KeyboardInterrupt:
        # This handles if the user presses Ctrl+C to quit
        print("\nPassword check cancelled.")

# This line tells Python to run the main() function
# when the script is executed.
if __name__ == "__main__":
    main()