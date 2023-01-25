a = {'emp1': {'name': 'Jhon', 'salary': 7500},
     'emp2': {'name': 'Emma', 'salary': 8000},
     'emp3': {'name': 'Brad', 'salary': 6500},
     }
item = a.pop('emp3')
print(item)
z = item.pop('salary')
print(z)
b = a.setdefault('emp3', {'name': 'Brad', 'salary': 8500})
for x in a:
    print(x)
    for y in a[x]:
        print(y, ": ", a[x][y], sep='')
