# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, которые нужно 
# перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть


numberCoins = int(input("Введите количество монет: "))

headsCoins = 0 # количество монет орлом вверх 
tailsCoins = 0 # количество монет решкой вверх

for i in range(numberCoins):
    temp = int(input())

    if temp == 1:
        headsCoins += 1
    elif temp == 0:
        tailsCoins += 1

if headsCoins > tailsCoins:
    print(f'Нужно перевернуть {tailsCoins}')
else:
    print(f'Нужно вернуть {headsCoins}')


