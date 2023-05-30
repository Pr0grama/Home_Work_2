n = int(input('Введите кол-во монет: '))
orel = reshka = 0
for i in range(n):
    x = int(input('Введите число 0 орёл или 1 решка: '))
    if x == 0:
        orel +=1 
    else:
        reshka += 1
print(f'Минимальное кол-во монет {min(orel,reshka)}')