# a = input("Введите строку: ")
a = "Привет, мир!"
gls = "аиоуюяыэеё"
b = []
for i in a:
    if i in gls:
        b.append(i)
print("Количество гласных равно:", len(b))
