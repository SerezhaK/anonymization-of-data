# imports for all regions

from any_region.bank_card_obez import generation_bankcard
from any_region.birthday_obez import generation_date_of_birth
from any_region.date_purchase import date_generation
from any_region.email_generation_obez import email_adress_generation
from any_region.inn_passport_obez import generation_passports
from any_region.sum_of_goods_obez import sum_goods_generation
# imports for SPB

from spb.adress import generation_adress
from spb.name_sex_obez import generation_sex_and_fio
from spb.phones_obez import phones_generation
from spb.profession_income_spb_obez import generation_profession


def massive_generation(count: int):
    """
    profession : [ [ profession, income], [profession, ...], ...]
    address : [ address, address , ...]
    phones : [phone_number, phone_number, ... ]
    sex_and_name : [ [sex, surname, name], [sex ... ] ...]

    bankcard : [ bankcard, bankcard, ...]
    date_of_birth :  [ [date_of_birth, age], [date_of_birth, age], ...]
    date_of_purchase : [date_of_purchase, date_of_purchase, ...]
    email : [email, email, email, ...]
    inn_passport : ([passport, passport, ...] , [inn, inn, inn ...])
    sum_goods : [sum_goods, sum_goods, ...]
    """
    profession = generation_profession(count)
    address = generation_adress(count)
    phones = phones_generation(count)
    sex_and_name = generation_sex_and_fio(count)
    bankcard = generation_bankcard(count)
    date_of_birth = generation_date_of_birth(count)
    date_of_purchase = date_generation(count)
    email = email_adress_generation(count)
    inn_passport = generation_passports(count)
    sum_goods = sum_goods_generation(count)

    answer = []

    # the order must be like this :
    # [name, surname, sex, date_of_birth, age, bankcard, address, inn, passport,
    # profession, income, phone_number, email, date_of_purchase, shops_gps, shops_name, categories, sum_of_goods, price]

    for i in range(count):
        answer.append(
            (
                sex_and_name[i][2],
                sex_and_name[i][1],
                sex_and_name[i][0],
                date_of_birth[i][0],
                date_of_birth[i][1],
                bankcard[i],
                address[i][0],
                inn_passport[1][i],
                inn_passport[0][i],
                profession[i][0],
                profession[i][1],
                phones[i],
                email[i],
                date_of_purchase[i],
                address[i][3],
                address[i][2],
                address[i][1],
                sum_goods[i],
                address[i][4]
            )
        )

    return answer
       
