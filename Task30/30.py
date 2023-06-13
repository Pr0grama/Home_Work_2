a1 = int(input('Введите начальное число: '))
d = int(input('Введите шаг: '))
n = int(input('Кол-во чисел: '))
res = []
for i in range(n):
    res.append(a1+i*d)
print(res)