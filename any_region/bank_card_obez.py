import random

veroiatnost = [0.8, 0.9, 0.94, 0.97, 0.98, 0.9888, 0.9938, 0.9988, 0.9998, 1]
veroiatnost2 = [0.27, 0.62, 1]
paySystem = ["2", "4", "5"]
bin_banks = ["27649", "20015", "37772", "02177", "53373", "21785", "14088", "49516", "16943", "03289"]


# 02177 райфайзинг
# 20015 альфабанк
# 37772 тинька
# 27649 сбер
# 53373 мтс
# 21785 cвой банк
# 14088 кредит европа банк
# 49516 отп
# 16943 фора
# 03289 сбай
def generation_bankcard(cnt):
    massiv_cards = []
    for j in range(cnt):
        bin_card = random.random()
        pay_system = random.random()
        card = ''
        for i in range(3):
            if pay_system <= veroiatnost2[i]:
                card += paySystem[i]
                break
        for i in range(10):
            if bin_card <= veroiatnost[i]:
                card += bin_banks[i]
                break
        for i in range(10):
            card += str(random.randint(0, 9))
        massiv_cards.append(card)
    return massiv_cards


# Обезличивание
def obez_bankcard(karti_dengi_dva_stvola):
    obez_karti_dengi_dva_stvola = []
    if karti_dengi_dva_stvola[1:6] == '02177':
        if karti_dengi_dva_stvola[0] == '2':
                obez_karti_dengi_dva_stvola.append('Райфайзинг/Mastercard')
        if karti_dengi_dva_stvola[0] == '4':
                obez_karti_dengi_dva_stvola.append('Райфайзинг/VISA')
        if karti_dengi_dva_stvola[0] == '5':
                obez_karti_dengi_dva_stvola.append('Райфайзинг/МИР')

    if karti_dengi_dva_stvola[1:6] == '20015':
        if karti_dengi_dva_stvola[0] == '2':
                obez_karti_dengi_dva_stvola.append('Альфабанк/Mastercard')
        if karti_dengi_dva_stvola[0] == '4':
                obez_karti_dengi_dva_stvola.append('Альфабанк/VISA')
        if karti_dengi_dva_stvola[0] == '5':
                obez_karti_dengi_dva_stvola.append('Альфабанк/МИР')

    if karti_dengi_dva_stvola[1:6] == '37772':
        if karti_dengi_dva_stvola[0] == '2':
                obez_karti_dengi_dva_stvola.append('Тинькофф/Mastercard')
        if karti_dengi_dva_stvola[0] == '4':
                obez_karti_dengi_dva_stvola.append('Тинькофф/VISA')
        if karti_dengi_dva_stvola[0] == '5':
                obez_karti_dengi_dva_stvola.append('Тинькофф/МИР')

    if karti_dengi_dva_stvola[1:6] == '27649':
         if karti_dengi_dva_stvola[0] == '2':
                obez_karti_dengi_dva_stvola.append('Сбербанк/Mastercard')
         if karti_dengi_dva_stvola[0] == '4':
                obez_karti_dengi_dva_stvola.append('Сбербанк/VISA')
         if karti_dengi_dva_stvola[0] == '5':
                obez_karti_dengi_dva_stvola.append('Сбербанк/МИР')

    if karti_dengi_dva_stvola[1:6] == '53373':
        if karti_dengi_dva_stvola[0] == '2':
                obez_karti_dengi_dva_stvola.append('МТС Банк/Mastercard')
        if karti_dengi_dva_stvola[0] == '4':
                obez_karti_dengi_dva_stvola.append('МТС Банк/VISA')
        if karti_dengi_dva_stvola[0] == '5':
                obez_karti_dengi_dva_stvola.append('МТС Банк/МИР')

    if karti_dengi_dva_stvola[1:6] == '21785':
        if karti_dengi_dva_stvola[0] == '2':
                obez_karti_dengi_dva_stvola.append('Свой Банк/Mastercard')
        if karti_dengi_dva_stvola[0] == '4':
                obez_karti_dengi_dva_stvola.append('Свой Банк/VISA')
        if karti_dengi_dva_stvola[0] == '5':
                obez_karti_dengi_dva_stvola.append('Свой Банк/МИР')

    if karti_dengi_dva_stvola[1:6] == '14088':
        if karti_dengi_dva_stvola[0] == '2':
                obez_karti_dengi_dva_stvola.append('Кредит Европа Банк/Mastercard')
        if karti_dengi_dva_stvola[0] == '4':
                obez_karti_dengi_dva_stvola.append('Кредит Европа Банк/VISA')
        if karti_dengi_dva_stvola[0] == '5':
                obez_karti_dengi_dva_stvola.append('Кредит Европа Банк/МИР')

    if karti_dengi_dva_stvola[1:6] == '49516':
        if karti_dengi_dva_stvola[0] == '2':
                obez_karti_dengi_dva_stvola.append('ОТП Банк/Mastercard')
        if karti_dengi_dva_stvola[0] == '4':
                obez_karti_dengi_dva_stvola.append('ОТП Банк/VISA')
        if karti_dengi_dva_stvola[0] == '5':
                obez_karti_dengi_dva_stvola.append('ОТП Банк/МИР')

    if karti_dengi_dva_stvola[1:6] == '16943':
        if karti_dengi_dva_stvola[0] == '2':
                obez_karti_dengi_dva_stvola.append('ФОРА/Mastercard')
        if karti_dengi_dva_stvola[0] == '4':
                obez_karti_dengi_dva_stvola.append('ФОРА/VISA')
        if karti_dengi_dva_stvola[0] == '5':
                obez_karti_dengi_dva_stvola.append('ФОРА/МИР')

    if karti_dengi_dva_stvola[1:6] == '03289':
        if karti_dengi_dva_stvola[0] == '2':
                obez_karti_dengi_dva_stvola.append('SBI/Mastercard')
        if karti_dengi_dva_stvola[0] == '4':
                obez_karti_dengi_dva_stvola.append('SBI/VISA')
        if karti_dengi_dva_stvola[0] == '5':
                obez_karti_dengi_dva_stvola.append('SBI/МИР')
    return obez_karti_dengi_dva_stvola
