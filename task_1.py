'''
Задача 2: Найдите сумму цифр трехзначного числа.
*Пример:*
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)
'''

А = int(input("Введите трехзначное число: "))
C = А % 10
B = А // 10 % 10
А //= 100
print(f"Сумма цифр равна: {А + B + C}")

