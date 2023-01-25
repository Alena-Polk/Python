a = int(input("Введите количество копеек в диапазоне от 1 до 99: "))
c = a % 10
if a == 11 or a == 12 or a == 13 or a == 14:
    print(a, "копеек")
elif 1 <= a <= 99:
    print(a, "копе", end = "")
    if c == 1:
        print("йка ")
    if 2 <= c <= 4:
        print("йки ")
    if c == 0 or 5 <= c <= 9:
        print("ек ")
else:
    print("Ошибка ввода данных")