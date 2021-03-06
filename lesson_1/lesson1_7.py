# Спортсмен занимается ежедневными пробежками. В первый день его результат составил a
# километров. Каждый день спортсмен увеличивал результат на 10% относительно
# предыдущего. Требуется определить номер дня, на который результат спортсмена составит не
# менее b километров. Программа должна принимать значения параметров a и b и выводить
# одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на шестой день спортсмен достиг результата — не менее 3 км.

name = input(' Как я могу к Вам обращаться?: ')
a_km = int(input('Введите результат пробежки первого дня в км: '))
b_km = int(input('Введите ожидаемый результат пробежки в км: '))
day = 1
finish = a_km
if a_km >= b_km:
    print('Вы уже достигли ожидаемого результата')
else:
    while finish < b_km:
        a_km = a_km + (0.1 * a_km)
        day += 1
        finish = finish + a_km

print('На {} день, {} вы достигните результата'.format(day, name))
