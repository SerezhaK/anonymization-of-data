import random


def sum_goods_generation(cnt):
    massiv_sum_goods = []
    for x in range(cnt):
        a = random.randint(1, 30)
        massiv_sum_goods.append(a)
    return massiv_sum_goods


# Обезличивание
def obez_sum_goods(sum_goods):
    if 1 <= sum_goods <= 5:
        return 'От 1 до 5 товаров'
    elif 6 <= sum_goods <= 10:
        return 'От 6 до 10 товаров'
    elif 11 <= sum_goods <= 15:
        return 'От 11 до 15 товаров'
    elif 16 <= sum_goods <= 20:
        return 'От 16 до 20 товаров'
    elif sum_goods > 20:
        return 'Более 20 товаров'


