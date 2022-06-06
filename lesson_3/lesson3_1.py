# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def two_numbers(a, b):
    if b == 0:
        print('Ошибка! Делить на ноль нельзя')
    else:
        try:
            return a / b
        except ValueError as err:
            print(err)


print(two_numbers(int(input('Введите первое число: ')), int(input('Введите второе число: '))))