a = []
n = int(input("Введите элементы списка:\nn = "))
for i in range(n):
    x = (int(input("-> ")))
    a.append(x)
ch = int(input("Введите число: \nch = "))
if ch in a:
    print("Число присутствует в элементах списка")
else:
    print("Число отсутствует в элементах списка")