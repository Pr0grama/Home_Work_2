list = []
n = int(input('Введите кол-во чисел: '))
for i in range(n):
    list.append(int(input('Введите число в массив: ')))

maxi = int(input('Введите максимальное: '))
mini = int(input('Введите минимальное: '))
for i in range(n):
    if mini <= list[i] <= maxi:
        print(i)