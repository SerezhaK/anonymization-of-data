# imports for all regions
from any_region.bank_card_obez import obez_bankcard
from any_region.birthday_obez import obez_birthday
from any_region.date_purchase import obez_date
from any_region.email_generation_obez import obez_email
from any_region.sum_of_goods_obez import obez_sum_goods

# imports for SPB

from spb.adress import obez_adress
from spb.adress import obez_name
from spb.adress import obez_price
from spb.phones_obez import obez_phones
from spb.profession_income_spb_obez import obez_pro_inc


def depersonalization(data):
    """
    from this:
    [
        name (0),
        surname (1),
        sex (2),
        date_of_birth (3),
        age (4),
        bankcard (5),
        address (6),
        inn (7),
        passport (8),
        profession (9),
        income (10),
        phone_number (11),
        email (12),
        date_of_purchase (13),
        shops_gps (14),
        shops_name (15),
        category (16),
        sum_of_goods (17),
        price(18)
    ]

    to this: [name, surname, sex, age, card, address, profession, income, category, shop_name, address_shop, price,
    date, phone_number, email, sum_goods]

    """

    answer = []

    for i in range(len(data)):
        answer.append(
            (
                # name and surname
                "Cелезнев",
                "Александр",

                # sex
                data[i][2],

                # date_of_birth
                obez_birthday(data[i][4]),

                # card
                obez_bankcard(data[i][5])[0],

                # address
                obez_adress(data[i][6]),

                # profession and income
                * obez_pro_inc([data[i][9], data[i][10]]),

                # category
                data[i][16],

                # shop_name
                obez_name(data[i][15]),

                # address shop
                obez_adress(data[i][14]),

                # price
                obez_price(data[i][18]),

                # date
                obez_date(data[0][13]),

                # phone number
                obez_phones(data[i][11]),

                # email
                obez_email(data[i][12]),

                # sum goods
                obez_sum_goods(data[i][17])
            ))

    return answer
