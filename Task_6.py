'''6. Пользователь вводит номер буквы в алфавите. Определить,
какая это буква.'''
number = int(input('Введите номер буквы в алфавите: '))

list = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

if number <= len(list):
    print(f'Номер буквы {number}: {list[number - 1]}')
else:
    print(
      f'Слишком большое число ({len(list)})'
    )
print(f'Весь алфавит: {list}')