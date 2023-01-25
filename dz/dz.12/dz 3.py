students = [
    {'name': 'Jennifer', 'final': 95},
    {'name': 'David', 'final': 92},
    {'name': 'Nikolas', 'final': 98}]

a = sorted(students, key=lambda item: item['name'])
print(a)
res = sorted(students, key=lambda item: item['final'], reverse=True)
print(res)
