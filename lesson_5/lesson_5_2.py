# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.

my_doc = ['Привет\n', 'Как твои дела\n', 'Пока\n']
with open("test_2.txt", 'w+') as file_obj:
    file_obj.writelines(my_doc)
with open("test.txt") as file_obj:
    lines = 0
    letters = 0
    for line in file_obj:
        lines += line.count("\n")
        letters = len(line)-1
        print(f"{letters} букв в {lines} строке")
    print(f"Всего обработано {lines} строк")