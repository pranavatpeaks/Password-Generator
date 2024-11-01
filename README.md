# Password Manager with Keyword Integration

This is a Python-based GUI application built with Tkinter that allows users to generate and manage passwords securely. The application enables users to:
- Generate strong, customizable passwords containing memorable keywords.
- Save passwords to a CSV file for specific services (e.g., Google, Netflix).
- Securely access the application via a set password, with an initial registration if the application is run for the first time.

## Features
- **Password Generation**: Generates multiple passwords with user-defined length, including a user-specified keyword inserted at a random position.
- **Password Management**: Saves and organizes passwords by service, viewable within the app.
- **Secure Login**: Requires users to set a password on the first run and authenticate in subsequent sessions.
- **User Interface**: Built with Tkinter, providing an intuitive interface for password generation, saving, and viewing saved passwords.

## Usage
1. **Run the Application**: When run for the first time, the user is prompted to register a password.
2. **Login**: On subsequent uses, enter the set password to access the application.
3. **Generate Passwords**: Input the desired number, length, and keyword for the password, and specify the service.
4. **Save Passwords**: Choose a generated password and save it for the corresponding service.
5. **View Saved Passwords**: Review saved passwords in a new window, pulled from the CSV file.

## How to Use
Run the script in a Python environment:
```python password_manager.py```
