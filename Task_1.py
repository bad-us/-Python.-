# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
import collections

def prof(n):
    all_p = 0
    for i in range(n):
        name = input(f'Введите название {i + 1}-й компании: ')
        profit = 0
        a = 1
        while a <= q:
            try:
                profit += float(input(f'Введите прибыль за {a}-й квартал: '))
            except ValueError:
                print('Вы ввели недопустимое значение')
                continue
            a += 1
        comp[name] = profit
        all_p += profit
    return all_p

comp = collections.defaultdict()  # Список компаний
p_comp = collections.deque()  # Список профессионалов
u_comp = collections.deque()  # Список даунсайдеров
q = 4  # Квартал

while True:
    try:
        n = int(input('Введите количество компаний: '))
    except ValueError:
        print('Вы ввели неправильное количество компаний')
        continue
    break

m = prof(n)
mid_p = m / n
for i, item in comp.items():
    if item >= mid_p:
        p_comp.append(i)
    else:
        u_comp.append(i)

print(f'Средняя прибыль для всех компаний составила: {round(mid_p,2)}')
print(f'Прибыль выше среднего у {len(p_comp)} компаний:')
for name in p_comp:
    print(name)
print(f'Прибыль ниже среднего у {len(u_comp)} компаний:')
for name in u_comp:
    print(name)