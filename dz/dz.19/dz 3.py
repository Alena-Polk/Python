a = [5, 9, 6, 7]
b = [3, 11, 8]
c = [2, 4]
d = [10, 1, 12]
f = a + b + c + d


def bubble(array, n):
    if n == 1:
        for i in range(len(array) - 1):
            for j in range(len(array) - i - 1):
                if array[j] < array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
    elif n == 2:
        for i in range(len(array) - 1):
            for j in range(len(array) - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]


print(f)
s = int(input("Выберите способ сортировки, где:\n 1 - сортировка по убыванию\n 2 - сортировка по возрастанию\n -> "))
bubble(f, s)
print(f)

