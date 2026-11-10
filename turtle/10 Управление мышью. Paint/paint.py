import turtle

# 1. НАСТРОЙКА ЭКРАНА И ЧЕРЕПАШКИ
screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(0)              
t.pensize(5)            
t.shape("circle")       # Кисточка - кружок
t.shapesize(0.5)

# 2. МАССИВ ЦВЕТОВ (Палитра)
palette = ["black", "red", "blue", "green", "yellow"]
t.color(palette[0])

# 3. ФУНКЦИИ СМЕНЫ ЦВЕТА
def set_color_0(): t.color(palette[0])
def set_color_1(): t.color(palette[1])
def set_color_2(): t.color(palette[2])
def set_color_3(): t.color(palette[3])
def set_color_4(): t.color(palette[4])

def clear_canvas():
    t.clear()

# 4. ПРИВЯЗКА КЛАВИАТУРЫ
screen.listen()
screen.onkeypress(set_color_0, "1")
screen.onkeypress(set_color_1, "2")
screen.onkeypress(set_color_2, "3")
screen.onkeypress(set_color_3, "4")
screen.onkeypress(set_color_4, "5")
screen.onkeypress(clear_canvas, "c")

# ==========================================
# 5. ИДЕАЛЬНАЯ ЛОГИКА РИСОВАНИЯ МЫШЬЮ
# ==========================================

# ШАГ А: Что делать при первоначальном клике (телепортация без следа)
def start_drawing(x, y):
    t.penup()      # Поднимаем перо, чтобы не нарисовать линию из прошлой точки
    t.goto(x, y)   # Перемещаемся в точку клика
    t.pendown()    # Опускаем перо
    # t.dot(t.pensize()) # Раскомментировать, если хотите, чтобы обычный клик без движения ставил точку

# ШАГ Б: Что делать при перетаскивании (зажали кнопку и ведем)
def draw(x, y):
    # Хитрость turtle: отключаем ondrag на долю секунды, пока рисуем текущую линию, 
    # чтобы программа не "захлебнулась" от количества координат мыши (убирает лаги)
    t.ondrag(None) 
    
    t.goto(x, y)   # Рисуем линию к новой позиции мыши
    
    # Снова включаем ondrag, чтобы продолжить рисовать
    t.ondrag(draw, 1)

# ПРИВЯЗЫВАЕМ СОБЫТИЯ К МЫШИ
# Когда просто кликаем ЛЕВОЙ кнопкой (1) - срабатывает start_drawing
screen.onscreenclick(start_drawing, 1)

# Когда зажимаем ЛЕВУЮ кнопку (1) и ведем мышь - срабатывает draw
t.ondrag(draw, 1)

turtle.done()