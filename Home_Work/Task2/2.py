a = int(input())
suma = 0
for index in enumerate(str(a)):
    suma += int(index[1])
print(suma)