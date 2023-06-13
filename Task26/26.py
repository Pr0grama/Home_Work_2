def f(a,b):
    if b == 0:
        return 1
    else:
        return a * f(a,b-1)
    
a = int(input("Введите число "))
b = int(input("Введите степень числа "))
print(f(a,b))