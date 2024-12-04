def find_maximum(numbers):
    max_value = numbers[0]
    for num in number:
        if num > max_value:
            max_value = num
    return max_value

nums = [3, 7, 2, 8, 5]
print(f"Максимальное значение: {find_maximum(nums)}")
