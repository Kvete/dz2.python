"""
3) Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому
 времени года относится месяц (зима, весна, лето, осень). Напишите решения
 через list и через dict.
"""
user_month = int(input('введите месяц '))
my_list = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето',
           'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
print(f'LIST месяц {user_month}=>{my_list[user_month - 1]}')

my_dict = {1: 'зима', 2: 'зима', 12: 'зима', 3: 'весна', 4: 'весна',
           5: 'весна', 6: 'лето', 7: 'лето', 8: 'лето', 9: 'осень',
           10: 'осень', 11: 'осень'}
print(f'DICT месяц {user_month}=>{my_dict[user_month]}')