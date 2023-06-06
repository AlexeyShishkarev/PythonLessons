# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
#
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

a = int(input('Введите число А: '))
b = int(input('Введите степень А: '))
sum = a
def multi(a, b, sum):
    if b == 0:
        return 1
    if b == 1:
        return sum
    sum *= a
    return multi(a, b - 1, sum)

print(multi(a, b, sum))






