# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1



import random

number = int(input('Количество оценок: '))

ratingLog = []

for i in range(number):
    ratingLog.append(random.randint(1, 5))
print(ratingLog)


for i in range(number):
    if ratingLog[i] > 3:
        ratingLog[i] = 1

print(ratingLog)




