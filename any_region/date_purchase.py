import random


def date_generation(cnt):
    massiv_dates = []
    for i in range(cnt):
        date = ''
        month = random.randint(1, 12)
        if month == 2:
            day = random.randint(1, 29)
        elif month in [1, 3, 5, 7, 8, 10, 12]:
            day = random.randint(1, 31)
        else:
            day = random.randint(1, 30)
        if month == 1 or month == 2:
            date = str(day) + '.' + str(month) + '.' + '2024'
        else:
            date = str(day) + '.' + str(month) + '.' + '2023'
        massiv_dates.append(date)
    return massiv_dates


# Обезличивание
def obez_date(date_of_purchase):
    winter = ['12', '1', '2']
    spring = ['3', '4', '5']
    summer = ['6', '7', '8']
    autumn = ['9', '10', '11']
    obez_date_of_purchase = []
    for x in range(len(date_of_purchase)):
        mounth = date_of_purchase[x][date_of_purchase[x].index('.') + 1:date_of_purchase[x].rfind('.')]
        if mounth in winter:
            obez_date_of_purchase.append('Зима')
        elif mounth in spring:
            obez_date_of_purchase.append('Весна')
        elif mounth in summer:
            obez_date_of_purchase.append('Лето')
        elif mounth in autumn:
            obez_date_of_purchase.append('Осень')
    return obez_date_of_purchase
a = date_generation(10)
