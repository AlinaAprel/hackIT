import turtle

turtle.bgcolor("lightyellow")

t = turtle.Turtle()
t.shape("turtle")
t.shapesize(2)
t.penup() # Поднимаем перо, мы же хотим только ставить печати
t.speed(0)

# 1. Создаем массив цветов
palette = ["red", "blue", "green", "orange", "purple"]

# 2. Создаем переменную-счетчик, чтобы переключать цвета
color_index = 0

# 3. Пишем функцию, которая сработает по клику
# ВАЖНО: Функция обязательно должна принимать x и y в скобках!
def draw_stamp(x, y):
    global color_index # Говорим Python, что будем менять глобальную переменную
    
    # Телепортируемся в точку клика
    t.goto(x, y)
    
    # Берем цвет из массива по текущему индексу
    current_color = palette[color_index]
    t.color(current_color)
    
    # Оставляем отпечаток черепашки на экране
    t.stamp() 
    
    # Увеличиваем индекс на 1, чтобы в следующий раз взять следующий цвет
    color_index = color_index + 1
    
    # Если индекс вышел за пределы массива (стало 5, а цветов всего 5, индексы 0-4)
    # обнуляем его, чтобы начать круг заново!
    if color_index == len(palette): 
        color_index = 0

# 4. Привязываем клик левой кнопкой мыши (1 - левая кнопка) к функции
turtle.onscreenclick(draw_stamp, 1)

turtle.done()