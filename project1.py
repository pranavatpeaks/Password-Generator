import tkinter as tk
import csv
import os
import random
import string

# Global variables
passwords = {}
registered = False
password_file = "registered_password.txt"
csv_file = "passwords.csv"

# Actual password generation logic with keyword insertion
def generate_passwords(num_passwords, length, keyword):
    password_list = []
    for _ in range(int(num_passwords)):
        # Ensure the password length is long enough to fit the keyword
        if len(keyword) > int(length):
            password_list.append(f"Error: Keyword too long for the given length!")
            continue

        # Generate random characters excluding the keyword length
        random_password = ''.join(random.choices(string.ascii_letters + string.digits, k=int(length) - len(keyword)))

        # Insert the keyword at a random position
        insertion_point = random.randint(0, len(random_password))
        password = random_password[:insertion_point] + keyword + random_password[insertion_point:]
        password_list.append(password)
    return password_list

def save_password_to_csv(service, password):
    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([service, password])

def set_password():
    entered_password = entry_set_password.get()
    with open(password_file, "w") as file:
        file.write(entered_password)
    global registered
    registered = True
    window_register.destroy()
    access_login()

def check_password():
    entered_password = entry_password.get()
    if os.path.exists(password_file):
        with open(password_file, "r") as file:
            stored_password = file.read().strip()
        if entered_password == stored_password:
            access_interface()
        else:
            entry_password.delete(0, tk.END)
            label_error.config(text="Invalid password!")
    else:
        access_register()

def access_login():
    global window_login, entry_password, label_error
    window_login = tk.Tk()
    window_login.title("Login")

    label_password = tk.Label(window_login, text="Enter Password:")
    label_password.pack()
    
    entry_password = tk.Entry(window_login, show="*")
    entry_password.pack()

    button_login = tk.Button(window_login, text="Login", command=check_password)
    button_login.pack()

    label_error = tk.Label(window_login, text="", fg="red")
    label_error.pack()

    window_login.mainloop()

def access_register():
    global window_register, entry_set_password
    window_register = tk.Tk()
    window_register.title("Register")

    label_set_password = tk.Label(window_register, text="Set Password:")
    label_set_password.pack()
    
    entry_set_password = tk.Entry(window_register, show="*")
    entry_set_password.pack()

    button_set_password = tk.Button(window_register, text="Set Password", command=set_password)
    button_set_password.pack()

    window_register.mainloop()

def display_saved_passwords():
    global window_saved_passwords
    window_saved_passwords = tk.Tk()
    window_saved_passwords.title("Saved Passwords")

    # Read passwords from CSV and display
    if os.path.exists(csv_file):
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            label_passwords = tk.Label(window_saved_passwords, text="Saved Passwords:")
            label_passwords.pack()
            for row in reader:
                label_password = tk.Label(window_saved_passwords, text=f"Service: {row[0]}, Password: {row[1]}")
                label_password.pack()
    else:
        label_passwords = tk.Label(window_saved_passwords, text="No passwords saved yet!")
        label_passwords.pack()

    window_saved_passwords.mainloop()

def access_interface():
    window_login.destroy()
    
    # Creating the main window
    global window, entry_number, entry_length, entry_keyword, entry_service, text_area, selected_password
    window = tk.Tk()
    window.title("Password Manager")

    label_number = tk.Label(window, text="Amount of passwords to generate:")
    label_number.pack()
    entry_number = tk.Entry(window)
    entry_number.pack()

    label_length = tk.Label(window, text="Input password length:")
    label_length.pack()
    entry_length = tk.Entry(window)
    entry_length.pack()

    label_keyword = tk.Label(window, text="Keyword to remember:")
    label_keyword.pack()
    entry_keyword = tk.Entry(window)
    entry_keyword.pack()

    label_service = tk.Label(window, text="Service name (e.g., Google, Netflix):")
    label_service.pack()
    entry_service = tk.Entry(window)
    entry_service.pack()

    # Button to generate passwords
    generate_button = tk.Button(window, text="Generate Passwords", command=generate_and_display)
    generate_button.pack()

    # Text area to display generated passwords
    text_area = tk.Text(window, height=10, width=40)
    text_area.pack()

    # Entry field to select password index
    selected_password_label = tk.Label(window, text="Choose password (index):")
    selected_password_label.pack()
    selected_password = tk.Entry(window)
    selected_password.pack()

    # Button to save selected password
    save_button = tk.Button(window, text="Save Password", command=save_password)
    save_button.pack()

    # Button to display saved passwords
    show_passwords_button = tk.Button(window, text="Show Saved Passwords", command=display_saved_passwords)
    show_passwords_button.pack()
    window.mainloop()

def generate_and_display():
    service = entry_service.get()
    num_passwords = entry_number.get()
    length = entry_length.get()
    keyword = entry_keyword.get()
    
    password_list = generate_passwords(num_passwords, length, keyword)
    global passwords
    passwords[service] = password_list

    text_area.delete(1.0, tk.END)
    for idx, password in enumerate(password_list):
        text_area.insert(tk.END, f"{idx}: {password}\n")

def save_password():
    service = entry_service.get()
    index = selected_password.get()

    if service in passwords and index.isdigit():
        index = int(index)
        if 0 <= index < len(passwords[service]):
            selected_pwd = passwords[service][index]
            save_password_to_csv(service, selected_pwd)

if __name__ == "__main__":
    if not os.path.exists(password_file):
        access_register()
    else:
        access_login()
