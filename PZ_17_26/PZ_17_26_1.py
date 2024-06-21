import tkinter as tk
from tkinter import ttk


def create_main_window():
    root = tk.Tk()
    root.title("Параметры скидки")
    root.geometry("800x600")

    label_style = ttk.Style()
    label_style.configure("My.TLabel",
                          font="helvetica 11",
                          foreground="#2F261E",
                          )

    # Создание вкладок
    tab_control = ttk.Notebook(root)
    tabs = ["Скидка", "Условия", "Ограничения", "Купоны", "Дополнительно"]
    for tab_name in tabs:
        frame = ttk.Frame(tab_control)
        tab_control.add(frame, text=tab_name)
    tab_control.pack(expand=1, fill='both')

    # Теперь создаем элементы внутри первой вкладки
    frame = tab_control.nametowidget(tab_control.winfo_children()[0])

    # Параметры скидки
    ttk.Label(frame, text="Параметры скидки", font=('Helvetica', 16)).pack(anchor='w', pady=10, padx=10)

    # Создание формы
    form_frame = ttk.Frame(frame)
    form_frame.pack(padx=10, pady=10, fill='x')

    # Активность
    ttk.Label(form_frame, text="Активность:", style="My.TLabel").grid(row=0, column=0, sticky='w')
    ttk.Checkbutton(form_frame).grid(row=0, column=1, sticky='w')

    # Название
    ttk.Label(form_frame, text="Название:", style="My.TLabel").grid(row=1, column=0, sticky='w')
    ttk.Entry(form_frame, width=60).grid(row=1, column=1, sticky='w')

    # Сайт
    ttk.Label(form_frame, text="Сайт:", style="My.TLabel").grid(row=2, column=0, sticky='w')
    site_combo = ttk.Combobox(form_frame, values=["(s1) Моя компания"])
    site_combo.grid(row=2, column=1, sticky='w')
    site_combo.set("(s1) Моя компания")

    # Период активности
    ttk.Label(form_frame, text="Период активности:", style="My.TLabel").grid(row=3, column=0, sticky='w')
    period_combo = ttk.Combobox(form_frame, values=["Интервал"])
    period_combo.grid(row=3, column=1, sticky='w')
    period_combo.set("Интервал")

    # Дата с
    ttk.Entry(form_frame).grid(row=3, column=2, padx=5)
    ttk.Button(form_frame, text="📅").grid(row=3, column=3, padx=5)

    # Дата по
    ttk.Entry(form_frame).grid(row=3, column=4, padx=5)
    ttk.Button(form_frame, text="📅").grid(row=3, column=5, padx=5)

    # Тип скидки
    ttk.Label(form_frame, text="Тип скидки:", style="My.TLabel").grid(row=4, column=0, sticky='w')
    type_combo = ttk.Combobox(form_frame, values=["В процентах"])
    type_combo.grid(row=4, column=1, sticky='w')
    type_combo.set("В процентах")

    # Величина скидки
    ttk.Label(form_frame, text="Величина скидки:", style="My.TLabel").grid(row=5, column=0, sticky='w')
    ttk.Entry(form_frame, width=5).grid(row=5, column=1, sticky='w')

    # Валюта скидки
    ttk.Label(form_frame, text="Валюта скидки:", style="My.TLabel").grid(row=6, column=0, sticky='w')
    currency_combo = ttk.Combobox(form_frame, values=["RUB"])
    currency_combo.grid(row=6, column=1, sticky='w')
    currency_combo.set("RUB")

    # Максимальная сумма скидки
    ttk.Label(form_frame, text="Максимальная сумма скидки (в валюте скидки):", style="My.TLabel").grid(row=7, column=0, sticky='w')
    ttk.Entry(form_frame).grid(row=7, column=1, sticky='w')

    # Применяется к продлению подписки
    ttk.Label(form_frame, text="Применяется к продлению подписки:", style="My.TLabel").grid(row=8, column=0, sticky='w')
    ttk.Checkbutton(form_frame).grid(row=8, column=1, sticky='w')

    # Приоритет применимости
    ttk.Label(form_frame, text="Приоритет применимости:", style="My.TLabel").grid(row=9, column=0, sticky='w')
    ttk.Entry(form_frame).grid(row=9, column=1, sticky='w')

    # Прекратить дальнейшее применение скидок
    ttk.Label(form_frame, text="Прекратить дальнейшее применение скидок:").grid(row=10, column=0, sticky='w')
    ttk.Checkbutton(form_frame).grid(row=10, column=1, sticky='w')

    # Краткое описание
    ttk.Label(form_frame, text="Краткое описание (до 255 символов):", style="My.TLabel").grid(row=11, column=0, sticky='w')
    tk.Text(form_frame, height=5, width=60).grid(row=11, column=1, padx=5, pady=5, sticky='w')

    # Кнопки управления
    button_frame = ttk.Frame(frame)
    button_frame.pack(pady=10)

    ttk.Button(button_frame, text="Сохранить").grid(row=0, column=0, padx=5)
    ttk.Button(button_frame, text="Применить").grid(row=0, column=1, padx=5)
    ttk.Button(button_frame, text="Отменить").grid(row=0, column=2, padx=5)

    root.mainloop()

if __name__ == "__main__":
    create_main_window()