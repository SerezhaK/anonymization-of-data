import random

mas = [[108, 39, 44, 34, 49, 64, 54, 59, 69, 13, 24, 5, 29, 19, 15, 7, 6, 7],
       [11.5, 20.9, 29.2, 36.9, 44.2, 51.1, 57.9, 64.2, 70.2, 76.1, 82, 87.5, 92.5, 94.6, 96.2, 97.8, 98.9, 100]]
q = [-1, 5, 6, 7, 13, 15, 17, 19, 24, 29, 34, 39, 44, 49, 54, 59, 64, 69, 108]
a = [[], []]


def generation_date_of_birth(cnt):
    for n in range(cnt):
        x = random.uniform(0, 100)
        for i in range(18):
            if (mas[1][i] > x):
                e = mas[0][i]
                break
        for i in range(18):
            if (q[i + 1] == e):
                b = q[i] + 1
                break
        e = 2023 - e
        b = 2023 - b
        y = random.randint(e, b)
        m = random.randint(1, 12)
        if m == 2 and y % 4 == 0:
            d = random.randint(1, 29)
        elif m == 2 and y % 4 != 0:
            d = random.randint(1, 28)
        elif m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
            d = random.randint(1, 31)
        else:
            d = random.randint(1, 30)
        t = str(d) + '.' + str(m) + '.' + str(y)
        a[0].append(t)
        a[1].append(2023 - y)

generation_date_of_birth(1000)
for i in range(1000):
    print(a[0][i], a[1][i])
