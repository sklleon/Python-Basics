# 3. Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

firm = {'Иванов': 170, 'Петров': 210, 'Сидоров': 190, 'Галкин': 150}
try:
    file_obj = open("test_3.txt", 'w')
    for last_name, salary in firm.items():
        file_obj.write(last_name + ':' + str(salary) + "\n")
except IOError:
    print(f"Произошла ошибка {IOError} ввода-вывода!")
finally:
    file_obj.close()
summa = 0
count = 0
persons = []
with open("test_3.txt", "r") as file_obj:
    for line in file_obj:
        print(line, end="")
        tokens = line.split(':')
        if int(tokens[1]) <= 200:
            persons.append(tokens[0])
        summa += int(tokens[1])
        count += 1
result = summa / count
print(f"Сотрудники {persons} имеет оклад менее 200 тысяч")
print(f"Подсчёт средней величины дохода сотрудников: {result}")
