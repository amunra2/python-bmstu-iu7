print('Лабораторная работа №3')
print()
print('Название программы : Таблица значений функций.')
print()
print('Назначение программы : Вычислить таблицу значений функций.')
print()

# p1, p2 - значения функций
# t, p - темповые переменные
# amount - количество значений p1 из диапазона
# k - количество повторний цикла
# a - начальное значение
# b - конечное значение
# step - значение шага
# max1 - максимум функции
# min1 - минимум функции
# max12 - разность между максимумом и минимумом
# zas - количество засечек
# m0 - расстояние до оси X
# m1 - расстояние до точки на графике

from math import sin, cos
a = float(input('Введите начальное значение : ' ))
b = float(input('Введите конечное значение : ' ))
step = float(input('Введите значение шага : '))

# Вычисляем количество шагов цикла и находим max и min :
k = int((b - a)/step)
t = a
max1 = -999999999
min1 = 9999999999


for i in range(k+1):
    p1 = t*t - 1
    if p1 > max1:
        max1 = p1
    if p1 < min1:
        min1 = p1
    t = t + step

zas = int(input('Количество засечек : '))

# Находим ось Y и значения над ней :
k = 70/zas
max12 = max1 - min1
k = int(k)
p = min1
if abs(p) < 50: 
    p = p
elif 50 <= abs(p) < 100:
    p = p/10
elif 100 <= abs(p) <= 1000:
    p = p/100

q =''
t = max12/zas
if min1 >= 0:
    if abs(t) < 50:
        if 4 <= zas <= 8:
            for i in range(1,zas):
                p = p + t
                n = str('{:<.1f}'.format(p))
                q = q + ' '*(k-3) + n
    elif 50 <= abs(t) < 100:
        t = t/10
        if 4 <= zas <= 8:
            for i in range(1,zas):
                p = p + t
                n = str('{:<.1f}'.format(p))
                q = q + ' '*(k-3) + n
    elif 100 <= abs(t) <= 1000:
        t = t/100
        if 4 <= zas <= 8:
            for i in range(1,zas):
                p = p + t
                n = str('{:<.1f}'.format(p))
                q = q + ' '*(k-3) + n
     
else:
    if abs(t) < 50:
        if 4 <= zas <= 8:
            for i in range(1,zas):
                p = p + t
                n = str('{:<.1f}'.format(p))
                q = q + ' '*(k-4) + n
    elif 50 <= abs(t) < 100:
        t = t/10
        if 4 <= zas <= 8:
            for i in range(1,zas):
                p = p + t
                n = str('{:<.1f}'.format(p))
                q = q + ' '*(k-4) + n
    elif 100 <= abs(t) <= 1000:
        t = t/100
        if 4 <= zas <= 8:
            for i in range(1,zas):
                p = p + t
                n = str('{:<.1f}'.format(p))
                q = q + ' '*(k-4) + n

print()
print('Функция p1 = sin(t) + 0.6*t*cos(t) обозначается звёздочкой (*).')
print()

if abs(min1) < 100:
    print('   ', round(min1,1) ,q )
elif abs(min1) >= 100:
    print('   ', round(min1/100,1) ,q )
print(' X  ', '\u2514' + ('\u2500'*(k-1) + '\u2534')*(zas - 2) +'\u2500'*(k-1) +\
      '\u2518' )
t = a
k = int((b - a)/step)
for i in range(k+1):
    if min1 > 0 or max1 < 0:
        print('{: 2.1f}'.format(t), end='')
        p1 =  t*t - 1
    
        m1 = ((p1 - min1)/(max1 - min1))*49 + 1
        m1 = int(m1)
        print(' '*m1 + '*')
        t = t + step
    else:
        print('{: 2.1f}'.format(t), end='')
        p1 =  t*t - 1
        m2 = int((0-min1)/(max1-min1)*69 + 1)
        m1 = ((p1 - min1)/(max1 - min1))*49 + 1
        m1 = int(m1)
        if m2 < m1:
            print(' '*m2 + '\u2503' + ' '*(m1 - m2 - 1) + '*')
        elif m2 > m1:
            print(' '*m1 + '*' + ' '*(m2 - m1 - 1) + '\u2503')
        elif m1 == m2:
            print(' '*m1 + '*')
        t = t + step
        
        
        
        

        
        











