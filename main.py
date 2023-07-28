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


def on_closing():
    app.destroy()


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


def copy_to_clipboard():
    widget = app.focus_get()
    if isinstance(widget, tk.Entry):
        selected_text = widget.selection_get()
        app.clipboard_clear()
        app.clipboard_append(selected_text)


def paste_from_clipboard(event=None):
    widget = app.focus_get()
    if isinstance(widget, tk.Entry) and widget.winfo_exists():
        clipboard_text = app.clipboard_get()
        try:
            widget.delete("sel.first", "sel.last")
        except tk.TclError:
            pass
        widget.insert(tk.INSERT, clipboard_text)
        return 'break'  # Отключаем стандартное поведение и предотвращаем двойную вставку


def show_context_menu(event):
    try:
        context_menu.tk_popup(event.x_root, event.y_root)
    finally:
        context_menu.grab_release()


app = tk.Tk()
app.title("Конвертер раскладки")
app.protocol("WM_DELETE_WINDOW", on_closing)

input_var = StringVar()
input_var.trace_add("write", update_output)

output_var = StringVar()

Label(app, text="Введите текст:").pack(pady=10)
input_entry = Entry(app, textvariable=input_var)
input_entry.pack(pady=10, padx=10, fill=tk.X)
input_entry.bind("<Button-2>", show_context_menu)  # Используем <Button-2> для кроссплатформенности
input_entry.bind('<Control-v>', paste_from_clipboard)  # Переопределение поведения

Label(app, text="Преобразованный текст:").pack(pady=10)
output_entry = Entry(app, textvariable=output_var, state="readonly")
output_entry.pack(pady=10, padx=10, fill=tk.X)
output_entry.bind("<Button-2>", show_context_menu)  # Используем <Button-2> для кроссплатформенности
output_entry.bind('<Control-v>', paste_from_clipboard)  # Переопределение поведения

# Создание контекстного меню
context_menu = tk.Menu(app, tearoff=0)
context_menu.add_command(label="Копировать", command=copy_to_clipboard)
context_menu.add_command(label="Вставить", command=paste_from_clipboard)

app.mainloop()
