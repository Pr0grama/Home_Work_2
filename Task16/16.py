n = int(input())
a = [None] * n
print('Элементы массива: ')
for i in range(n):
    a[i] = int(input())
x = int(input('Поиск числа: '))
print(f"Кол-во чисел {x} в массиве равно {a.count(x)}")