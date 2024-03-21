import random

probably_of_codes = [0.2925, 0, 565, 0, 7875, 1]  # МТС > мегафон > Теле2 > Билайн
mtc = ['981', '911', '989', '986', '958', '932', '933', '981', '939', '984', '980', '994', '992', '988', '930', '967',
       '924', '968', '936', '938', '985', '999', '983', '969', '902', '989', '993', '931', '923', '904']
megaphone = ['921', '931', '999', '929', '930', '933', '937', '932', '939', '923', '924', '958', '999', '996', '995']
tele2 = ['952', '953', '904', '950', '901', '951', '996', '994', '992', '900', '991', '902', '993', '995', '991', '993',
         '958', '939', '930', '995', '980', '932', '939', '977', '996', '958']
beeline = ['965', '966', '969', '905', '964', '967', '960', '962', '963', '906', '961', '909', '968', '903']


def phones_generation(cnt):
    massiv_phones = []
    for j in range(cnt):
        phone = '8'
        operator = random.random()
        for i in range(4):
            if (operator < probably_of_codes[i]):
                if (i == 0):
                    s = random.randint(0, 29)
                    phone += mtc[s]
                elif (i == 1):
                    s = random.randint(0, 14)
                    phone += megaphone[s]
                elif (i == 2):
                    s = random.randint(0, 25)
                    phone += tele2[s]
                else:
                    s = random.randint(0, 13)
                    phone += beeline[s]
                break
        for i in range(7):
            phone += str(random.randint(0, 9))
        massiv_phones.append(phone)
    return massiv_phones


# Обезличивание
def obez_phones(phones):
    phones_obez = []
    for x in range(len(phones)):
        if phones[x][1:4] in mtc:
            phones_obez.append('МТС')
        elif phones[x][1:4] in megaphone:
            phones_obez.append('МЕГАФОН')
        elif phones[x][1:4] in tele2:
            phones_obez.append('ТЕЛЕ2')
        elif phones[x][1:4] in beeline:
            phones_obez.append('Билайн')
    return phones_obez
