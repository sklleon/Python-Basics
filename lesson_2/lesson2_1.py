# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

m = [2, 'text', 456, 45.3, None, 8, 9, 10]
for i in m:
    print(type(i))