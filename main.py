import tkinter as tk
from tkinter import Entry, Label, StringVar

mapping = {
    'q': 'й', 'w': 'ц', 'e': 'у', 'r': 'к', 't': 'е', 'y': 'н', 'u': 'г',
    'i': 'ш', 'o': 'щ', 'p': 'з', '[': 'х', ']': 'ъ', 'a': 'ф', 's': 'ы',
    'd': 'в', 'f': 'а', 'g': 'п', 'h': 'р', 'j': 'о', 'k': 'л', 'l': 'д',
    ';': 'ж', "'": 'э', 'z': 'я', 'x': 'ч', 'c': 'с', 'v': 'м', 'b': 'и',
    'n': 'т', 'm': 'ь', ',': 'б', '.': 'ю', '/': '.',
    'Q': 'Й', 'W': 'Ц', 'E': 'У', 'R': 'К', 'T': 'Е', 'Y': 'Н', 'U': 'Г',
    'I': 'Ш', 'O': 'Щ', 'P': 'З', '{': 'Х', '}': 'Ъ', 'A': 'Ф', 'S': 'Ы',
    'D': 'В', 'F': 'А', 'G': 'П', 'H': 'Р', 'J': 'О', 'K': 'Л', 'L': 'Д',
    ':': 'Ж', '"': 'Э', 'Z': 'Я', 'X': 'Ч', 'C': 'С', 'V': 'М', 'B': 'И',
    'N': 'Т', 'M': 'Ь', '<': 'Б', '>': 'Ю', '?': ',', '@': '"', '#': '№',
    '$': ';', '^': ':', '&': '?'
}


def update_output(*args):
    input_text = input_var.get()
    output_var.set(convert_layout(input_text))


def convert_layout(text):
    result = []
    for char in text:
        if char in mapping:
            result.append(mapping[char])
        else:
            result.append(char)
    return ''.join(result)


app = tk.Tk()
app.title("Конвертер раскладки")

input_var = StringVar()
input_var.trace_add("write", update_output)

output_var = StringVar()

Label(app, text="Введите текст:").pack(pady=10)
Entry(app, textvariable=input_var).pack(pady=10, padx=10, fill=tk.X)

Label(app, text="Преобразованный текст:").pack(pady=10)
Entry(app, textvariable=output_var, state="readonly").pack(pady=10, padx=10, fill=tk.X)

app.mainloop()
