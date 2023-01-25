# s1 = input("Введите первую строку: ")
# s2 = input("Введите вторую строку: ")
s1 = 'Python'
s2 = 'Programming language'
s = set(s1)-set(s2)
print("Искомыми буквами являются: ")
for i in s:
    print(i, end=" ")