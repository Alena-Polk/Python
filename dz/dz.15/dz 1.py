a = 'I am learning Python. hello, WORLD!'
b1 = a.find('h')
b2 = a.rfind('h')
c = a[:b1] + a[b2 + 1:]
print(c)
