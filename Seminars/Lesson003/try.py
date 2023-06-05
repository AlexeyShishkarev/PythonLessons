
list_1 = input('Введите слово: ').upper()

dict_price = {1 : 'AEIOULNSTRАВЕИНОРСТ',
              2 : 'DGДКЛМПУ',
              3 : 'BCMPБГЁЬЯ',
              4 : 'FHVWYЙЫ',
              5 : 'KЖЗХЦЧ',
              8 : 'JXШЭЮ',
              10 : 'QZФЩЪ'}

summ = 0

for i in list_1:
    for key, value in dict_price.items():
        if i in value:
            summ += key

print(summ)
