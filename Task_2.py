'''2. Отсортируйте по возрастанию методом слияния одномерный вещественный
массив, заданный случайными числами на промежутке [0; 50). Выведите на экран
исходный и отсортированный массивы.'''

from random import randint

SIZE = 50

import operator

def sort_merge(L, compare=operator.lt):
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L) / 2)
        left = sort_merge(L[:middle], compare)
        right = sort_merge(L[middle:], compare)
        return merge_list(left, right, compare)

def merge_list(list_1, list_2, compare):
    result = []
    i, j = 0, 0

    while i < len(list_1) and j < len(list_2):
        if compare(list_1[i], list_2[j]):
            result.append(list_1[i])
            i += 1
        else:
            result.append(list_2[j])
            j += 1

    result += list_1[i:]
    result += list_2[j:]
    return result


numbers = [randint(0, 50) for _ in range(SIZE)]

print('Array' , ' -- ', numbers)
print('After sort', ' -- ', sort_merge(numbers))