'''1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный
массив, заданный случайными числами на промежутке [-100; 100). Выведите на
экран исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).'''

import random

def sort_bubble(list):
    n = 1

    while n < len(list):
        count = 0

        for i in range(len(list) - 1 - (n - 1)):

            if list[i] < list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                count += 1

        if count == 0:
            break

        n += 1


SIZE = 10
MIN = -100
MAX = 99
array = [random.randint(MIN, MAX) for i in range(SIZE)]

print(array, ' -- ', 'Array')
sort_bubble(array)
print(array, ' -- ',  'After sort')