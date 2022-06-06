# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

translater = {'One': 'odin', 'Two': 'dva', 'Three': 'tri', 'Four': 'chetyre'}
my_list = []
result = []
try:
    file_obj = open("test_out.txt", 'r')
    for line in file_obj:
        tokens = line.split(" - ")
        print(tokens)
        if tokens[0] in translater:
            word = translater[tokens[0]]
            result.append(word + ' - ' + tokens[1])
    print(result)
except IOError:
    print(f"Произошла ошибка {IOError} ввода-вывода!")
finally:
    file_obj.close()

try:
    file_input = open("test_in.txt", "w")
    file_input.writelines(result)
except IOError:
    print(f"Произошла ошибка {IOError} ввода-вывода!")
finally:
    file_input.close()
