def f23(x):
    preTable = [[f"{round((int(i[0].split()[0][:2])) / 100, 1)}",
                 i[1].split()[1:],
                 f"{'%s%s' % (i[4][0:6], i[4][8:10])}",
                 f"{i[5][0:i[5].index('@')]}"] for i in x]
    table = []
    for i in preTable:
        if i not in table:
            table.append(i)
    table = list(map(list, zip(*table)))
    return table

# print(f23([
#    ['97%', 'Егор Бичберг', None, None, '26.02.2001', 'bicberg89@yandex.ru'],
#    ['26%', 'Амир Говоший', None, None, '22.03.2004', 'govosij87@yandex.ru'],
#    ['26%', 'Амир Говоший', None, None, '22.03.2004', 'govosij87@yandex.ru'],
#   ['89%', 'Артур Ребичак', None, None, '18.04.2002', 'rebicak3@rambler.ru'],
#    ['92%', 'Мирон Зигий', None, None, '25.06.1999', 'miron28@mail.ru']
# ]))
