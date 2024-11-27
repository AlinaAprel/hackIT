import tkinter as tk
from tkinter import messagebox

# Функция для проверки условий
def check_registration():
    try:
        age = int(age_entry.get())
        passport = passport_var.get()
        visa = visa_var.get()

        if age < 18:
            messagebox.showerror("Ошибка", "Вам должно быть не менее 18 лет для регистрации.")
        elif not passport:
            messagebox.showerror("Ошибка", "Для регистрации необходим заграничный паспорт.")
        elif not visa:
            messagebox.showerror("Ошибка", "Для регистрации необходима виза.")
        else:
            messagebox.showinfo("Успех", "Вы успешно зарегистрировались!")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректный возраст.")

# Создаем главное окно
root = tk.Tk()
root.title("Регистрация в аэропорту")

# Настройки шрифта

# Метка и поле ввода возраста
age_label = tk.Label(root, text="Введите ваш возраст:", # Добавь параметры)
age_label.pack(# Добавь параметры)

age_entry = tk.Entry(root, # Добавь параметры)
age_entry.pack(# Добавь параметры)

# Чекбокс для заграничного паспорта
passport_var = tk.BooleanVar()
passport_check = tk.Checkbutton(root, #Добавь параметры)
passport_check.pack(# Добавь параметры)

# Чекбокс для визы
visa_var = tk.BooleanVar()
visa_check = tk.Checkbutton(root, # Добавь параметры)
visa_check.pack(# Добавь параметры)

# Кнопка для проверки
check_button = tk.Button(root, text="Проверить регистрацию", command=check_registration, 
                         font=font_button, bg="#4682B4", fg="#FFFFFF", bd=3, relief="raised")
check_button.pack(pady=20)

# Запуск основного цикла программы
root.mainloop()
