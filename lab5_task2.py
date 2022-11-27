import matplotlib.pyplot as plt
import numpy as np
import random as r

s=[]
print("Введите количество элементов списка:")
N=int(input())
for i in range(0, N):
    s.append(r.randint(0,1))
print("Ваш список:")
print(s)

mean=sum(s)/len(s)
print("Математическое ожидание:")
print(mean)

s2n=sum((i-mean)**2 for i in s)/len(s)
print("Среднеквадратическое отклонение:")
print(s2n)

def coef(x, y):
    n=np.size(x)
    m_x=np.mean(x)
    m_y=np.mean(y)
    SS_xy=np.sum(y*x)-n*m_y*m_x
    SS_xx=np.sum(x*x)-n*m_x*m_x
    b_1=SS_xy/SS_xx
    b_0=m_y-b_1*m_x
    return b_0,b_1

def graph(x, y, b):
    sc=plt.scatter(x,y,color="orange",marker="o",s=30)
    y_pred=b[0]+b[1]*x
    plt.plot(x,y_pred,color="blue")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

vec_x=[]
vec_y=[]
for i in range(len(s)):
    vec_x.append(i + 1)
    vec_y.append(s[i])
vec_x=np.array(vec_x)
vec_y=np.array(vec_y)
graph(vec_x, vec_y, coef(vec_x, vec_y))
