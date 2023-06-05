# Задача 18: Требуется найти в массиве A[1..N] 
# самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – 
# количество элементов в массиве. В последующих  строках записаны 
# N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

import random
import sys

n = int(input('Введите размер массива: '))
x = int(input('Введите число x: '))
number = 0
minimum = sys.maxsize
list_1 = list()

for i in range(0, n):
    num = random.randint(0, 10)
    list_1.append(num)

    if abs(x - list_1[i]) < minimum:
        number = list_1[i]
        minimum = abs(x - list_1[i])


print(list_1)
print(number)





