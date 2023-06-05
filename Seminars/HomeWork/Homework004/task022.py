# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input('Введите колчиство элементов первого множества: '))
m = int(input('Введите количество элементов второго множества: '))

plentyN = []
plentyM = []
plentyResult = []

print('Введите числа первого множества: ')
while len(plentyN) < n:
    plentyN.append(int(input()))
print('Введите числа второго множества: ')
while len(plentyM) < m:
    plentyM.append(int(input()))

plentyN = set(plentyN)
plentyM = set(plentyM)

plentyResult = plentyN.intersection(plentyM)
# plentyResult = sorted(list(plentyResult))

print(plentyN)
print(plentyM)

print(plentyResult)

plentyResult = list(plentyResult)

def QuikSort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greatest = [i for i in array[1:] if i > pivot]

        return QuikSort(less) + [pivot] + QuikSort(greatest)

print(QuikSort(plentyResult))

