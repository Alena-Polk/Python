def func_compute(nun):
    def apple(x):
        return nun * x

    return apple


res = func_compute(2)
print(res(15))
print(res(20))
res = func_compute(3)
print(res(15))
print(res(20))
