symbol = None
count = int(input("Введите количество символов: "))
orientation = 0
while True:
    symbol = input("Тип символа: ")
    if len(symbol) == 1:
        break

while True:
    orientation = int(input("Ориентация линии: "))
    if orientation in [0, 1]:
        break

separator = ' ' if orientation == 0 else '\n'
for i in range(0, count):
    if i == count - 1:
        separator = '\n'
    print(symbol, end=separator)