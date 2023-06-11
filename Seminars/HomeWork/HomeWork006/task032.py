# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint
list_1 = []
indexNumber = []

length = int(input('Введите размер массива: '))
minimum = int(input('Введите минимум: '))
maximum = int(input('Введите максимум: '))


for i in range(length):
    list_1.append(randint(-50, 50))
    if list_1[i] >= minimum and list_1[i] <= maximum:
        indexNumber.append(i)

print(list_1)
print(indexNumber)

