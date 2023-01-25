def apple(tpl):
    pear = []
    [pear.append(one) for one in reversed(tpl) if one not in pear]
    return tuple(pear)


print(apple([1, 2, 3, 3, 2]))
print(apple([2, 1, 3, 1, 2, 5, 5, 9, 2, 0, 0]))
