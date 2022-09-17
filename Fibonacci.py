print("Введите число:")
def fib(n):
    a1=1
    a2=1
    a3=2
    while a3<=n:
        if n==a1 or n==a2 or n==a3:
            return print("Число принадлежит ряду Фибоначчи")
        a1,a2,a3 = a2,a3,a2+a3
    print("Число не принадлежит ряду Фибоначчи")
n=int(input())
fib(n)