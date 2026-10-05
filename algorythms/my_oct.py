def my_oct(number: int) -> str:
    if number == 0:
        return "0o0"
    
    is_negative = number < 0
    number = abs(number)
    
    result = ""
    
    while number > 0:
        remainder = number % 8
        result = str(remainder) + result
        number = number // 8
        
    if is_negative:
        return "-0o" + result
    return "0o" + result
