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

# Метка и поле ввода возраста
age_label = tk.Label(root, text="Введите ваш возраст:")
age_label.pack()

age_entry = tk.Entry(root)
age_entry.pack()

# Чекбокс для заграничного паспорта
passport_var = tk.BooleanVar()
passport_check = tk.Checkbutton(root, text="У меня есть заграничный паспорт", variable=passport_var)
passport_check.pack()

# Чекбокс для визы
visa_var = tk.BooleanVar()
visa_check = tk.Checkbutton(root, text="У меня есть виза", variable=visa_var)
visa_check.pack()

# Кнопка для проверки
check_button = tk.Button(root, text="Проверить регистрацию", command=check_registration)
check_button.pack()

# Запуск основного цикла программы
root.mainloop()


