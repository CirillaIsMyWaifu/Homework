print("Введите элементы матрицы а11,a12,a13,a21,a22,a23,a31,a32,a33")
m=[int(input()),int(input()),int(input()),int(input()),int(input()),int(input()),int(input()),int(input()),int(input())]
det=m[0]*m[4]*m[8]+m[1]*m[5]*m[6]+m[2]*m[3]*m[7]-m[0]*m[5]*m[7]-m[1]*m[3]*m[8]-m[2]*m[4]*m[6]
if det==0:
    print("Определитель матрицы равен нулю! Обратной матрицы не существует!")
    quit()
else:
    mt=[m[0],m[3],m[6],m[1],m[4],m[7],m[2],m[5],m[8]]
    a11=mt[4]*mt[8]-mt[5]*mt[7]
    a12=(-1)*(mt[3]*mt[8]-mt[5]*mt[6])
    a13=mt[3]*mt[7]-mt[4]*mt[6]
    a21=(-1)*(mt[1]*mt[8]-mt[2]*mt[7])
    a22=mt[0]*mt[8]-mt[2]*mt[6]
    a23=(-1)*(mt[0]*mt[7]-mt[1]*mt[6])
    a31=mt[1]*mt[5]-mt[2]*mt[4]
    a32=(-1)*(mt[0]*mt[5]-mt[2]*mt[3])
    a33=mt[0]*mt[4]-mt[1]*mt[3]
    mA=[a11,a12,a13,a21,a22,a23,a31,a32,a33]
    mM=float(1/det)
    mTrans=[mA[0]*mM,mA[1]*mM,mA[2]*mM,mA[3]*mM,mA[4]*mM,mA[5]*mM,mA[6]*mM,mA[7]*mM,mA[8]*mM]
    print("Обратная матрица:")
    print(mTrans[0],mTrans[1],mTrans[2])
    print(mTrans[3],mTrans[4],mTrans[5])
    print(mTrans[6],mTrans[7],mTrans[8])