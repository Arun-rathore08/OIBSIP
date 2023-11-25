import random
import string
import tkinter as tk

def generate_password(length=8):
    characters = string.ascii_letters + string.digits 
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_button_clicked():
    length = int(length_entry.get())
    password = generate_password(length)
    password_label.config(text="Generated Password: " + password)

# Create the main window
window = tk.Tk()
window.title("Password Generator")

# Create the length label and entry
length_label = tk.Label(window, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(window)
length_entry.pack()

# Create the generate button
generate_button = tk.Button(window, text="Generate Password", command=generate_button_clicked)
generate_button.pack()

# Create the password label
password_label = tk.Label(window, text="Generated Password: ")
password_label.pack()

# Start the GUI event loop
window.mainloop()
