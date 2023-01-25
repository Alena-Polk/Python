students = [
    {'name': 'Jennifer', 'final': 95},
    {'name': 'David', 'final': 92},
    {'name': 'Nikolas', 'final': 98}]

a = max(students, key=lambda item: item['final'])
print(a)
b = min(students, key=lambda item: item['final'])
print(b)
