"""
5) Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор
натуральных чисел.У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент
с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например,
 my_list = [7, 5, 3, 3, 2].
"""
my_list = [7, 5, 3, 3, 2]
print(my_list)
user_number = int(input('give me number '))
for i in range(len(my_list)):
    if my_list[len(my_list) - 1] >= user_number:
        my_list.append(user_number)
        break
    elif user_number > my_list[i]:
        my_list.insert(i, user_number)
        break
print(my_list)
