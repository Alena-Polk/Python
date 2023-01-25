a = [int(input("Введите элемент списка: ")) for i in range(int(input("Введите длину списка: ")))]
print("Список:", a)
newlist = [int(x) for x in a if x > 0]
print("Новый список, состоящий из положительных элементов:", newlist)
max_number = max(a)
print("Наибольший элемент списка:", max_number)

