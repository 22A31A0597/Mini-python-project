import tkinter as tk
from tkinter import messagebox
import random
import string
class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        master.title("Password Generator")
        self.username_label = tk.Label(master, text="Enter username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(master, width=30, bg="pink")
        self.username_entry.pack()
        self.password_label = tk.Label(master, text="Enter password length:")
        self.password_label.pack()
        self.password_entry = tk.Entry(master, width=30, bg="pink")
        self.password_entry.pack()
        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()
        self.strength_label = tk.Label(master, text="")
        self.strength_label.pack()
    def generate_password(self):
        try:
            username = self.username_entry.get()
            length = int(self.password_entry.get())
            if length <= 0:
                messagebox.showerror("Error", "Length should be a positive integer.")
                return
            password = self._generate_random_password(length)
            messagebox.showinfo("Generated Password", f"Username: {username}\nPassword: {password}")
            self.check_password_strength(password)
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid integer for the length.")
    def _generate_random_password(self, length):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password
    def check_password_strength(self, password):
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in string.punctuation for c in password)
        length_ok = len(password) >= 8
        if has_upper and has_lower and has_digit and has_special and length_ok:
            self.strength_label.config(text="Password is strong!")
        else:
            self.strength_label.config(text="Password could be stronger.")
def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
if __name__ == "__main__":
    main()