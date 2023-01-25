try:
    operation = int(input("Введите цифру: "))
    i1 = int(input("Введите первое число: "))
    i2 = int(input("Введите второе число: "))
    if operation == 1:
        if i1 < 0 and i2 < 0:
            print("Результат:", i1 * (-1) + i2 * (-1))
        elif i1 < 0 and i2 > 0:
            print("Результат:", i1 * (-1) + i2)
        elif i1 > 0 and i2 < 0:
            print("Результат:", i1 + i2 * (-1))
        else:
            print("Результат:", i1 + i2)
    elif operation == 2:
        print("Результат:", (i1 + i2))
    elif operation == 3:
        print("Результат:", (i1 - i2))
    elif operation == 4:
        if i2 == 0:
            print("На ноль делить нельзя")
        else:
            print("Результат:", (int(i1 / i2)))
    elif operation == 5:
        print("Результат:", (i1 * i2))
    elif operation == 6:
        print("Результат:", (i1 % i2))
    elif operation == 7:
        minim = (i1 if i1 == i2 else i1 if i1 < i2 else i2)
        print("Результат:", minim)
    elif operation == 8:
        maxim = (i1 if i1 == i2 else i2 if i1 < i2 else i1)
        print("Результат:", maxim)
    else:
        print("Операция не поддерживается")
except ValueError:
    print("Нельзя вводить строки. Начните сначала.")
