# Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и
# выведите в формате чч:мм:сс. Используйте форматирование строк.

import time

p_sec = int(input('Введите время в секундах:'))
f_res = time.gmtime(p_sec)
result = time.strftime('%H:%M:%S', f_res)
print('Переводим время в часы, минуты, секунды - в формате чч:мм:сс', result)

# var -2
# time = int(input('Enter the time in seconds: '))
# hours = time // 3600
# minutes = time // 60 - hours * 60
# seconds = time % 60
# print(f'{hours:02}:{minutes:02}:{seconds}:02')
