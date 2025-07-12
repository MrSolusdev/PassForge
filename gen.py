import tkinter as tk
from tkinter import messagebox
import random
import string

root = tk.Tk()
root.title("LONER PASSWORD GEN @i_o_ekobo")
root.geometry("400x460")
root.resizable(False, False)

# === Настройки ===
length_var = tk.IntVar(value=12)
include_letters = tk.BooleanVar(value=True)
include_digits = tk.BooleanVar(value=True)
include_symbols = tk.BooleanVar(value=False)
include_specials = tk.BooleanVar(value=False)

# === Функция генерации ===
def generate_password():
    length = length_var.get()
    chars = ""

    if include_letters.get():
        chars += string.ascii_letters
    if include_digits.get():
        chars += string.digits
    if include_symbols.get():
        chars += "!@#$%^&*()_+=-"
    if include_specials.get():
        chars += "№;%:?*"

    if not chars:
        messagebox.showerror("Ошибка", "Выбери хотя бы один тип символов!")
        return

    password = ''.join(random.choice(chars) for _ in range(length))
    output.delete(0, tk.END)
    output.insert(0, password)
    status_label.config(text="Пароль сгенерирован ✅")

# === Копирование в буфер по кнопке ===
def copy_to_clipboard():
    pwd = output.get()
    if pwd:
        root.clipboard_clear()
        root.clipboard_append(pwd)
        status_label.config(text="Скопировано в буфер обмена ✅")
    else:
        messagebox.showwarning("Внимание", "Пароль пустой, сначала сгенерируй!")

# === GUI ===
tk.Label(root, text="🔒 Длина пароля:").pack(pady=(20, 5))
tk.Spinbox(root, from_=4, to=128, textvariable=length_var, width=5).pack()

options_frame = tk.LabelFrame(root, text="Включить в пароль:")
options_frame.pack(pady=15, padx=10, fill="x")

tk.Checkbutton(options_frame, text="Буквы (A-Z, a-z)", variable=include_letters).pack(anchor="w")
tk.Checkbutton(options_frame, text="Цифры (0-9)", variable=include_digits).pack(anchor="w")
tk.Checkbutton(options_frame, text="Символы (!@#)", variable=include_symbols).pack(anchor="w")
tk.Checkbutton(options_frame, text="Спецсимволы (№;%:?)", variable=include_specials).pack(anchor="w")

tk.Button(root, text="⚡ Сгенерировать", command=generate_password, width=30).pack(pady=(10,5))
tk.Button(root, text="📋 Копировать в буфер", command=copy_to_clipboard, width=30).pack(pady=(0,15))

output = tk.Entry(root, font=("Courier", 14), justify="center", width=32)
output.pack(pady=5)

status_label = tk.Label(root, text="", fg="green")
status_label.pack()

footer = tk.Label(root, text="Создано Лонером © 2025", fg="gray")
footer.pack(side="bottom", pady=10)

root.mainloop()
