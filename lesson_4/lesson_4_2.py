# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для его формирования используйте генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

def com(a, b):
    print(a * b)


my_list = [15, 16, 17, 2, 3, 4, 16, 1, 5, 4, 10, 20]
my_then = [my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num - 1]]
print(my_then)

com('*', 10)

i = 0
new = []
for el in my_list:
    if el > my_list[i - 1]:
        new.append(el)
    i += 1
print(new)
