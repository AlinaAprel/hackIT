from passenger_data import passengers

# Пример использования циклов и обработки данных
def process_passenger_data():
    
    print("Список всех пассажиров:")
    # Цикл для вывода всей информации о пассажирах
    for passenger in passengers:
        
    
    print("\nПроверка возраста пассажиров:")
    # Цикл для проверки возраста пассажиров
    for passenger in passengers:
        if :
            print()
        else:
            print()

    print("\nПассажиры на самолете Boeing:")
    # Фильтрация пассажиров, летящих на Boeing
    

    print("\nПроверка времени вылета:")
    # Проверка времени вылета пассажиров
    for passenger in passengers:
        time = passenger[5]
        hour = int(time.split()[1].split(":")[0])  # Извлечение часа
        if hour < 12:
            print()
        else:
            print()

# Вызов функции обработки данных
if __name__ == "__main__":
    process_passenger_data()
