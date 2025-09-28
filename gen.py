import tkinter as tk
from tkinter import messagebox
import random
import string

root = tk.Tk()
root.title("PassForge")
root.geometry("420x480")
root.resizable(False, False)

# === Settings ===
length_var = tk.IntVar(value=12)
include_letters = tk.BooleanVar(value=True)
include_digits = tk.BooleanVar(value=True)
include_symbols = tk.BooleanVar(value=False)
include_specials = tk.BooleanVar(value=False)
auto_copy = tk.BooleanVar(value=True)

password_var = tk.StringVar()

# === Password generation ===
def generate_password():
    length = length_var.get()
    pools = []

    if include_letters.get():
        pools.append(string.ascii_letters)
    if include_digits.get():
        pools.append(string.digits)
    if include_symbols.get():
        pools.append("!@#$%^&*()_+=-")
    if include_specials.get():
        pools.append("№;%:?*")

    if not pools:
        status_label.config(text="❌ Select at least one character set!", fg="red")
        messagebox.showerror("Error", "Please enable at least one option.")
        return

    # Guarantee at least 1 char from each chosen set
    password_chars = [random.choice(pool) for pool in pools]

    # Fill the rest with random choices
    all_chars = "".join(pools)
    password_chars += [random.choice(all_chars) for _ in range(length - len(password_chars))]
    random.shuffle(password_chars)

    password = "".join(password_chars)
    password_var.set(password)

    status_label.config(text="✅ Password generated!", fg="green")

    if auto_copy.get():
        copy_to_clipboard()

# === Copy password ===
def copy_to_clipboard():
    pwd = password_var.get()
    if pwd:
        root.clipboard_clear()
        root.clipboard_append(pwd)
        status_label.config(text="📋 Copied to clipboard!", fg="green")
    else:
        status_label.config(text="⚠️ Nothing to copy!", fg="orange")

# === GUI ===
tk.Label(root, text="🔒 Password length:").pack(pady=(20, 5))
tk.Spinbox(root, from_=4, to=128, textvariable=length_var, width=5).pack()

options_frame = tk.LabelFrame(root, text="Include in password:")
options_frame.pack(pady=15, padx=10, fill="x")

tk.Checkbutton(options_frame, text="Letters (A-Z, a-z)", variable=include_letters).pack(anchor="w")
tk.Checkbutton(options_frame, text="Digits (0-9)", variable=include_digits).pack(anchor="w")
tk.Checkbutton(options_frame, text="Symbols (!@#)", variable=include_symbols).pack(anchor="w")
tk.Checkbutton(options_frame, text="Specials (№;%:?*)", variable=include_specials).pack(anchor="w")
tk.Checkbutton(options_frame, text="Copy automatically", variable=auto_copy).pack(anchor="w")

tk.Button(root, text="⚡ Generate", command=generate_password, width=30).pack(pady=(10, 5))
tk.Button(root, text="📋 Copy to clipboard", command=copy_to_clipboard, width=30).pack(pady=(0, 15))

output = tk.Entry(root, textvariable=password_var, font=("Courier", 14), justify="center", width=32)
output.pack(pady=5)

status_label = tk.Label(root, text="", fg="green")
status_label.pack()

footer = tk.Label(root, text="Created by Loner © 2025", fg="gray")
footer.pack(side="bottom", pady=10)

root.mainloop()
