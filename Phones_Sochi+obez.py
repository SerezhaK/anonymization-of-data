import random
probably_of_codes = [56.25, 16.5, 15.25, 9.25] # МТС > Билайн > Мегафон > Теле2
mtc = ['918', '978', '986', '988', '989']
megaphone = ['928', '929', '938', '939', '999']
tele2 = ['900', '901', '902', '908', '952', '953', '995']
beeline = ['903', '905', '906', '909', '933', '960', '961', '962', '963', '964', '965', '966', '967', '968', '969']


def phones_generation(cnt):
    massiv_phones=[]
    for j in range(cnt):
        phone = '8'
        operator=random.random()
        for i in range(4):
            if(operator<probably_of_codes[i]):
                if(i==0):
                    s=random.randint(0,29)
                    phone+=mtc[s]
                elif(i==1):
                    s=random.randint(0,14)
                    phone+=megaphone[s]
                elif(i==2):
                    s=random.randint(0,25)
                    phone+=tele2[s]
                else:
                    s=random.randint(0,13)
                    phone+=beeline[s]
                break
        for i in range(7):
            phone+=str(random.randint(0,9))
        massiv_phones.append(phone)
    return massiv_phones

# Обезличивание
phones = phones_generation(100)
phones_obez = []
for x in range(len(phones)):
    if phones[x][0:2] in mtc:
        phones_obez.append('МТС')
    elif phones[x][0:2] in megaphone:
        phones_obez.append('МЕГАФОН')
    elif phones[x][0:2] in tele2:
        phones_obez.append('ТЕЛЕ2')
    elif phones[x][0:2] in beeline:
        phones_obez.append('Билайн')
print(phones_generation(100))

