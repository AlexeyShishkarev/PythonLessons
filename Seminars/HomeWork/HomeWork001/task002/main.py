# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

number = int(input('Введите трехзначное число: '))
number1 = number
result = 0

while number1 != 0:
    result += number1 % 10
    number1 //= 10
print('Сумма чисел числа', number, ': ', result)



