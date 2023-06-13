def summ(a,b):
    if a == 0:
        return b
    else:
        return summ(a-1,b+1)

a = int(input("Введите число "))
b = int(input("Введите степень числа "))
print(summ(a,b))