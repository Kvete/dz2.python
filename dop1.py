"""
Напишите программу, которая принимает на вход вещественное число и
показывает сумму его цифр.
Пример:
- 6782 -> 23
- 0,56 -> 11
"""
n = input('give me number ')
sum_of_digits = 0

for i in range(len(n)):
    if n[i] == '.' or n[i] == '-' or n[i] == ',':
        continue
    sum_of_digits += int(n[i])
print(f'summ of digit in number {n}={sum_of_digits}')
