import os

file_name = input('Введите имя файла: ')
if os.path.exists(file_name):
    name = os.path.basename(file_name)
    dirs = os.path.dirname(file_name)
    access_time = os.path.getmtime(file_name)
    print(f"Имя файла: {name}")
    print(f"Имя директории: {dirs}")
    print(f"Время последнего доступа к файлу: {access_time} сек.")
else:
    print('Файл не существует.')


