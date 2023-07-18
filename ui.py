import tkinter as tk

class LoginPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login Page")
        self.configure(bg="black")

        frame_login = tk.Frame(self, bg="black")
        frame_login.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        label_username = tk.Label(frame_login, text="Username:", bg="black", fg="white", font=("Arial", 12))
        label_username.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.entry_username = tk.Entry(frame_login, bg="white", fg="black", highlightbackground="white", highlightthickness=2, font=("Arial", 12))
        self.entry_username.grid(row=0, column=1, padx=10, pady=10)

        label_password = tk.Label(frame_login, text="Password:", bg="black", fg="white", font=("Arial", 12))
        label_password.grid(row=1, column=0, sticky="w", padx=10, pady=10)
        self.entry_password = tk.Entry(frame_login, bg="white", fg="black", show="*", highlightbackground="white", highlightthickness=2, font=("Arial", 12))
        self.entry_password.grid(row=1, column=1, padx=10, pady=10)

        self.button_login = tk.Button(frame_login, text="Login", command=self.login, width=10, bg="white", fg="black", font=("Arial", 12), relief=tk.RAISED)
        self.button_login.grid(row=2, column=1, pady=20)

        self.message_label = tk.Label(frame_login, text="", bg="black", fg="white", font=("Arial", 12))
        self.message_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.entry_username.bind("<Enter>", self.on_enter_username)  # Bind hover event for username entry
        self.entry_username.bind("<Leave>", self.on_leave_username)  # Bind leave event for username entry

        self.entry_password.bind("<Enter>", self.on_enter_password)  # Bind hover event for password entry
        self.entry_password.bind("<Leave>", self.on_leave_password)  # Bind leave event for password entry

        self.geometry("300x200")
        self.resizable(False, False)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Perform login authentication logic here
        if username == "admin" and password == "password":
            self.message_label.config(text="Login successful!", fg="green")
        else:
            self.message_label.config(text="Login failed. Please try again.", fg="red")

    def on_enter_username(self, event):
        self.entry_username.config(bg="green")

    def on_leave_username(self, event):
        self.entry_username.config(bg="white")

    def on_enter_password(self, event):
        self.entry_password.config(bg="red")

    def on_leave_password(self, event):
        self.entry_password.config(bg="black", fg="white")

if __name__ == "__main__":
    login_page = LoginPage()
    login_page.mainloop()
