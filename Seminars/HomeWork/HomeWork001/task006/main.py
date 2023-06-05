# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*

# 385916 -> yes
# 123456 -> no

number = int(input('Введите номер билета: '))
numberTemp = number
twoPartNumber = 0
onePartNumber = 0

while numberTemp // 1000 != 0:
    twoPartNumber += numberTemp % 10
    numberTemp //= 10

numberTemp = number // 1000

while numberTemp != 0:
    onePartNumber += numberTemp % 10
    numberTemp //= 10

if onePartNumber == twoPartNumber:
    print('YES')
else:
    print('NO')








