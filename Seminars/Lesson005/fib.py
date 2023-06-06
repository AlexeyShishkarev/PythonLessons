# Задача №31. Решение в группах
# Последовательностью Фибоначчи называется
# последовательность чисел
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21


number = int(input('Введите номер числа фиббоначи: '))


# def fib (number):
#     if number < 2:
#         return number
#     else:
#         return (fib(number-1) + fib(number-2))
#
# for i in range(number):
#     print(fib(i))

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,


numb1 = 0
numb2 = 1
fib = 0

if number == 1:
    print(0)

if number > 1:
    print(0)
    print(1)
for i in range(number - 2):
    fib = numb1 + numb2
    numb1 = numb2
    numb2 = fib
    print(fib)







