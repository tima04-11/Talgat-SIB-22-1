n = int(input("Введите число для таблицы умножения (от 1 до 10): "))

if 1 <= n <= 10:
    for i in range(1, n + 1):
        print(f"\nТаблица умножения для {i}:")
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")
else:
    print("Введите число от 1 до 10.")