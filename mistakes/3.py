names = ["Alice", "Bob", "Charlie", 12345]
counter = 0

for name in names:
    if name.isalpha():
        counter += 1

print("Количество имен:", counter)
