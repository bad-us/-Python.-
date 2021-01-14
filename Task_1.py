# Python 3.8.7
# OS - Windows 10 64bit

# По введенным пользователем координатам двух точек вывести уравнение прямой,
# которая проходит через эти точки

import sys
import random

print('Введите координаты точки A(x1; y1):')
x1 = float(input('x1 = '))
y1 = float(input('y1 = '))

print('Введите координаты точки B(x2; y2), где B != A:')
x2 = float(input('x2 = '))
y2 = float(input('y2 = '))

print('Уравнение прямой, проходящей через эти точки:')
if x1 == x2:
    print(f'x = {x1:.3f}')
else:
    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2
    print(f'y = {k:.3f} * x + {b:.3f}')

sum = 0
var = (x1, y1, x2, y2, k ,b)
for i in var:
    sum += sys.getsizeof(i)
print(f'Под переменные используется {sum} байт памяти')

# Под переменные используется 144 байт памяти

print('-'* 30)

# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

num = int(input('Введите целое число: '))
even, odd = 0, 0
while num > 0:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
    num = num // 10
print(f"четных - {even}, нечетных - {odd}")

sum = 0
var = (num, even, odd)
for i in var:
    sum += sys.getsizeof(i)
print(f'Под переменные используется {sum} байт памяти')

# Под переменные используется 80 байт памяти.

print('-'*30)

# А теперь расчитаем расход памяти на матрицы

# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# то во второй массив надо заполнить значениями 0, 3, 4, 5 (индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
spam = 0
print(array)

result = []
for i in range(len(array)):
    if array[i] % 2 == 0:
        result.append(i)
print(f'Индексы четных элементов: {result}')

#result_new = [i for i in range(len(array)) if array[i] % 2 == 0]
#print(f'Индексы четных элементов: {result_new}')

sum = 0
var = (SIZE, MIN_ITEM, MAX_ITEM, array, result, spam)
for i in var:
    sum += sys.getsizeof(i)
print(f'Под переменные используется {sum} байт памяти')

# Под переменные используется 412 байт памяти