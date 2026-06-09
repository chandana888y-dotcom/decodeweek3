# decodeweek3
A simple Python project that generates strong and secure random passwords based on the user-defined length. The generated password includes a mix of uppercase letters, lowercase letters, numbers, and special characters to improve security.

📌 Features

* Generates random passwords of any length (minimum 4 characters)
* Includes:
    * Uppercase letters (A-Z)
    * Lowercase letters (a-z)
    * Numbers (0-9)
    * Special characters (!, @, #, $, etc.)
* Ensures every password contains at least:
    * 1 uppercase letter
    * 1 lowercase letter
    * 1 digit
    * 1 special character
* User-friendly command-line interface
* Input validation for password length

🛠️ Technologies Used

* Python 3
* Built-in random module
* Built-in string module
* 📂 Project Structure
* random-password-generator/
│
├── password_generator.py
└── README.md
▶️ How to Run

1. Make sure Python 3 is installed on your system.
2. Download or clone the project.
3. Open a terminal in the project folder.
4. Run the program:
5. python password_generator.py
6. 5. Enter the desired password length when prompted.
   6. 💻 Sample Output
   7. ========================================
      RANDOM PASSWORD GENERATOR
========================================

Enter password length (minimum 4): 12

Generated Password:
A#7mK!9xP@2q
🔒 Password Security

This project generates passwords using a combination of letters, digits, and special characters, making them more resistant to guessing and brute-force attacks. Each generated password contains a balanced mix of character types to improve strength.

🎯 Learning Objectives

This project helps beginners learn:

* Functions in Python
* User input handling
* Exception handling (try-except)
* Randomization using the random module
* String manipulation
* Basic password security concepts

🚀 Future Enhancements

* Password strength checker
* Copy password to clipboard
* Save generated passwords to a file
* Custom character selection options
* Graphical User Interface (GUI) using Tkinter
