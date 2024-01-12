import datetime
import random

from data.birthday import age_probability_distributions_st_petersburg


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


print(generation_date_of_birth(1000))
