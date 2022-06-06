# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и dict.

seasons = ['Зима',
           'Весна',
           'Лето',
           'Осень']
months = {
    1: 'Январь',
    2: 'Февраль',
    3: 'Март',
    4: 'Апрель',
    5: 'Май',
    6: 'Июнь',
    7: 'Июль',
    8: 'Август',
    9: 'Сентябрь',
    10: 'Октябрь',
    11: 'Ноябрь',
    12: 'Декабрь'
}

cho = int(input('Введите месяц в виде целого числа от 1 до 12: '))

if cho == 12 or cho == 1 or cho == 2:
    print(f'Это месяц: ', months.get(cho))
    print(f'И сезон: ', seasons[0])
elif cho == 3 or cho == 4 or cho == 5:
    print(f'Это месяц: ', months.get(cho))
    print(f'И сезон: ', seasons[1])
elif cho == 6 or cho == 7 or cho == 8:
    print(f'Это месяц: ', months.get(cho))
    print(f'И сезон: ', seasons[2])
elif cho == 9 or cho == 10 or cho == 11:
    print(f'Это месяц: ', months.get(cho))
    print(f'И сезон: ', seasons[3])
else:
    print("Какой ты скучный")
