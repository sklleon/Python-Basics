# Поработайте с переменными, создайте несколько, выведите на экран. Запросите у
# пользователя некоторые числа и строки и сохраните в переменные, затем выведите на экран.

p_name = input('Введите свое имя: ')
print('Добро пожаловать:', p_name)
p_age = int(input('Введите Ваш возраст: '))
print('Через 20 лет {} Вам будет {}'.format(p_name, p_age + 20))
p_sity = input('Откуда ВЫ ? Вы из:')
print('Это прекрастно {} из {}'.format(p_name, p_sity))
