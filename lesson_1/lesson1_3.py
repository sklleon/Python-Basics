# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь
# ввёл число 3. Считаем 3 + 33 + 333 = 369.

p_num = int(input('Введите любое число: '))
f_num1 = int('%s' % p_num)
f_num2 = int('%s%s' % (p_num, p_num))
f_num3 = int('%s%s%s' % (p_num, p_num, p_num))
i_num = (f_num1 + f_num2 + f_num3)
print('Находим сумму чисел {} + {} + {}, Результат: {}'.format(f_num1, f_num2, f_num3, i_num))
