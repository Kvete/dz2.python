"""
2) Для списка реализовать обмен значений соседних элементов, т.е. значениями
 обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве
 элементов последний сохранить на своем месте. Для заполнения списка элементов
  необходимо использовать функцию input().
"""
user_list = input('give me list ').split()
print(user_list)
for i in range(0, len(user_list) - 1, 2):
    temp = user_list[i]
    user_list[i] = user_list[i + 1]
    user_list[i + 1] = temp
print(user_list)
