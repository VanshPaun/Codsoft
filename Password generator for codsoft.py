import tkinter as tk
import random

def Capital_Letters():
    return random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

def Small_Letters():
    return random.choice('abcdefghijklmnopqrstuvwxyz')

def Special_Charachters():
    return random.choice('@#$%&')

def Numbers():
    return random.choice('0123456789')

def generate_password():
    length = int(length_entry.get())
    include_special = special_var.get()
    include_capital = capital_var.get()
    include_numbers = numbers_var.get()

    password_characters = []

    if include_special:
        password_characters.append(Special_Charachters())
    if include_capital:
        password_characters.append(Capital_Letters())
    if include_numbers:
        password_characters.append(Numbers())
    
    # Fill the rest of the password with small letters
    while len(password_characters) < length:
        password_characters.append(Small_Letters())
    
    # Shuffle the resulting password to ensure randomness
    random.shuffle(password_characters)
    password = ''.join(password_characters)

    # Ensure minimum length to include at least one of each selected type
    min_length = (include_special) + (include_capital) + (include_numbers)
    if length < min_length:
        result_label.config(text=f"Password length must be at least {min_length} to include all selected types.")
    else:
        result_label.config(text=f"Generated password: {password}")

# Create main window
window = tk.Tk()
window.title("Password Generator")

# Length label and entry
length_label = tk.Label(window, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(window)
length_entry.pack()

# Special characters checkbox
special_var = tk.BooleanVar()
special_checkbox = tk.Checkbutton(window, text="Include Special Characters", variable=special_var)
special_checkbox.pack()

# Capital letters checkbox
capital_var = tk.BooleanVar()
capital_checkbox = tk.Checkbutton(window, text="Include Capital Letters", variable=capital_var)
capital_checkbox.pack()

# Numbers checkbox
numbers_var = tk.BooleanVar()
numbers_checkbox = tk.Checkbutton(window, text="Include Numbers", variable=numbers_var)
numbers_checkbox.pack()

# Generate button
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack()

# Result label
result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()