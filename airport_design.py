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
root.geometry("400x300")
root.config(bg="#F0F8FF")  # Устанавливаем фоновый цвет окна

# Настройки шрифта
font_label = ("Helvetica", 12, "bold")
font_entry = ("Helvetica", 12)
font_button = ("Helvetica", 10, "bold")

# Метка и поле ввода возраста
age_label = tk.Label(root, text="Введите ваш возраст:", font=font_label, bg="#F0F8FF", fg="#4682B4")
age_label.pack(pady=10)

age_entry = tk.Entry(root, font=font_entry, bg="#FFFFFF", fg="#000000", bd=2)
age_entry.pack(pady=5)

# Чекбокс для заграничного паспорта
passport_var = tk.BooleanVar()
passport_check = tk.Checkbutton(root, text="У меня есть заграничный паспорт", variable=passport_var, 
                                font=font_label, bg="#F0F8FF", fg="#4682B4", activebackground="#F0F8FF")
passport_check.pack(pady=5)

# Чекбокс для визы
visa_var = tk.BooleanVar()
visa_check = tk.Checkbutton(root, text="У меня есть виза", variable=visa_var, 
                            font=font_label, bg="#F0F8FF", fg="#4682B4", activebackground="#F0F8FF")
visa_check.pack(pady=5)

# Кнопка для проверки
check_button = tk.Button(root, text="Проверить регистрацию", command=check_registration, 
                         font=font_button, bg="#4682B4", fg="#FFFFFF", bd=3, relief="raised")
check_button.pack(pady=20)

# Запуск основного цикла программы
root.mainloop()
