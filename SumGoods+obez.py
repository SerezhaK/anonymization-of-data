import random


def sum_goods_generation(cnt):
    massiv_sum_goods = []
    for x in range(cnt):
        a = random.randint(1, 30)
        massiv_sum_goods.append(a)
    return massiv_sum_goods


# Обезличивание
def obez_sum_goods(sum_goods):
    obez_sum_goods = []
    for x in range(len(sum_goods)):
        if 1 <= sum_goods[x] <= 5:
            obez_sum_goods.append('От 1 до 5 товаров')
        elif 6 <= sum_goods[x] <= 10:
            obez_sum_goods.append('От 6 до 10 товаров')
        elif 11 <= sum_goods[x] <= 15:
            obez_sum_goods.append('От 11 до 15 товаров')
        elif 16 <= sum_goods[x] <= 20:
            obez_sum_goods.append('От 16 до 20 товаров')
        elif sum_goods[x] > 20:
            obez_sum_goods.append('Более 20 товаров')
    return obez_sum_goods
  


