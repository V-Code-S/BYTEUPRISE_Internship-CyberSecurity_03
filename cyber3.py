import tkinter as tk
from tkinter import messagebox

def caesar_cipher(text, shift, mode):
    result = ""

    if mode == "decrypt":
        shift = -shift

    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char

    return result

def encrypt_message():
    shift = int(shift_entry.get())
    plaintext = text_entry.get("1.0", tk.END).strip()
    ciphertext = caesar_cipher(plaintext, shift, "encrypt")
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, ciphertext)

def decrypt_message():
    shift = int(shift_entry.get())
    ciphertext = text_entry.get("1.0", tk.END).strip()
    plaintext = caesar_cipher(ciphertext, shift, "decrypt")
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, plaintext)

def on_closing():
    root.destroy()

# Setup GUI
root = tk.Tk()
root.title("Caesar Cipher Project By Virupakshi")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

text_label = tk.Label(frame, text="Enter text:")
text_label.grid(row=0, column=0, pady=5)

text_entry = tk.Text(frame, wrap='word', width=50, height=10)
text_entry.grid(row=1, column=0, pady=5)

shift_label = tk.Label(frame, text="Shift value:")
shift_label.grid(row=2, column=0, pady=5)

shift_entry = tk.Entry(frame)
shift_entry.grid(row=3, column=0, pady=5)

encrypt_button = tk.Button(frame, text="Encrypt", command=encrypt_message)
encrypt_button.grid(row=4, column=0, pady=5)

decrypt_button = tk.Button(frame, text="Decrypt", command=decrypt_message)
decrypt_button.grid(row=5, column=0, pady=5)

result_label = tk.Label(frame, text="Result:")
result_label.grid(row=6, column=0, pady=5)

result_text = tk.Text(frame, wrap='word', width=50, height=10)
result_text.grid(row=7, column=0, pady=5)

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
