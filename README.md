# Password-Checker
Advanced password strength checker built using Python and Tkinter with real-time feedback and smart suggestions.
👉 Includes features like progress bar, password generator, and secure validation techniques.

## 📌 Description

This project is an **Advanced Password Strength Checker** built using **Python and Tkinter**. It evaluates the strength of a password based on multiple security parameters and provides real-time feedback with suggestions for improvement.

This project is developed as part of my **SkillCraft Technology Internship (Task 03)** and focuses on improving password security awareness and user experience.

## 🚀 Features

* 🔍 Password strength evaluation (Weak / Medium / Strong)
* 📊 Strength progress bar visualization
* 👁️ Show/Hide password functionality
* 🔑 Auto-generate strong and secure passwords
* 💡 Smart suggestions for weak passwords
* 🧹 Clear/reset functionality
* 🖥️ Simple and user-friendly GUI

## 🛠️ Technologies Used

* Python 3
* Tkinter (GUI Library)
* Regular Expressions (`re`)
* Random & String modules (for password generation)

## 📂 Project Structure

```
password-strength-checker/
│
├── advanced_password_checker.py
├── README.md
```

## ▶️ How to Run

1. Install Python (3.x recommended)
2. Open terminal / command prompt
3. Navigate to project folder
4. Run the program:

```
python advanced_password_checker.py
```
## 💡 How It Works

The system evaluates the password based on the following criteria:

* Minimum length (8+ characters)
* Strong length (12+ characters)
* Presence of uppercase letters
* Presence of lowercase letters
* Inclusion of numbers
* Inclusion of special characters

Each condition increases the strength score. Based on the score:

* Weak ❌
* Medium ⚠️
* Strong ✅

## 💡 Password Suggestion Feature

The application provides intelligent suggestions such as:

* Add uppercase letters
* Include numbers
* Use special characters
* Increase password length

This helps users create stronger and more secure passwords.

## 🎯 Example

```
Input: abc123
Output: Weak ❌  
Suggestions: Add uppercase letters, Include special characters

Input: Abc@12345
Output: Strong ✅
```
## 🎯 Applications

* Learning cybersecurity fundamentals
* Password security awareness
* Academic mini-projects
* Hackathon submissions
* Beginner GUI development practice

## ⚠️ Limitations

* Basic rule-based checking (not AI-based)
* Does not check against real-world password breaches

## 🔮 Future Enhancements

* Integration with password breach APIs
* Strength meter with real-time typing feedback
* Web-based version (Flask/React)
* Dark/Light theme toggle
* Multi-language support

## 👨‍💻 Author

Palla Venkata Mahesh
GitHub: https://github.com/palla-mahesh

## 📜 License
This project is licensed under the MIT License.
## ✅ Conclusion

This project successfully demonstrates the implementation of a password strength evaluation system using Python and Tkinter. It not only checks the strength of passwords but also guides users in creating secure passwords through intelligent suggestions. The addition of features like password generation, progress visualization, and user-friendly interface enhances both functionality and usability. Overall, this project provides a strong foundation in cybersecurity concepts and GUI application development, making it valuable for academic learning and practical implementation.

⭐ If you like this project, give it a **star**!
