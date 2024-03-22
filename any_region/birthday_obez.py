age_probability_distributions_st_petersburg = [(11.5, [70, 108]), (20.9, [35, 39]), (29.2, [39, 44]), (36.9, [29, 34]),
                                               (44.2, [44, 49]), (51.1, [59, 64]),
                                               (57.9, [49, 54]), (64.2, [54, 59]), (70.2, [64, 69]), (76.1, [7, 13]),
                                               (82, [19, 24]), (87.5, [0, 5]),
                                               (92.5, [24, 29]), (94.6, [17, 19]), (96.2, [13, 15]), (97.8, [15, 17]),
                                               (98.9, [6, 6]), (100, [7, 13])]
import datetime
import random


def generate_day(month: int, year: int):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return random.randint(1, 31)
    if month == 2:
        return random.randint(1, 28 + int(year % 4 == 0))
    return random.randint(1, 30)


def generation_date_of_birth(count: int):
    probabilities = age_probability_distributions_st_petersburg
    answer = []

    for _ in range(count):
        value_for_check = random.random() * 100

        # получаем год согласно распредлению вероятности
        for i in probabilities:
            if value_for_check < i[0]:
                age_range = i[1]
                break

        age = random.randint(age_range[0], age_range[1])
        today_year = int(datetime.datetime.now().year)

        year = today_year - age
        month = random.randint(1, 12)
        day = generate_day(month, year)

        answer.append([
            f"{day}.{month}.{year}",
            today_year - year
        ])

    return answer


# Обезличивание
def obez_birthday(birthday):
    birthday_obez = []
    for x in range(len(birthday)):
        if 0<= birthday[x][1] <= 5:
            birthday_obez.append('0-5')
        elif 6 <= birthday[x][1] <= 12:
            birthday_obez.append('6-12')
        elif 13 <= birthday[x][1] <= 17:
            birthday_obez.append('13-17')
        elif 18 <= birthday[x][1] <= 25:
            birthday_obez.append('18-25')
        elif 26 <= birthday[x][1] <= 34:
            birthday_obez.append('26-34')
        elif 35 <= birthday[x][1] <= 45:
            birthday_obez.append('35-45')
        elif 46 <= birthday[x][1] <= 54:
            birthday_obez.append('46-54')
        elif 55 <= birthday[x][1] <= 65:
            birthday_obez.append('55-65')
        elif 66 <= birthday[x][1] <= 74:
            birthday_obez.append('66-74')
        elif 75 <= birthday[x][1] <= 84:
            birthday_obez.append('75-84')
        elif 85 <= birthday[x][1] <= 95:
            birthday_obez.append('85-95')
        elif birthday[x][1] > 95:
            birthday_obez.append('>95')
    return birthday_obez
