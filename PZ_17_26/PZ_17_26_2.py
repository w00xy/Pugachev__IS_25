# Использую код из своего практического занятия номер 2

import tkinter as tk
from tkinter import messagebox


def convert_cm_to_meters():
    try:
        # Получаем значение из поля ввода
        number = entry.get()
        cm = int(number)
        cm = abs(cm)
        if type(cm) == int:
            metre = cm // 100
            result_label.config(text=f"{cm} - {metre} полных метров")
        else:
            raise ValueError
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректное значение.")


# Создаем главное окно приложения
root = tk.Tk()
root.title("Конвертер сантиметров в метры")

# Создаем и располагаем элементы интерфейса
label = tk.Label(root, text="Введите расстояние (в сантиметрах):")
label.pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)

convert_button = tk.Button(root, text="Конвертировать", command=convert_cm_to_meters)
convert_button.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=5)

# Запуск главного цикла приложения
root.mainloop()