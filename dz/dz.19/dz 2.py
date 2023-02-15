a = open("dz19.txt", "w")
a.write("Замена строки в текстовом файле; \nизменить строку в списке; \nзаписать список в файл;")
a.close()

pos = int(input('Введите индекс, pos = '))
a = open("dz19.txt")
lst = a.readlines()
print(lst)
if (pos < len(lst)) and (pos >= 0):
    i = pos
    while i < len(lst) - 1:
        lst[i] = lst[i + 1]
        i = i + 1
    lst = lst[:-1]
a.close()

f = open("dz19.txt", "w")
for line in lst:
    f.write(line)

f.close()
print(lst)
