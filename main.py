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


def convert_layout(text):
    result = []
    for char in text:
        # Проверка языка и преобразование в другой язык
        if char in mapping:
            result.append(mapping[char])
        elif char in mapping.values():
            for key, value in mapping.items():
                if char == value:
                    result.append(key)
                    break
        else:
            result.append(char)
    return ''.join(result)


def update_output(*args):
    input_text = input_var.get()
    output_var.set(convert_layout(input_text))


def copy_to_clipboard(event):
    widget = app.focus_get()
    if isinstance(widget, tk.Entry):
        selected_text = widget.selection_get()
        app.clipboard_clear()
        app.clipboard_append(selected_text)
        return 'break'  # Отключаем стандартное поведение


def paste_from_clipboard(event):
    widget = app.focus_get()
    if isinstance(widget, tk.Entry):
        clipboard_text = app.clipboard_get()
        widget.delete("sel.first", "sel.last")
        widget.insert(tk.INSERT, clipboard_text)
        return 'break'  # Отключаем стандартное поведение


app = tk.Tk()
app.title("Конвертер раскладки")

# Учитываем кроссплатформенность
if app.tk.call('tk', 'windowingsystem') == 'aqua':  # macOS
    app.bind_all('<Command-c>', copy_to_clipboard)
    app.bind_all('<Command-v>', paste_from_clipboard)
else:  # Windows и Linux
    app.bind_all('<Control-c>', copy_to_clipboard)
    app.bind_all('<Control-v>', paste_from_clipboard)

input_var = StringVar()
input_var.trace_add("write", update_output)

output_var = StringVar()

Label(app, text="Введите текст:").pack(pady=10)
Entry(app, textvariable=input_var).pack(pady=10, padx=10, fill=tk.X)

Label(app, text="Преобразованный текст:").pack(pady=10)
Entry(app, textvariable=output_var, state="readonly").pack(pady=10, padx=10, fill=tk.X)

app.mainloop()
