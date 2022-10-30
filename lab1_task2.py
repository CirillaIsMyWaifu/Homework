import math

print("Введите необходимую функцию из списка ниже:"
      "\n (1)Сложение (a+b)"
      "\n (2)Вычитание (a-b)"
      "\n (3)Умножение (a*b)"
      "\n (4)Деление (a/b)"
      "\n (5)Возведение в степень (a^b)"
      "\n (6)Логарифм (числа b по основанию a)")
f = int(input())
if f==1 or f==2 or f==3 or f==4 or f==5 or f==6:
   print("Введите первый элемент")
   a = int(input())
   print("Введите второй элемент")
   b = int(input())
   if f==1:
     r=a+b
   if f==2:
     r=a-b
   if f==3:
     r=a*b
   if f==4:
     try:
       r = float(a/b)
     except:
       print("Ошибка! Деление на ноль!")
       exit
   if f==5:
     r=a**b
   if f==6:
     r=math.log(a,b)
   print("Ответ:"
      "\n",r)
else:
    print("Данное значение не является значением операции!")
    exit
