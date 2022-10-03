print("Выберите операцию, которую хотите произвести над матрицей(-ами):"
      "\n (1)Транспонирование матрицы"
      "\n (2)Умножение двух матриц"
      "\n (3)Определение ранга матрицы")
f=int(input())
if f==1:
    print("Выберите размер матрицы из списка ниже:"
      "\n (1)1x2"
      "\n (2)2x1"
      "\n (3)1x3"
      "\n (4)3x1"
      "\n (5)2x2"
      "\n (6)3x3")
    r=int(input())
    if r==1:
        print("Введите элементы матрицы а11,а12")
        m1=[int(input()), int(input())]
        print("Транспонированная матрица:")
        print(m1[0])
        print(m1[1])
    elif r==2:
        print("Введите элементы матрицы а11,а21")
        m2=[int(input()), int(input())]
        print("Транспонированная матрица:")
        print(m2[0],m2[1])
    elif r==3:
        print("Введите элементы матрицы а11,а12,a13")
        m3=[int(input()), int(input()), int(input())]
        print("Транспонированная матрица:")
        print(m3[0])
        print(m3[1])
        print(m3[2])
    elif r==4:
        print("Введите элементы матрицы а11,а21,a31")
        m4=[int(input()), int(input()), int(input())]
        print("Транспонированная матрица:")
        print(m4[0],m4[1],m4[2])
    elif r==5:
        print("Введите элементы матрицы а11,а12,a21,a22")
        m5=[int(input()), int(input()), int(input()), int(input())]
        print("Транспонированная матрица:")
        print(m5[0],m5[2])
        print(m5[1],m5[3])
    elif r==6:
        print("Введите элементы матрицы а11,а12,a13,a21,a22,a23,a31,a32,a33")
        m6=[int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input())]
        print("Транспонированная матрица:")
        print(m6[0],m6[3],m6[6])
        print(m6[1],m6[4],m6[7])
        print(m6[2],m6[5],m6[8])
