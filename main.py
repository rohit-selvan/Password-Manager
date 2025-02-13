import tkinter as tk
from tkinter import messagebox
import pyperclip  
import random
import string

class PasswordManager(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Password Manager")
        self.geometry("400x400")
        self.configure(bg="#f0f4c3")  
        self.create_widgets()

    def create_widgets(self):
     
        title_label = tk.Label(self, text="Password Manager", font=("Verdana", 20, "bold"), bg="#f0f4c3", fg="#333")
        title_label.pack(pady=20)
        
        
        frame = tk.Frame(self, bg="#dcedc8", padx=10, pady=10)
        frame.pack(pady=10)
        
      
        tk.Label(frame, text="Website:", font=("Verdana", 12), bg="#dcedc8").grid(row=0, column=0, sticky="w")
        self.website_entry = tk.Entry(frame, font=("Verdana", 12), width=30)
        self.website_entry.grid(row=0, column=1, pady=5)
        
        
        tk.Label(frame, text="Username:", font=("Verdana", 12), bg="#dcedc8").grid(row=1, column=0, sticky="w")
        self.username_entry = tk.Entry(frame, font=("Verdana", 12), width=30)
        self.username_entry.grid(row=1, column=1, pady=5)
        
       
        tk.Label(frame, text="Password:", font=("Verdana", 12), bg="#dcedc8").grid(row=2, column=0, sticky="w")
        self.password_entry = tk.Entry(frame, font=("Verdana", 12), width=30)
        self.password_entry.grid(row=2, column=1, pady=5)
        
        
        generate_button = tk.Button(self, text="Generate Password", font=("Verdana", 12), command=self.generate_password, bg="#aed581", fg="white", relief="groove", cursor="hand2")
        generate_button.pack(pady=10)
        
       
        save_button = tk.Button(self, text="Save Password", font=("Verdana", 12), command=self.save_password, bg="#81c784", fg="white", relief="raised", cursor="hand2")
        save_button.pack(pady=5)
        
    def generate_password(self):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(12))
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)
        pyperclip.copy(password)
        messagebox.showinfo("Password Generated", "Password has been copied to clipboard!")

    def save_password(self):
        website = self.website_entry.get().strip()
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        
        if not website or not username or not password:
            messagebox.showwarning("Input Error", "Please fill in all fields.")
            return
        
        with open("passwords.txt", "a") as file:
            file.write(f"Website: {website} | Username: {username} | Password: {password}\n")
        
        messagebox.showinfo("Success", "Password saved successfully!")
        self.clear_fields()

    def clear_fields(self):
        self.website_entry.delete(0, tk.END)
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

if __name__ == "__main__":
    app = PasswordManager()
    app.mainloop()
