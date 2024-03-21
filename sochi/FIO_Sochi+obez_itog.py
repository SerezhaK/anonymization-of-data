import random
Male_names = ['Александр','Сергей','Андрей','Алексей','Владимир','Дмитрий','Максим','Иван','Евгений','Олен',]
Probably_of_Mn = [0.208775561, 0.369621702, 0.485988168, 0.584665522, 0.674520339, 0.760176745, 0.829949649, 0.892896464, 0.953200922, 1]
Male_surnames = ['Иванов','Петров','Григорян','Арутюнян','Акопян','Шевченко','Бондаренко','Коваленко','Бойко','Кравченко']
Probably_of_Ms = [0.5592903, 0.794579173, 0.844686163, 0.882489301, 0.918865906, 0.941244651, 0.959700428, 0.974589872, 0.98814194, 1]
Female_names = ['Елена','Светлана','Татьяна','Анна','Анастасия','Александра','Виктория','Алена','Ксения','Валерия']
Probably_of_Fmn = [0.184092011, 0.333264047, 0.480634656, 0.622064019, 0.730236263, 0.814383703, 0.892537933, 0.934680939, 0.967556987, 1]
Female_surnames = ['Иванова','Петрова','Попова','Кузнецова','Волкова','Морозова','Григорян','Шевченко','Акопян','Арутюнян']
Probably_of_Fms = [0.350802407, 0.488465396, 0.58776329, 0.6832999, 0.761534604, 0.828736209, 0.877256771, 0.919884655, 0.961634906,  1]
Sex=["Female","Male"]
Probably_of_sex=[0.53497966, 1]

def generation_sex_and_fio(cnt):
    massiv_sex_and_fio=[]
    for i in range(cnt):
        sex_and_fio=[]
        q=random.random()
        if(q<Probably_of_sex[0]):
            sex_and_fio.append(Sex[0])
            second_name=random.random()
            for j in range(8):
                if(second_name<=Probably_of_Fms[j]):
                    sex_and_fio.append(Female_surnames[j])
                    break
            name=random.random()
            for j in range(10):
                if(name<=Probably_of_Fmn[j]):
                    sex_and_fio.append(Female_names[j])
                    break
        else:
            sex_and_fio.append(Sex[1])
            second_name = random.random()
            for j in range(8):
                if (second_name <= Probably_of_Ms[j]):
                    sex_and_fio.append(Male_surnames[j])
                    break
            name = random.random()
            for j in range(10):
                if (name <= Probably_of_Mn[j]):
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
