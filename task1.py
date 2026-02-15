numbers = []

size = int(input("Введіть кількість елементів списку: "))

for i in range(size):
    num = int(input("Введіть число: "))
    numbers.append(num)

n = int(input("Введіть кількість позицій для зсуву вправо: "))

n = n % size

shifted = []

for i in range(size - n, size):
    shifted.append(numbers[i])

for i in range(0, size - n):
    shifted.append(numbers[i])

print("Зсунутий список:", shifted)
