import tkinter as tk
from tkinter import ttk


def create_main_window():
    root = tk.Tk()
    root.title("Параметры скидки")
    root.geometry("800x600")

<<<<<<< HEAD
    label_style = ttk.Style()
    label_style.configure("My.TLabel",
                          font="helvetica 11",
                          foreground="#2F261E",
                          )

=======
>>>>>>> origin/main
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
<<<<<<< HEAD
    ttk.Label(frame, text="Параметры скидки", font=('Helvetica', 16)).pack(anchor='w', pady=10, padx=10)
=======
    tk.Label(frame, text="Параметры скидки", font=('Helvetica', 14)).pack(anchor='w', pady=10, padx=10)
>>>>>>> origin/main

    # Создание формы
    form_frame = ttk.Frame(frame)
    form_frame.pack(padx=10, pady=10, fill='x')

    # Активность
<<<<<<< HEAD
    ttk.Label(form_frame, text="Активность:", style="My.TLabel").grid(row=0, column=0, sticky='w')
    ttk.Checkbutton(form_frame).grid(row=0, column=1, sticky='w')

    # Название
    ttk.Label(form_frame, text="Название:", style="My.TLabel").grid(row=1, column=0, sticky='w')
    ttk.Entry(form_frame, width=60).grid(row=1, column=1, sticky='w')

    # Сайт
    ttk.Label(form_frame, text="Сайт:", style="My.TLabel").grid(row=2, column=0, sticky='w')
=======
    tk.Label(form_frame, text="Активность:").grid(row=0, column=0, sticky='e', padx=[0,10])
    tk.Checkbutton(form_frame).grid(row=0, column=1, sticky='w')

    # Название
    tk.Label(form_frame, text="Название:").grid(row=1, column=0, sticky='e', padx=[0,10])
    tk.Entry(form_frame, width=60).grid(row=1, column=1, sticky='w')

    # Сайт
    tk.Label(form_frame, text="Сайт:").grid(row=2, column=0, sticky='e', padx=[0,10])
>>>>>>> origin/main
    site_combo = ttk.Combobox(form_frame, values=["(s1) Моя компания"])
    site_combo.grid(row=2, column=1, sticky='w')
    site_combo.set("(s1) Моя компания")

    # Период активности
<<<<<<< HEAD
    ttk.Label(form_frame, text="Период активности:", style="My.TLabel").grid(row=3, column=0, sticky='w')
=======
    tk.Label(form_frame, text="Период активности:").grid(row=3, column=0, sticky='e', padx=[0,10])
>>>>>>> origin/main
    period_combo = ttk.Combobox(form_frame, values=["Интервал"])
    period_combo.grid(row=3, column=1, sticky='w')
    period_combo.set("Интервал")

<<<<<<< HEAD
    # Дата с
    ttk.Entry(form_frame).grid(row=3, column=2, padx=5)
=======

    # Дата с
    tk.Entry(form_frame).grid(row=3, column=2, padx=5)
>>>>>>> origin/main
    ttk.Button(form_frame, text="📅").grid(row=3, column=3, padx=5)

    # Дата по
    ttk.Entry(form_frame).grid(row=3, column=4, padx=5)
    ttk.Button(form_frame, text="📅").grid(row=3, column=5, padx=5)

    # Тип скидки
<<<<<<< HEAD
    ttk.Label(form_frame, text="Тип скидки:", style="My.TLabel").grid(row=4, column=0, sticky='w')
=======
    ttk.Label(form_frame, text="Тип скидки:").grid(row=4, column=0, sticky='e', padx=[0,10])
>>>>>>> origin/main
    type_combo = ttk.Combobox(form_frame, values=["В процентах"])
    type_combo.grid(row=4, column=1, sticky='w')
    type_combo.set("В процентах")

    # Величина скидки
<<<<<<< HEAD
    ttk.Label(form_frame, text="Величина скидки:", style="My.TLabel").grid(row=5, column=0, sticky='w')
    ttk.Entry(form_frame, width=5).grid(row=5, column=1, sticky='w')

    # Валюта скидки
    ttk.Label(form_frame, text="Валюта скидки:", style="My.TLabel").grid(row=6, column=0, sticky='w')
=======
    ttk.Label(form_frame, text="Величина скидки:").grid(row=5, column=0, sticky='e', padx=[0,10])
    ttk.Entry(form_frame, width=5).grid(row=5, column=1, sticky='w')

    # Валюта скидки
    ttk.Label(form_frame, text="Валюта скидки:").grid(row=6, column=0, sticky='e', padx=[0,10])
>>>>>>> origin/main
    currency_combo = ttk.Combobox(form_frame, values=["RUB"])
    currency_combo.grid(row=6, column=1, sticky='w')
    currency_combo.set("RUB")

    # Максимальная сумма скидки
<<<<<<< HEAD
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
=======
    ttk.Label(form_frame, text="Максимальная сумма скидки (в валюте скидки):").grid(row=7, column=0, sticky='e', padx=[0,10])
    ttk.Entry(form_frame).grid(row=7, column=1, sticky='w')

    # Применяется к продлению подписки
    tk.Label(form_frame, text="Применяется к продлению подписки:").grid(row=8, column=0, sticky='e', padx=[0,10])
    tk.Checkbutton(form_frame).grid(row=8, column=1, sticky='w')

    # Приоритет применимости
    tk.Label(form_frame, text="Приоритет применимости:").grid(row=9, column=0, sticky='e', padx=[0,10])
    tk.Entry(form_frame).grid(row=9, column=1, sticky='w')

    # Прекратить дальнейшее применение скидок
    tk.Label(form_frame, text="Прекратить дальнейшее применение скидок:").grid(row=10, column=0, sticky='e', padx=[0,10])
    tk.Checkbutton(form_frame).grid(row=10, column=1, sticky='w')

    # Краткое


    # описание
    tk.Label(form_frame, text="Краткое описание (до 255 символов):").grid(row=11, column=0, sticky='e', padx=[0,10])
>>>>>>> origin/main
    tk.Text(form_frame, height=5, width=60).grid(row=11, column=1, padx=5, pady=5, sticky='w')

    # Кнопки управления
    button_frame = ttk.Frame(frame)
    button_frame.pack(pady=10)

<<<<<<< HEAD
    ttk.Button(button_frame, text="Сохранить").grid(row=0, column=0, padx=5)
    ttk.Button(button_frame, text="Применить").grid(row=0, column=1, padx=5)
    ttk.Button(button_frame, text="Отменить").grid(row=0, column=2, padx=5)

    root.mainloop()

=======
    tk.Button(button_frame, text="Сохранить", bg='green').grid(row=0, column=0, padx=5, pady=80)
    tk.Button(button_frame, text="Применить").grid(row=0, column=1, padx=5)
    tk.Button(button_frame, text="Отменить").grid(row=0, column=2, padx=5)

    root.mainloop()


>>>>>>> origin/main
if __name__ == "__main__":
    create_main_window()