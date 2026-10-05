def my_bin(number: int) -> str:
    if number == 0:
        return "0b0"
    
    is_negative = number < 0
    number = abs(number)
    
    result = ""
    
    while number > 0:
        remainder = number % 2
        result = str(remainder) + result
        number = number // 2
        
    if is_negative:
        return "-0b" + result
    return "0b" + result

print(my_bin(17))