"""
Напишите программу, которая принимает на вход число N и выдает набор
произведений чисел от 1 до N.
Пример:
- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
"""
n = int(input('give me number '))
list_fac = [1]
for i in range(1, n):
    list_fac.append((i + 1) * list_fac[i - 1])
print(list_fac)
