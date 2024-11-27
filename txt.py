import os


filenames = ["1.txt", "2.txt", "3.txt"]

# Функция для подсчета количества строк в файле
def count_lines(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return sum(1 for line in file)

# Объединение файлов в результирующий файл
with open('result.txt', 'w', encoding='utf-8') as result_file:
    sorted_filenames = sorted(filenames, key=count_lines)
    
    for filename in sorted_filenames:
        with open(filename, 'r', encoding='utf-8') as input_file:
            lines = input_file.readlines()  # Читаем весь файл целиком
        
        # Запись служебной информации
        result_file.write(f"{filename}\n")
        result_file.write(f"{len(lines)}\n")
        
        # Запись содержимого файла
        result_file.writelines(lines)