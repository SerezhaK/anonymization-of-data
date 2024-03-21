import random
import string

veroiatnos = [0.25, 0.6, 1]
pochta = ["@gmail.com", "@mail.ru", "@yandex.ru"]


def email_adress_generation(cnt):
    massiv_emails = []
    for i in range(cnt):
        email_adress = ''
        lenght = random.randint(10, 15)
        ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=lenght))
        email_adress = str(ran)
        email = random.random()
        for j in range(3):
            if veroiatnos[j] > email:
                email_adress += pochta[j]
                break
        massiv_emails.append(email_adress)
    return (massiv_emails)


# Обезличивание
email = email_adress_generation(10)
email_obez = []
for x in range(len(email)):
    if "@gmail.com" in email[x]:
        email_obez.append('gmail.com')
    elif "@mail.ru" in email[x]:
        email_obez.append('mail.ru')
    elif "@yandex.ru" in email[x]:
        email_obez.append('@yandex.ru')
print(email, email_obez)
