import random

def generate_joke():
    subjects = ["Программист", "Сисадмин", "Хакер", "Компьютер"]
    actions = ["пытался", "решил", "забыл", "сломал"]
    endings = [
        "перезагрузить сервер, а перезагрузил себя.",
        "поправить баг, а создал два новых.",
        "почистить реестр, а удалил систему.",
        "настроить Wi-Fi, а интернет пропал у всех."
    ]

    subject = random.choice(subjects)
    action = random.choice(actions)
    ending = random.choice(endings)

    return f"{subject} {action} {ending}"

# Главная часть программы
print("Генератор шуток")
print("-" * 30)

while True:
    print("\nВот ваша шутка:")
    print(generate_joke())
    choice = input("\nХотите еще одну? (да/нет): ").strip().lower()
    if choice != "да":
        print("Спасибо за использование генератора шуток! Пока!")
        break
