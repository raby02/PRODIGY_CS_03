# PRODIGY_CS_03
Implementation of Password Complexity Checker
# Password Complexity Checker

## Overview
The **Password Complexity Checker** is a Python tool designed to evaluate the strength of a user's password based on several criteria:
- Length of the password.
- Inclusion of uppercase and lowercase letters.
- Presence of numbers.
- Use of special characters.

The tool provides real-time feedback to the user on the password's strength, indicating areas for improvement to make the password more secure.

## Features
- **Password Length Check**: 
  - Identifies if the password is at least 8 characters long.
  - Recommends a length of 12 or more characters for a stronger password.

- **Uppercase and Lowercase Check**:
  - Checks for the presence of both uppercase and lowercase letters in the password.
  
- **Number Check**:
  - Ensures that the password contains at least one numerical digit.
  
- **Special Characters Check**:
  - Verifies that the password includes special characters such as `!@#$%^&*(),.?":{}|<>`.

- **Password Strength Scoring**:
  - Scores the password based on the criteria above.
  - Categorizes the password strength as **Weak**, **Moderate**, or **Strong** based on the total score.
  
- **Feedback Mechanism**:
  - Provides actionable feedback for users on how to improve their passwords.
 
## Requirements
- **Python 3.x**: Ensure that Python is installed on your system.
- **`re` module**: This is a built-in Python module for regular expressions, so no additional installation is needed.

## How It Works
1. The user is prompted to input a password.
2. The script checks the password against various criteria:
   - Length
   - Presence of uppercase and lowercase letters
   - Inclusion of numbers and special characters
3. A score is assigned based on the strength of the password.
4. The password is categorized as "Weak," "Moderate," or "Strong."
5. Feedback is provided to the user to help improve their password if necessary.
6. The user can continue testing passwords until they choose to quit the program.

## How to Run
1. **Clone the Repository**: Download or clone the project from GitHub.
   ```bash
   git clone https://github.com/raby02/PRODIGY_CS_03.git 
2. **Navigate to the project directory**:
    ```bash
    cd PRODIGY_CS_03
   ```
3. **Navigate to the project directory**:
 ```bash
   python password_checker.py
 ```
   
## Code Explanation

### `check_password_strength(password)` Function
This function takes a password as input and checks it against several security criteria. It returns two values:
- **Strength**: A string indicating whether the password is "Weak," "Moderate," or "Strong."
- **Feedback**: A list of suggestions on how to improve the password.

#### Steps in the Function:
1. **Initialize Score and Feedback**:
   - A score variable is initialized to track the password's strength.
   - A feedback list stores suggestions for improvement.

2. **Length Check**:
   - If the password is less than 8 characters, a suggestion is added to the feedback.
   - If the password is 12 or more characters, an extra point is added for "Good length."

3. **Uppercase, Lowercase, Number, and Special Character Checks**:
   - Uses regular expressions (`re.search`) to check for the presence of uppercase, lowercase letters, numbers, and special characters.
   - Adds to the score if the password meets these criteria.
   - Provides feedback if any of these criteria are not met.

4. **Strength Determination**:
   - Determines password strength based on the total score:
     - **< 3**: Weak
     - **< 5**: Moderate
     - **>= 5**: Strong

### Main Program
- A `while` loop continuously prompts the user for passwords.
- Users can quit the program by entering 'q'.
- The password's strength and feedback are displayed after each input.

## Example Usage
```plaintext
Enter a password (or 'q' to quit): MyPassword123

Password Strength: Moderate
Feedback:
- Add special characters for a stronger password.

