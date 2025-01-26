import tkinter as tk
from PIL import Image, ImageTk
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QApplication

def get_system_theme():
    try:
        app = QApplication([])
        palette = app.palette()
        color = palette.color(QPalette.Window)

        if color.lightness() < 128:
            return 'dark'
        else:
            return 'light'
    except Exception as e:
        print("Ошибка при определении темы:", e)
        return 'light'

def calculate():
    try:
        num1 = float(entry.get())
        num2 = float(entry3.get())
        operator = entry2.get()

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == ':':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Ошибка: деление на 0"
        else:
            result = "Неверный оператор"

        result_label.pack_forget()
        result_label.config(text="Результат: " + str(result))
        result_label.pack(pady=10)

    except ValueError:
        result_label.pack_forget()
        result_label.config(text="Ошибка: введены некорректные данные")
        result_label.pack(pady=10)

def toggle_inputs():
    global inputs_visible
    if inputs_visible:

        entry.pack_forget()
        entry2.pack_forget()
        entry3.pack_forget()
        button.pack_forget()

        info_label.pack(pady=10)
    else:
        entry.pack(pady=5)
        entry2.pack(pady=5)
        entry3.pack(pady=5)
        button.pack(pady=10)

        info_label.pack_forget()

    inputs_visible = not inputs_visible

current_theme = get_system_theme()

app = tk.Tk()
app.title("Easy-Calculator")

if current_theme == 'dark':
    app.config(bg='#333333')
    button_bg = '#555555'
    button_fg = '#FFFFFF'
    entry_bg = '#555555'
    entry_fg = '#FFFFFF'
    result_label_fg = '#FFFFFF'
else:
    app.config(bg='#FFFFFF')
    button_bg = '#DDDDDD'
    button_fg = '#000000'
    entry_bg = '#FFFFFF'
    entry_fg = '#000000'
    result_label_fg = '#000000'

entry = tk.Entry(app, bg=entry_bg, fg=entry_fg)
entry2 = tk.Entry(app, bg=entry_bg, fg=entry_fg)
entry3 = tk.Entry(app, bg=entry_bg, fg=entry_fg)
button = tk.Button(app, text='Сложить', command=calculate, bg=button_bg, fg=button_fg)
result_label = tk.Label(app, text="Результат: ", fg=result_label_fg, bg=app.cget("bg"))
result_label.pack_forget()

info_label = tk.Label(
    app,
    text="Easy-Calculator - Это самый простой калькулятор написанный на Python! И запомните. В первой строке число, во второй символ, в третьей число! Автор: holos",
    fg=result_label_fg,
    bg=app.cget("bg"),
    wraplength=300
)

info_label.pack_forget()

icon_img = Image.open("Images/iicon.png")
icon_img = icon_img.resize((30, 30), Image.Resampling.LANCZOS)
icon = ImageTk.PhotoImage(icon_img)
toggle_button = tk.Button(app, image=icon, command=toggle_inputs, bg=button_bg, relief="flat")
toggle_button.image = icon
toggle_button.pack(side="bottom", anchor="se", padx=10, pady=10)

entry.pack(pady=5)
entry2.pack(pady=5)
entry3.pack(pady=5)
button.pack(pady=10)

icon_img = Image.open("Images/icon.png")
icon = ImageTk.PhotoImage(icon_img)
app.iconphoto(True, icon)
app.resizable(False, False)

inputs_visible = True
app.mainloop()
