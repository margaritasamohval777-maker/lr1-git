<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 330f97e (Сюда вставить описание измнений)
def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n * (n + 1) // 2):  # Достаточно для создания пирамиды
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def print_fibonacci_pyramid(rows):
    fib_sequence = fibonacci(rows)
    index = 0
    
    for i in range(1, rows + 1):
        # Печатаем пробелы для выравнивания
        print(" " * (rows - i), end='')
        for j in range(i):
            print(fib_sequence[index], end=' ')
            index += 1
        print()  # Переход на новую строку

# Укажите количество строк пирамиды
rows = 19
<<<<<<< HEAD
print_fibonacci_pyramid(rows) #рита самохвал

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

# Добавьте вызов функции в конец файла
print(f"Факториал числа {rows}: {factorial(rows)}")
=======
����� �뢮�� ������ �� ��࠭ (ECHO) ����祭.
>>>>>>> d07cd86 (Initial commit)
=======
print_fibonacci_pyramid(rows) #рита самохвал
>>>>>>> 330f97e (Сюда вставить описание измнений)
