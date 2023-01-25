# s1 = input("Введите первую строку: ")
# s2 = input("Введите вторую строку: ")
s1 = 'test'
s2 = 'string'
s = list(set(s1) | set(s2))
print("Искомыми буквами являются: ")
for i in s:
    print(i, end=" ")
