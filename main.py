import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

def new_file():
    text_box.delete(1.0, tk.END)

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            text_box.delete(1.0, tk.END)
            text_box.insert(tk.END, content)

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension='.txt')
    if file_path:
        content = text_box.get(1.0, tk.END)
        with open(file_path, 'w') as file:
            file.write(content)

def exit_app():
    if messagebox.askokcancel("Выход", "Вы уверены, что хотите выйти?"):
        root.destroy()

def set_light_theme():
    root.config(bg='white')
    text_box.config(bg='white', fg='black')

def set_dark_theme():
    root.config(bg='black')
    text_box.config(bg='black', fg='white')

root = tk.Tk()
root.title("Простой блокнот")

menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Новый", command=new_file)
file_menu.add_command(label="Открыть", command=open_file)
file_menu.add_command(label="Сохранить", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=exit_app)
menu_bar.add_cascade(label="Файл", menu=file_menu)

theme_menu = tk.Menu(menu_bar, tearoff=0)
theme_menu.add_command(label="Светлая", command=set_light_theme)
theme_menu.add_command(label="Темная", command=set_dark_theme)
menu_bar.add_cascade(label="Тема", menu=theme_menu)

root.config(menu=menu_bar)

text_box = tk.Text(root)
text_box.pack(fill=tk.BOTH, expand=True)

root.mainloop()