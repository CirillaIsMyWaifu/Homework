import random as r

s=[]
print("Введите количество элементов списка:")
N=int(input())
for i in range(0, N):
    s.append(r.randint(0,1))
print("Ваш список:")
print(s)

def check(s):
    for i in range(0, N):
        k = 0
        checker = i
        while s[checker] == s[i] and checker >= 0:
            k += 1
            checker -= 1
        if s[i] == 0:
            for f in range(k):
                zeroes[f] += 1
        else:
            for f in range(k):
                ones[f] += 1
zeroes=[0 for i in range(s.count(0))]
ones=[0 for k in range(s.count(1))]

zero=s.count(0)
zero_percent=zero/N*100
one=s.count(1)
one_percent=one/N*100
print("\nПроцентное отношение для элемента 0")
print(zero_percent,"%",sep='')
print("Процентное отношение для элемента 1")
print(one_percent,"%",sep='')

check(s)
print("\nИдущие подряд нули (<сколько нулей идёт подряд> — <сколько раз встречается> — <процентное отношение>:")
for j in range(1,len(zeroes)):
    if zeroes[j]!=0:
        print("[",(j+1),"]", "0"*(j+1)," — ",zeroes[j]," раз"," — ",zeroes[j]*(j+1)*100/len(s),"%",sep='')
print("\nИдущие подряд единицы (<сколько единиц идёт подряд> — <сколько раз встречается> — <процентное отношение>:")
for j in range(1,len(ones)):
    if ones[j]!=0:
        print("[",(j+1),"]", "1"*(j+1)," — ",ones[j]," раз"," — ",ones[j]*(j+1)*100/len(s),"%",sep='')