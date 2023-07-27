import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import getpass

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

        self.entry_username.bind("<Enter>", self.on_enter_username) 
        self.entry_username.bind("<Leave>", self.on_leave_username)  

        self.entry_password.bind("<Enter>", self.on_enter_password) 
        self.entry_password.bind("<Leave>", self.on_leave_password) 

        self.geometry("300x200")
        self.resizable(False, False)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        
        if username == "admin" and password == "password":
            self.message_label.config(text="Login successful!", fg="green")
            system_username = getpass.getuser()
            login_page2 = LoginPage2(system_username)
            login_page2.mainloop()
            self.destroy()
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



class LoginPage2(tk.Toplevel):
    def __init__(self, system_username):
        super().__init__()
        self.title("Admin Portal")
        self.configure(bg="white")
        self.geometry("1500x500")

        self.clock_in_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  

        label_message = tk.Label(self, text=f"Welcome, {system_username}!", bg="white", fg="black",
                                 font=("Arial", 16, "bold"))
        label_message.pack(pady=20)

        self.label_time = tk.Label(self, text="", bg="white", fg="black", font=("Arial", 12))
        self.label_time.pack(pady=10)

        self.update_time()  
        self.after(1000, self.update_time)  

        
        button_frame = tk.Frame(self, bg="white")
        button_frame.pack(pady=10)

       
        button_save = tk.Button(button_frame, text="Save Data", width=15, height=2, font=("Arial", 12),
                                command=self.save_data)
        button_save.pack(side=tk.LEFT, padx=(0, 10))

        
        button_view_data = tk.Button(button_frame, text="View Saved Data", width=15, height=2, font=("Arial", 12),
                                     command=self.view_data)
        button_view_data.pack(side=tk.LEFT)

        
        button1 = tk.Button(button_frame, text="Button 1", width=15, height=2, font=("Arial", 12))
        button1.pack(side=tk.LEFT, padx=(10, 0))

        button2 = tk.Button(button_frame, text="Button 2", width=15, height=2, font=("Arial", 12))
        button2.pack(side=tk.LEFT)

       
        field_frame = tk.Frame(self, bg="white")
        field_frame.pack(pady=20)

        label_name = tk.Label(field_frame, text="Name:", bg="white", fg="black", font=("Arial", 12))
        label_name.pack(side=tk.LEFT, padx=(0, 10))

        self.entry_name = tk.Entry(field_frame, bg="white", fg="black", font=("Arial", 12))
        self.entry_name.pack(side=tk.LEFT)

        label_age = tk.Label(field_frame, text="Age:", bg="white", fg="black", font=("Arial", 12))
        label_age.pack(side=tk.LEFT, padx=(20, 10))

        self.entry_age = tk.Entry(field_frame, bg="white", fg="black", font=("Arial", 12))
        self.entry_age.pack(side=tk.LEFT)

        label_email = tk.Label(field_frame, text="Email:", bg="white", fg="black", font=("Arial", 12))
        label_email.pack(side=tk.LEFT, padx=(20, 10))

        self.entry_email = tk.Entry(field_frame, bg="white", fg="black", font=("Arial", 12))
        self.entry_email.pack(side=tk.LEFT)

        
        clock_in_label = tk.Label(self, text=f"User {system_username} clocked in at: {self.clock_in_time}",
                                  bg="white", fg="black", font=("Arial", 12))
        clock_in_label.pack(side=tk.BOTTOM, pady=10)

        self.saved_data = []  

        
        validate_age = self.register(self.validate_age)
        self.entry_age.config(validate="key", validatecommand=(validate_age, "%S"))

        validate_email = self.register(self.validate_email)
        self.entry_email.config(validate="key", validatecommand=(validate_email, "%P"))


    def update_time(self):
        current_time = datetime.now().strftime("%H:%M:%S")  
        self.label_time.config(text="Current Time: " + current_time)
        self.after(1000, self.update_time)  

    def validate_age(self, char):
        if char.isdigit() or char == "\b":
            return True
        return False

    def save_data(self):
        name = self.entry_name.get()
        age = self.entry_age.get()
        email = self.entry_email.get()

       
        if name.strip() == "" or age.strip() == "" or "@" not in email:
            messagebox.showerror("Error", "All fields must be filled and a valid email address must be provided.")
            return False

       
        data_entry = {"Name": name, "Age": age, "Email": email}
        self.saved_data.append(data_entry)

       
        dialog = tk.Toplevel()
        dialog.title("Data Saved")
        dialog.geometry("400x200")

        
        message_font = ("Arial", 14)

       
        message = f"Data saved:\nName: {name}\nAge: {age}\nEmail: {email}"
        message_label = tk.Label(dialog, text=message, font=message_font)
        message_label.pack(padx=20, pady=10)

       
        close_button = tk.Button(dialog, text="Close", command=dialog.destroy, width=10)
        close_button.pack(pady=10)

    def view_data(self):
        if self.saved_data:
            view_data_window = tk.Toplevel()
            view_data_window.title("View Saved Data")
            view_data_window.geometry("600x400")

           
            search_frame = tk.Frame(view_data_window, bg="white")
            search_frame.pack(pady=10)

            search_label = tk.Label(search_frame, text="Search:", bg="white", fg="black", font=("Arial", 12))
            search_label.pack(side=tk.LEFT)

            search_entry = tk.Entry(search_frame, bg="white", fg="black", font=("Arial", 12))
            search_entry.pack(side=tk.LEFT, padx=5)

            search_button = tk.Button(search_frame, text="Search", width=10, height=1, font=("Arial", 12),
                                      command=lambda: self.search_data(search_entry.get()))
            search_button.pack(side=tk.LEFT)

            
            data_frame = tk.Frame(view_data_window, bg="white")
            data_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

            self.data_text = tk.Text(data_frame, bg="white", fg="black", font=("Arial", 12))
            self.data_text.pack(fill=tk.BOTH, expand=True)

            
            for data_entry in self.saved_data:
                self.data_text.insert(tk.END, f"Name: {data_entry['Name']}\nAge: {data_entry['Age']}\nEmail: {data_entry['Email']}\n\n")

           
            close_button = tk.Button(view_data_window, text="Close", command=view_data_window.destroy,
                                      width=10)
            close_button.pack(pady=10)
        else:
            messagebox.showinfo("No Data", "No data has been saved.")

    def search_data(self, search_text):
        self.data_text.delete(1.0, tk.END)


        matching_entries = []
        for data_entry in self.saved_data:
            if search_text.lower() in data_entry["Name"].lower():
                matching_entries.append(data_entry)

       
        for data_entry in matching_entries:
            self.data_text.insert(tk.END, f"Name: {data_entry['Name']}\nAge: {data_entry['Age']}\nEmail: {data_entry['Email']}\n\n")

if __name__ == "__main__":
    login_page = LoginPage()
    login_page.mainloop()
