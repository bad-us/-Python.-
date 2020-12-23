# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
from collections import defaultdict
from collections import deque


def dex(string):
    dex_num = 0
    num = deque(string)
    num.reverse()
    for i in range(len(num)):
        dex_num += tab[num[i]] * 16 ** i
    return dex_num


def hex(num_b):
    num = deque()
    while num_b > 0:
        d = num_b % 16
        for i in tab:
            if tab[i] == d:
                num.append(i)
        num_b //= 16
    num.reverse()
    return list(num)


sim = '0123456789ABCDEF' # Символы
tab = defaultdict(int)
a = 0 # Счетчик
for key in sim:
    tab[key] += a
    a += 1

first = dex(input('Введите первое число: ').upper())
second = dex(input('Введите второе число: ').upper())

print(f'Сумма чисел: {"".join(hex(first + second))}')
print(f'Произведение чисел: {"".join(hex(first * second))a}')