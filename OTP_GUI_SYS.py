# Importing Necessary libraries
import random
import tkinter as tk
from tkinter import messagebox
from email.message import EmailMessage
import smtplib

class OTPVerificationSystem:
    def __init__(self):         #Constructor __init__ method
        self.root = tk.Tk()
        self.root.title("OTP Verification System")
        self.root.geometry("400x200")
        self.root.configure(bg="#D3D3D3")

        self.generated_otp = ""
        self.attempts_left = 3

        self.create_widgets()

    # to generate 6-digit otp
    def generate_otp(self):
        return ''.join([str(random.randint(0, 9)) for i in range(6)])
    
    #send_otp Method 
    def send_otp(self, email, otp):
        try:
            # Connect to Gmail's SMTP server
            with smtplib.SMTP('smtp.gmail.com', 587) as gmail_server:
                gmail_server.starttls()
               
                from_mail = 'pvijayalaxmi9845@gmail.com'
                gmail_server.login(from_mail, 'rmkk oudy eevj zjnk')  #app password

                # Create the email message
                message = EmailMessage()
                message['Subject'] = 'OTP Verification'
                message['From'] = from_mail
                message['To'] = email
                message.set_content('Your OTP is: ' + otp)

                # Send the email
                gmail_server.send_message(message)

            messagebox.showinfo("OTP Sent", "OTP has been sent to your email.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send OTP: {str(e)}")
    
    # verify_otp Method
    def verify_otp(self):
        entered_otp = self.otp_entry.get()
        if entered_otp == self.generated_otp:
            messagebox.showinfo("OTP verified successfully!")
            self.root.destroy()
        else:
            self.attempts_left -= 1
            if self.attempts_left > 0:
                messagebox.showerror("Error", f"Incorrect OTP. {self.attempts_left} attempts left.")
            else:
                messagebox.showerror("Error", "Max attempts reached.")
                self.root.destroy()
    
    # submitting email
    def submit_email(self):
        email = self.email_entry.get()
        if email.strip() == "":
            messagebox.showerror("Error", "Please enter your email address.")
        else:
            self.generated_otp = self.generate_otp()
            self.send_otp(email, self.generated_otp)
            self.attempts_left = 3
    
    # creating GUI elements
    def create_widgets(self):
        # Email Label and Entry
        email_label = tk.Label(self.root, text="Email:", font=("Arial", 10), bg="#F0F0F0")
        email_label.grid(row=0, column=0, padx=10, pady=5)
        self.email_entry = tk.Entry(self.root, font=("Arial", 10), width=30)
        self.email_entry.grid(row=0, column=1, padx=10, pady=5)

        # OTP Label and Entry
        otp_label = tk.Label(self.root, text="OTP:", font=("Arial", 10), bg="#F0F0F0")
        otp_label.grid(row=1, column=0, padx=10, pady=5)
        self.otp_entry = tk.Entry(self.root, font=("Arial", 10))
        self.otp_entry.grid(row=1, column=1, padx=10, pady=5)

        # Send OTP Button
        send_otp_button = tk.Button(self.root, text="Send OTP", command=self.submit_email, font=("Arial", 10), bg="#FF5733", fg="white")
        send_otp_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="we")

        # Verify Button
        verify_button = tk.Button(self.root, text="Verify OTP", command=self.verify_otp, font=("Arial", 10), bg="#008CBA", fg="white")
        verify_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="we")

        self.root.mainloop()

# Initialize the OTPVerificationSystem
otp_system = OTPVerificationSystem() 



