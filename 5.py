rev = int(input('Введите выручку фирмы, руб. - '))
cost = int(input('Введите издержки фирмы, руб. - '))

if rev > cost:
    print(f'Ваша фирма работает с прибылью. Рентабельность выручки составляет {int((rev - cost) / cost * 100)}%')
    size = int(input('Введите численность фирмы - '))
    print(f'Прибыль фирмы на одного сотрудника составляет {int((rev - cost) / size)} руб.')

elif rev == cost:
    print(f'Ваша фирма работает в ноль.')

else:
    print(f'Ваша фирма работает с убытком.')