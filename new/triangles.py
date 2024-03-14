def insert_asterisks(matr, L, R):
    n = len(matr)
    for i in range(n):
        for j in range(n):
            if eval(L) <= j <= eval(R):
                matr[i][j] = '*'


_1 = 'i'
_2 = 'n-i-1'


def U(matr):
    insert_asterisks(matr, _1, _2)


def D(matr):
    insert_asterisks(matr, _2, _1)


def L(matr):
    insert_asterisks(matr, '0', f'min({_1}, {_2})')


def R(matr):
    insert_asterisks(matr, f'max({_1}, {_2})', 'n-1')


def go():
    figure = {
        1: ['Верхний и правый треугольники', [U, R]],
        2: ['Левый и нижний треугольники', [L, D]],
        3: ['Верхний треугольник', [U]],
        4: ['Нижний треугольник', [D]],
        5: ['Верхний и нижний треугольники', [U, D]],
        6: ['Левый и правый треугольники', [L, R]],
        7: ['Левый треугольник', [L]],
        8: ['Правый треугольник', [R]],
        9: ['Верхний и левый треугольники', [U, L]],
        10: ['Правый и нижний треугольники', [R, D]]
    }

    def input_fig_num():
        while True:
            print()
            for k, v in figure.items():
                print(f'{k}. {v[0]}')
            num = int(input('\nВыберите номер фигуры: '))
            if num in figure:
                return num

    while True:
        num = input_fig_num()
        size = int(input('Введите длину стороны квадрата: '))
        if size % 2 == 0:
            size -= 1
        matr = [[' '] * size for _ in range(size)]
        for fun in figure[num][1]:
            fun(matr)
        print(f'\n{num}.{figure[num][0].upper()}:')
        for row in matr:
            print(*row)
        if input('Выйти из программы(1)?: ') == '1':
            break


go()