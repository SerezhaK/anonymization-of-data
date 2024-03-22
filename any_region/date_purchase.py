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

    mounth = date_of_purchase[date_of_purchase.index('.') + 1:date_of_purchase.rfind('.')]
    if mounth in winter:
        return 'Зима'
    elif mounth in spring:
        return 'Весна'
    elif mounth in summer:
        return 'Лето'
    elif mounth in autumn:
        return 'Осень'
