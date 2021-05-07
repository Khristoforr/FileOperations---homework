import os
# Получаем список файлов из текущего каталога
list_of_files = os.listdir()
# Отфильтровываем файлы с расширением .txt
txt_files = [file for file in list_of_files if file.endswith('.txt')]

dict = {}
# Цикл для перебора каждого файла с целью подсчета кол-ва строк
for file in txt_files:
    with open(file, encoding='utf-8') as f:
        dict[file] = sum(1 for line in f)

# Записываем в новый файл
with open('file_to_write.txt', 'w', encoding='utf-8') as file_to_write:
    # Данная функция позволяет отсортировать список по значениям
    # для упорядоченной записи в новый файл
    for file in sorted(dict, key = lambda key: dict[key]):
        with open(file, 'r', encoding='utf-8') as file_to_read:
            # Для записи названия файла:
            file_to_write.write(str(file)+"\n")
            # Для записи кол-ва строк файла
            file_to_write.write(str(dict[file])+'\n')
            # Для записи содержимого файла
            file_to_write.write(file_to_read.read()+'\n')
