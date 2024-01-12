import random
a=[[],[]]
s="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def gn_ps(col,b,c):
    for i in range(col):
        t=""
        for j in range(b):
            t+=s[random.randint(0,25)]
        for j in range(c):
            t+=str(random.randint(0,9))
        x=random.randint(1,89)
        if(x<10):
            f='0'+str(x)
        else:
            f=str(x)
        for j in range(10):
            f+=str(random.randint(0,9))
        a[0].append(t)
        a[1].append(f)
gn_ps(690,1,6) #паспорта Таджикистана
gn_ps(220,0,15) #паспорта Узбекистана
gn_ps(150,0,9) #паспорта Украины
gn_ps(250,2,7) #паспорта Армении,Кыргызстана,Молдовы и Беларуси
gn_ps(130,1,7) #паспорта Азербайджана и Туркменистана



for i in range(160): #паспорта Казахстана
    v="N"
    for j in range(8):
        v+=str(random.randint(0,9))
    d = random.randint(1, 89)
    if (d < 10):
        k = '0' + str(d)
    else:
        k = str(d)
    for j in range(10):
        k += str(random.randint(0, 9))
    a[0].append(v)
    a[1].append(k)

for i in range(98400): #паспорта России
    v=""
    for j in range(4):
        v+=str(random.randint(0,9))
    v+=' '
    for j in range(6):
        v+=str(random.randint(0,9))
    d = random.randint(1, 89)
    if (d < 10):
        k = '0' + str(d)
    else:
        k = str(d)
    for j in range(10):
        k += str(random.randint(0, 9))
    a[0].append(v)
    a[1].append(k)


for i in range(0,1000,2):
    print(a[0][i],a[1][i])
