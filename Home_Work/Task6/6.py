a = input()
suma1 = 0
suma2 = 0
for i in range(len(a)):
    suma1 += int(a[i])
    suma2 += int(a[len(a)-i-1])
if suma1 == suma2:
    print('Yes')
else:
    print('No')