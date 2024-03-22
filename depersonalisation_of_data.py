from any_region.bank_card_obez import obez_bankcard
from any_region.birthday_obez import obez_birthday
from any_region.date_purchase import obez_date
from any_region.email_generation_obez import obez_email
from any_region.inn_passport_obez import obez_passport_inn
from any_region.sum_of_goods_obez import obez_sum_goods
# imports for SPB

from spb.adress import obez_adress
from spb.name_sex_obez import obez_FIO
from spb.phones_obez import obez_phones
from spb.profession_income_spb_obez import obez_pro_inc
from spb.adress import obez_price
from spb.adress import obez_name



def obez_massive(start_data):
    # [name (0), surname (1), sex (2), date_of_birth (3), age (4), bankcard (5), address (6), inn (7), passport (8),
    # profession (9), income (10), phone_number (11), email (12), date_of_purchase (13), shops_gps (14), shops_name (15), categories (16), sum_of_goods (17), price(18)]




    #[sex, age, card, adres, profession, income, categoria, name, adress_shop, price,date, phone_number, email,sum_goods]
    a = start_data
    answer = []
    for i in range(len(a)):  # итый, кокретный
        #a[i][3] = obez_birthday([a[i][3:5]])[0]  # проблема (функицю не менял)
        # a[i][4]
        #a[i][5] = obez_bankcard(a[i][5])[0]  # поменял функцию
        #a[i][6] = obez_adress(a[i][6])[0]  # поменял функцию
        #a[i][9] = obez_pro_inc(list(a[0][9:11]))[0]  # переделал для профессии
        #a[i][10] = obez_pro_inc(list(a[0][9:11]))[1]
        #a[i][11] = obez_phones(a[i][11])[0]  # поменял
        #a[i][12] = obez_email(a[i][12])[0]  # поменял
        #a[i][13] = obez_date(a[0][13])[0]  # поменял
        # a[i][14]
        # a[i][15]
        # a[i][16]
        #a[i][14] = obez_sum_goods(a[i][14])[0] #индекс 17 должен быть, но по факту 14 #поменял
        answer.append(a[i][2])
        answer.append(obez_birthday([a[i][3:5]])[0]) #надо залить
        answer.append(obez_bankcard(a[i][5])[0]) #надо залить
        answer.append(obez_adress(a[i][6])[0]) #надо залить
        answer.append(obez_pro_inc(list(a[0][9:11]))[0]) #надо залить
        answer.append(obez_pro_inc(list(a[0][9:11]))[1])
        answer.append(a[i][16])
        answer.append(obez_name(a[i][15]))
        answer.append(obez_adress(a[i][14])[0]) #shop_gps
        answer.append(obez_price(a[i][18]))
        answer.append(obez_date(a[0][13])[0]) #залить
        answer.append(obez_phones(a[i][11])[0]) # залить
        answer.append(obez_email(a[i][12])[0]) # залить
        answer.append(obez_sum_goods(a[i][17])[0]) # залить



    return answer



