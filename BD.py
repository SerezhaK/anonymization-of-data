import random
a=[[],[]]
def gn_BD(col,yn,yk):
    for i in range(col):
        y=random.randint(yn,yk)
        q=random.randint(1,12)
        if(q==1 or q==3 or q==5 or q==7 or q==8 or q==10 or q==12):
            w=random.randint(1,31)
        elif(q==4 or q==6 or q==9 or q==11):
            w=random.randint(1,30)
        elif(q==2 and y%4==0):
            w=random.randint(1,29)
        elif(q==2 and y%4!=0):
            w=random.randint(1,29)
        t = str(w) + '.' + str(q) + '.' +str(y)
        a[0].append(t)
        a[1].append(2023-y)
    return
gn_BD(1165,2017,2017)
gn_BD(1165,2016,2016)
gn_BD(6344,2010,2015)
gn_BD(1694,2008,2009)
gn_BD(1694,2006,2007)
gn_BD(2223,2004,2005)
gn_BD(6244,1999,2003)
gn_BD(5292,1994,1998)
gn_BD(8149,1989,1993)
gn_BD(9948,1984,1988)
gn_BD(8784,1979,1983)
gn_BD(7725,1974,1978)
gn_BD(7196,1969,1973)
gn_BD(6667,1964,1968)
gn_BD(7302,1959,1963)
gn_BD(6350,1954,1958)
gn_BD(11870,1924,1953)
gn_BD(300,1915,1923)

for i in range(100112):
    print(a[0][i], a[1][i])