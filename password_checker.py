import re

def check_password_strength(password):
    # Initialize score and feedback
    score = 0
    feedback = []

    # Check length
    if len(password) < 8:
        feedback.append("Password is too short. It should be at least 8 characters long.")
    else:
        score += 1
        if len(password) >= 12:
            score += 1
            feedback.append("Good length!")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add uppercase letters for stronger password.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add lowercase letters for stronger password.")

    # Check for numbers
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Add numbers for stronger password.")

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Add special characters for stronger password.")

    # Determine strength based on score
    if score < 3:
        strength = "Weak"
    elif score < 5:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, feedback

# Main program
while True:
    password = input("Enter a password (or 'q' to quit): ")
    if password.lower() == 'q':
        break

    strength, feedback = check_password_strength(password)

    print(f"\nPassword Strength: {strength}")
    if feedback:
        print("Feedback:")
        for item in feedback:
            print(f"- {item}")
    else:
        print("Great job! Your password meets all criteria.")

    print()  # Add a blank line for readability