elif f==2:
    print("Выберите размер первой матрицы из списка ниже:"
          "\n (1)1x2"
          "\n (2)2x1"
          "\n (3)1x3"
          "\n (4)3x1"
          "\n (5)2x2"
          "\n (6)3x3")
    r1 = int(input())
    print("Выберите размер второй матрицы из списка ниже:"
          "\n (1)1x2"
          "\n (2)2x1"
          "\n (3)1x3"
          "\n (4)3x1"
          "\n (5)2x2"
          "\n (6)3x3")
    r2 = int(input())
    if r1==1 and r2==2:
        print("Введите элементы первой матрицы а11,а12")
        m1 = [int(input()), int(input())]
        print("Введите элементы второй матрицы а11,а21")
        m2 = [int(input()), int(input())]
        mf1=[m1[0]*m2[0]+m1[1]*m2[1]]
        print("Результат умножения двух матриц:")
        print(mf1)
    elif r1==1 and r2==5:
        print("Введите элементы первой матрицы а11,а12")
        m1 = [int(input()), int(input())]
        print("Введите элементы второй матрицы а11,а12,а21,а22")
        m2 = [int(input()), int(input()), int(input()), int(input())]
        mf2=[m1[0]*m2[0]+m1[1]*m2[2],m1[0]*m2[1]+m1[1]*m2[3]]
        print("Результат умножения двух матриц:")
        print(mf2)
    elif r1==2 and r2==1:
        print("Введите элементы первой матрицы а11,а21")
        m1 = [int(input()), int(input())]
        print("Введите элементы второй матрицы а11,а12")
        m2 = [int(input()), int(input())]
        mf3=[m1[0]*m2[0],m1[0]*m2[1],m1[1]*m2[0],m1[1]*m2[1]]
        print("Результат умножения двух матриц:")
        print(mf3[0],mf3[1])
        print(mf3[2],mf3[3])
    elif r1 == 2 and r2 == 3:
        print("Введите элементы первой матрицы а11,а21")
        m1 = [int(input()), int(input())]
        print("Введите элементы второй матрицы а11,а12,a13")
        m2 = [int(input()), int(input()), int(input())]
        mf4 = [m1[0]*m2[0],m1[0]*m2[1],m1[0]*m2[2],m1[1]*m2[0],m1[1]*m2[1],m1[1]*m2[2]]
        print("Результат умножения двух матриц:")
        print(mf4[0], mf4[1], mf4[2])
        print(mf4[3], mf4[4], mf4[5])
    elif r1 == 3 and r2 == 4:
        print("Введите элементы первой матрицы а11,а12,a13")
        m1 = [int(input()), int(input()), int(input())]
        print("Введите элементы второй матрицы а11,а21,a31")
        m2 = [int(input()), int(input()), int(input())]
        mf5 = [m1[0]*m2[0]+m1[1]*m2[1]+m1[2]*m2[2]]
        print("Результат умножения двух матриц:")
        print(mf5)
    elif r1 == 3 and r2 == 6:
        print("Введите элементы первой матрицы а11,а12,a13")
        m1 = [int(input()), int(input()), int(input())]
        print("Введите элементы второй матрицы а11,a12,a13,а21,a22,a23,a31,a32,a33")
        m2 = [int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input())]
        mf6 = [m1[0]*m2[0]+m1[1]*m2[3]+m1[2]*m2[6],m1[0]*m2[1]+m1[1]*m2[4]+m1[2]*m2[7],m1[0]*m2[2]+m1[1]*m2[5]+m1[2]*m2[8]]
        print("Результат умножения двух матриц:")
        print(mf6[0], mf6[1], mf6[2])
    elif r1 == 4 and r2 == 1:
        print("Введите элементы первой матрицы а11,а21,a31")
        m1 = [int(input()), int(input()), int(input())]
        print("Введите элементы второй матрицы а11,а12")
        m2 = [int(input()), int(input())]
        mf7 = [m1[0] * m2[0], m1[0] * m2[1], m1[1] * m2[0], m1[1] * m2[1], m1[2] * m2[0], m1[2] * m2[1]]
        print("Результат умножения двух матриц:")
        print(mf7[0], mf7[1])
        print(mf7[2], mf7[3])
        print(mf7[4], mf7[5])
    elif r1 == 4 and r2 == 3:
        print("Введите элементы первой матрицы а11,а21,a31")
        m1 = [int(input()), int(input()), int(input())]
        print("Введите элементы второй матрицы а11,a12,a13")
        m2 = [int(input()), int(input()), int(input())]
        mf8 = [m1[0]*m2[0],m1[0]*m2[1],m1[0]*m2[2],m1[1]*m2[0],m1[1]*m2[1],m1[1]*m2[2],m1[2]*m2[0],m1[2]*m2[1],m1[2]*m2[2]]
        print("Результат умножения двух матриц:")
        print(mf8[0], mf8[1], mf8[2])
        print(mf8[3], mf8[4], mf8[5])
        print(mf8[6], mf8[7], mf8[8])
    elif r1 == 5 and r2 == 2:
        print("Введите элементы первой матрицы а11,a12,а21,a22")
        m1 = [int(input()), int(input()), int(input()), int(input())]
        print("Введите элементы второй матрицы а11,а21")
        m2 = [int(input()), int(input())]
        mf9 = [m1[0] * m2[0]+m1[1] * m2[1], m1[2] * m2[0]+ m1[3] * m2[1]]
        print("Результат умножения двух матриц:")
        print(mf9[0])
        print(mf9[1])
    elif r1 == 5 and r2 == 5:
        print("Введите элементы первой матрицы а11,a12,а21,a22")
        m1 = [int(input()), int(input()), int(input()), int(input())]
        print("Введите элементы второй матрицы а11,a12,а21,a22")
        m2 = [int(input()), int(input()), int(input()), int(input())]
        mf10 = [m1[0] * m2[0] + m1[1] * m2[2], m1[0] * m2[1] + m1[1] * m2[3],m1[2] * m2[0] + m1[3] * m2[2], m1[2] * m2[1] + m1[3] * m2[3]]
        print("Результат умножения двух матриц:")
        print(mf10[0],mf10[1])
        print(mf10[2],mf10[3])
    elif r1 == 6 and r2 == 4:
        print("Введите элементы первой матрицы а11,a12,a13,а21,a22,a23,a31,a32,a33")
        m1 = [int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input())]
        print("Введите элементы второй матрицы а11,a21,а31")
        m2 = [int(input()), int(input()), int(input())]
        mf11 = [m1[0] * m2[0] + m1[1] * m2[1]+ m1[2] * m2[2], m1[3] * m2[0]+m1[4] * m2[1] + m1[5] * m2[2], m1[6] * m2[0] + m1[7] * m2[1]+m1[8]*m2[2]]
        print("Результат умножения двух матриц:")
        print(mf11[0])
        print(mf11[1])
        print(mf11[2])
    elif r1 == 6 and r2 == 6:
        print("Введите элементы первой матрицы а11,a12,a13,а21,a22,a23,a31,a32,a33")
        m1 = [int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input())]
        print("Введите элементы второй матрицы а11,a12,a13,а21,a22,a23,a31,a32,a33")
        m2 = [int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input())]
        mf12 = [m1[0] * m2[0] + m1[1] * m2[3]+ m1[2] * m2[6], m1[0] * m2[1]+m1[1] * m2[4] + m1[2] * m2[7], m1[0] * m2[2] + m1[1] * m2[5]+m1[2]*m2[8],m1[3] * m2[0] + m1[4] * m2[3]+ m1[5] * m2[6], m1[3] * m2[1]+m1[4] * m2[4] + m1[5] * m2[7], m1[3] * m2[2] + m1[4] * m2[5]+m1[5]*m2[8],m1[6] * m2[0] + m1[7] * m2[3]+ m1[8] * m2[6], m1[6] * m2[1]+m1[7] * m2[4] + m1[8] * m2[7], m1[6] * m2[2] + m1[7] * m2[5]+m1[8]*m2[8],]
        print("Результат умножения двух матриц:")
        print(mf12[0],mf12[1],mf12[2])
        print(mf12[3],mf12[4],mf12[5])
        print(mf12[6],mf12[7],mf12[8])
    else:
        print("Ошибка! Умножение матриц данных размеров невозможно!")
elif f==3:
    print("Выберите размер матрицы из списка ниже:"
          "\n (1)2x2"
          "\n (2)3x3")
    print("Операцию определения ранга, к сожалению, не успел сделать хоть в каком-либо виде:(")
else:
    print("Ошибка! Неверный код операции")
