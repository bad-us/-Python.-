"""
Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
Пример работы функции:

func("papa")
6
func("sova")
9
"""

import hashlib


def func(str):
    result = set()
    N = len(str)
    for i in range(N):
        if i == 0:
            N = len(str) - 1
        else:
            N = len(str)
        for j in range(N, i, -1):
            result.add(hashlib.sha1(str[i:j].encode('utf-8')).hexdigest())
            print(str[i:j])

    print(f'Number of different substrings in a string {str} = {len(result)}')


func(input('Input string from latin letters ').lower())
