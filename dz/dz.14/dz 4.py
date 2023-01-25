def dw(n):
    s = ''
    while n > 0:
        s = str(n % 2) + s
        n //= 2
    return s


while 1:
    n = int(input('->'))
    if n != 0:
        print(dw(n))
    else:
        break


