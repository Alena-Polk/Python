import random as r

a = [r.randint(0, 100) for i in range(10)]
print(a)
a.sort(reverse=True)
print(a)

