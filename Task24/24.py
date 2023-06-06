import random
kust = int(input("введите количество кустов: "))
berryes = list(random.randint(0, 10) for i in range(kust))
maxsumma = 0
i = 0
sum = 0
k = 0
print(berryes)

while (i < kust):
    if i >= kust - 2:
        maxsumma = max(maxsumma, berryes[i] + berryes[k] + berryes[k+1])
        k += 1
        i += 1
    else:
        maxsumma = max(maxsumma, berryes[i] + berryes[i+1] + berryes[i+2])
        i += 1
print(maxsumma)