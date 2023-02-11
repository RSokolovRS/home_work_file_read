import os
    
my_list = []
my_dict = {}

def read_file(): # Создаем пустую функцию.
    for fn in os.listdir('folder'): # Определяем папку и проходимся циклом по содержимому папки.
        with open(os.path.join('folder', fn), 'r', encoding = 'utf-8') as file: # Открываем файлы в папке.
            f = file.readlines() # Читаем и записываем каждый файл в переменную в цикле по кол-ву файлов.
        my = {fn: f} # Создаем словарь с ключем (название файлов "fn") и значением(списком "f").
        my_dict.update(my) # Добавляем словарь в пустой словарь.
    return my_dict # Возвращаем словарь в функцию.

read_dict = read_file() # Обьевляем переменную для функции.

def list_read(): # Создаем функцию для сортировки значения словаря по кол-ву строк в значении словаряю.
    for i in read_dict.values():
        my_list.append(i)
    my_list.sort(key=len)
    return my_list

l_read = list_read()

# Цикл для сравнения списков и последовательной записи результата в один файл.
for s in l_read:
    for j, v in read_dict.items():
        if v == s:
            with open('folder/4.txt', 'a', encoding = 'utf-8') as file_1:
                f1 = file_1.writelines(f'{j} \n')
                f2 = file_1.writelines(f'Количество строк: {len(s)} \n')
                f3 = file_1.writelines(f'{s} \n\n')
        else:
            print('совпадений не обнаружено!')

