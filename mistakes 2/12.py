def get_max_value(numbers):
    mx_value = number[0]
    for num in numbers:
        if num > mx_value:
            mx_value = num
    return mx_value

nums = [3, 7, "10", 2]
print(f"Максимальное значение: {get_max_value(nums)}")
