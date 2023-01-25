import random as r

w, h = 3, 4
matrix = [[r.randint(0, 4) for x in range(w)] for y in range(h)]
p = 1
for h in matrix:
    for w in h:
        print(w, end='\t\t')
        if w > 0:
            p *= w
    print()

print('Произведение ненулевых элементов:', p)

