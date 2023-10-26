# Контекст
# Корреляция - статистическая мера, используемая для оценки связи между двумя случайными величинами.
# ● Ваша задача
# Написать скрипт для расчета корреляции Пирсона между двумя случайными величинами (двумя массивами).
# Можете использовать любую парадигму, но рекомендую использовать функциональную,
# т.к. в этом примере она значительно упростит вам жизнь.
from statistics import mean


def calc(lst1, lst2):
    mean_lst1 = mean(lst1)
    mean_lst2 = mean(lst2)
    return sum(map(lambda x, y: (x - mean_lst1) * (y - mean_lst2), lst1, lst2)) / (
                sum(map(lambda x: (x - mean_lst1) ** 2, lst1)) * sum(map(lambda y: (y - mean_lst2) ** 2, lst2))) ** 0.5


init_lst1 = [1, 2, 3, 4, 3]
init_lst2 = [1, 2, 3, 4, 4]
print(calc(init_lst1, init_lst2))