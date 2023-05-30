import math as m
summa = int(input("Введите сумму чисел: "))
proz = int(input('Введите произведение чисел: '))
if m.sqrt(summa**2 - 4 * proz) >= 0:
    x1 = (summa + m.sqrt(summa**2 - 4 * proz))//2
    x2 = (summa - m.sqrt(summa**2 - 4 * proz))//2
    print(int(x1), int(x2))
else:
    print("Таких чисел нету")