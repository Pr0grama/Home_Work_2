point = {1:"AEIOULNSTRАВЕИНОРСТ",
                2:"DGДКЛМПУ",
                3:"BCMPБГЁЬЯ",
                4:"FHVWYЙЫ",
                5:"KЖЗХЦЧ",
                8:"JXШЭЮ",
                10:"QZФЩЪ"}

word = input('Введите слово: ').upper()
summ = 0
for i in word:
    for k,v in point.items():
        if i in v:
            summ += k
print(summ)