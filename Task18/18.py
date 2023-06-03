
n = int(input())
a = [None] * n
print('Элементы массива: ')
for i in range(n):
    a[i] = int(input())
x = int(input('Число: '))
mini = 10**10
for i in range(n):
    k = abs(x - a[i])
    if mini > k:
        mini = k
        z = a[i]
print(z)
        