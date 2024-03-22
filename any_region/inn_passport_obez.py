import random

veroiatnost = [98.4, 99.09, 99.31, 99.47, 99.62, 99.75, 99.84, 99.9, 99.94, 99.97, 100]
s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def generation_passports(count):
    answer_pasport, answer_inn = [], []
    for n in range(count):
        t = ""
        x = random.uniform(0, 100)
        for j in range(11):
            if veroiatnost[j] > x:
                w = j
                break
        if w == 5 or w == 7 or w == 9 or w == 10:  # паспорта Армении,Кыргызстана,Молдовы и Беларуси
            t = s[random.randint(0, 25)] + s[random.randint(0, 25)]
            for i in range(7):
                t += str(random.randint(0, 9))
        elif w == 6 or w == 8:  # паспорта Азербайджана и Туркменистана
            t = s[random.randint(0, 25)]
            for i in range(7):
                t += str(random.randint(0, 9))
        elif w == 0:  # паспорта России
            for i in range(4):
                t += str(random.randint(0, 9))
            t += ' '
            for i in range(6):
                t += str(random.randint(0, 9))
        elif w == 1:  # паспорта Таджикистана
            t = s[random.randint(0, 25)]
            for i in range(6):
                t += str(random.randint(0, 9))
        elif w == 2:  # паспорта Узбекистана
            for i in range(15):
                t += str(random.randint(0, 9))
        elif w == 3:  # паспорта Казахстана
            t = 'N'
            for i in range(8):
                t += str(random.randint(0, 9))
        elif w == 4:  # паспорта Украины
            for i in range(9):
                t += str(random.randint(0, 9))
        inn = ''
        for i in range(12):
            inn += str(random.randint(0, 9))
        answer_pasport.append(t)
        answer_inn.append(inn)
    return answer_pasport, answer_inn

# Обезличивание
def obez_passport_inn(generation):
    answer = []
    a = [0,0]
    for x in range(len(generation[0])):
        answer.append(a)
    return answer

