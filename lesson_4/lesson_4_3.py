# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Решите задание в одну строку.
# Подсказка: используйте функцию range() и генератор.

num = range(20, 241)
new_list = [el for el in num if el % 20 == 0 or el % 21 == 0]
print(new_list)
