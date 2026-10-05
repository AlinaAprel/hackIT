def my_hex(number: int) -> str:
    if number == 0:
        return "0x0"
    
    is_negative = number < 0
    number = abs(number)
    
    # Создаем строку-алфавит
    hex_digits = "0123456789abcdef"
    
    result = ""
    
    while number > 0:
        # Получаем остаток от деления на 16. Это будет число от 0 до 15.
        remainder = number % 16
        result = hex_digits[remainder] + result
        number = number // 16
        
    if is_negative:
        return "-0x" + result
    return "0x" + result

print(my_hex(145345))