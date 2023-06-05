def max1(a, b):
    if a > b:
        return a
    return b

def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n-1) + fib(n - 2)


def QuikSort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greatest = [i for i in array[1:] if i > pivot]

        return QuikSort(less) + [pivot] + QuikSort(greatest)
    list ()def MergeSort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        MergeSort(left)
        MergeSort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1






