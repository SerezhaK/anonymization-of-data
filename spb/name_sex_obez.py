import random

Male_names = ['Александр', 'Иван', 'Сергей', 'Андрей', 'Алексей', 'Дмитрий', 'Максим', 'Михаил', 'Владимир', 'Игорь']
Probably_of_Mn = [0.166694684, 0.320639313, 0.450079526, 0.573998164, 0.686666753, 0.791563757, 0.859814051,
                  0.909753921, 0.958245509, 0.999999999]
Male_surnames = ['Иванов', 'Петров', 'Смирнов', 'Васильев', 'Андреев', 'Алексеев', 'Кузнецов', 'Соколов']
Probably_of_Ms = [0.4041095, 0.561519661, 0.695821964, 0.779460256, 0.837650162, 0.892827124, 0.946646321, 0.999999999]
Female_names = ['Екатерина', 'Мария', 'Елена', 'Анна', 'Ольга', 'Анастасия', 'Наталья', 'Ирина', 'Татьяна', 'Светлана']
Probably_of_Fmn = [0.122365996, 0.244641631, 0.35735714, 0.465952217, 0.568348574, 0.667437742, 0.762406477,
                   0.844815123, 0.925886435, 1]
Female_surnames = ['Иванова', 'Смирнова', 'Петрова', 'Васильева', 'Кузнецова', 'Романова', 'Соколова', 'Андреева']
Probably_of_Fms = [0.362110095, 0.517638342, 0.65773304, 0.749737956, 0.8144179, 0.87776051, 0.940832039, 1]
Sex = ["Female", "Male"]
Probably_of_sex = [0.551166966, 1]


def generation_sex_and_fio(cnt):
    massiv_sex_and_fio = []
    for i in range(cnt):
        sex_and_fio = []
        q = random.random()
        if (q < Probably_of_sex[0]):
            sex_and_fio.append(Sex[0])
            second_name = random.random()
            for j in range(8):
                if (second_name < Probably_of_Fms[j]):
                    sex_and_fio.append(Female_surnames[j])
                    break
            name = random.random()
            for j in range(10):
                if (name < Probably_of_Fmn[j]):
                    sex_and_fio.append(Female_names[j])
                    break
        else:
            sex_and_fio.append(Sex[1])
            second_name = random.random()
            for j in range(8):
                if (second_name < Probably_of_Ms[j]):
                    sex_and_fio.append(Male_surnames[j])
                    break
            name = random.random()
            for j in range(10):
                if (name < Probably_of_Mn[j]):
                    sex_and_fio.append(Male_names[j])
                    break
        massiv_sex_and_fio.append(sex_and_fio)
    return massiv_sex_and_fio


#Обезличивание
def obez_FIO(generate):
    FIO_sex_obez = []
    for x in range(len(generate)):
        a = []
        a.append(generate[x][0])
        a.append('0_o')
        FIO_sex_obez.append(a)
    return(FIO_sex_obez)
