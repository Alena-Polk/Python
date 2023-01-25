def decor(*args):
    def args_dec(fn):
        def wrap(*x):
            print(*args, end='')
            print(*x, sep=', ', end='')
            print(' = ', end='')
            fn(*x)

        return wrap

    return args_dec


@decor("Сумма чисел: ")
def summa(*au):
    print(sum(au))


@decor('Среднее арифметическое чисел: ')
def avg(*ae):
    print(sum(ae) / len(ae))


summa(2, 3, 3, 4)
avg(2, 3, 3, 4)
