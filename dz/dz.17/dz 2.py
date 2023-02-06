def neg_numbers(num):
    if len(num) == 0:
        return 0
    else:
        count = neg_numbers(num[1:])
        if num[0] < 0:
            count += 1
        return count


n = [3, -5, 11, 2, -7, 8, -2]
print('n =', neg_numbers(n))
