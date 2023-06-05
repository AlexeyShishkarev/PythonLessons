# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

import random

list_1 = list()

for i in range(0, 10):
    n = random.randint(0, 1)
    list_1.append(n)

print(list_1)

list_1 = set(list_1)
print(len(list_1))






