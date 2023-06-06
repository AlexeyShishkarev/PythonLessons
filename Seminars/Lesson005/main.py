list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
print(list_1)


number = int(input('Введите искомое число: '))

def BinarySearch(array, number):
    mid = len(array) // 2

    if array[mid] == number:
        return 1
    elif number < array[mid]:
        return BinarySearch(array[:mid], number)
    elif number > array[mid]:
        return BinarySearch(array[mid:], number)
    else:
        return -1






print(BinarySearch(list_1, number))






