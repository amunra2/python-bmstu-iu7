print('Лабораторная работа №13\n')

print('Название : Уточнение корней')
print('Назначение : Уточнить все корни, пренадлежащие заданной функции\n\n')


'''
a, b - границы отрезка
h - шаг
eps - точность для нахождения корня
maxiter - макимальное количество итераций
time1, time 2 - итоговое время на каждый из методов
mistake - значение ошиибки

'''




import matplotlib.pyplot as plt

import scipy.optimize as scp
from time import perf_counter
from math import sin, fabs

eps = 1e-3
max_iter = 100

def f(x):
    return(sin(x))



def shapka():
    
    print('┌','─'*7,'┬','─'*11,'┬','─'*10,'┬','─'*10,'┬','─'*14,'┬',
          '─'*10,'┬','─'*12,'┬','─'*8,'┐',sep = '')
    print('│   №   │   Метод   │   Левая  │  Правая  ', end = '')
    print('│   Значение   │ Значение │ Количество │  Код   │')
    print('│       │           │  граница │  граница │    корня', end = '')
    print('     │ функции  │  итераций  │ ошибки │')



def stroka(numr, l, r, x, y, iterq, mis):
    
    if numr == '*':
        print('│ {:4} '.format(rnum),'│brenth_Ptn ', end = '')
    else:
        print('│      ', '│   brenth  ', end = '')
    if -10000<l<10000:
        print('│ {:8.2g} '.format(l), end = '')
    else:
        print('│ {:8.1e} '.format(l), end = '')
    if -10000<r<10000:
        print('│ {:8.2g} '.format(r), end = '')
    else:
        print('│ {:8.1e} '.format(r), end = '')
    if mis == 0:
        if -1000<x<1000:
            print('│ {:12.6f} '.format(x), end = '')
        else:
            print('│ {:12.4e} '.format(x), end = '')
        print('│ {:8.0e} │ {:>10} │ {:6} │'.format(y, iterq, mis))
    else:
        print('│ {:^12} '.format('--'), end = '')
        print('│ {:^8} │ {:^10} │ {:6} │'.format('--', '--', mis))



# brenth (Python)

def brenth_Python(fn, na, nb, xtol, maxiter):
    
    rtol = 8.881784197001252e-16
    l_x = na
    n_x = nb
    bel_x = 0.
    l_f = fn(l_x) # l - last
    n_f = fn(n_x) # n - new
    bel_f = 0.    # bel - below
    l_s = 0.
    n_s = 0.

    if l_f*n_f > 0:
        return 0, 0, 2
    
    if l_f == 0.:
        return l_x, 0, 0

    if n_f == 0.:
        return n_x, 0, 0
    
    # Алгоритм за максимальное количество итераций
    iters = 0
    for i in range(maxiter):
        iters += 1
        if l_f*n_f < 0:
            bel_x = l_x
            bel_f = l_f
            l_s = n_s = n_x - l_x

        if fabs(l_f) < fabs(n_f):
            l_x = n_x
            n_x = bel_x
            bel_x = l_x

            l_f = n_f
            n_f = bel_f
            bel_f = l_f

        delta = (xtol + rtol*fabs(n_x))/2

        # Изменение при половинном делении
        s_bis = (bel_x - n_x)/2
        
        # Достигнута точность
        if n_f == 0. or fabs(s_bis) < delta:
            return n_x, iters, 0

        # Проверка на возможность выхода за границы отрезка при более
        # быстрых методах
        if fabs(l_s) > delta and fabs(n_f) < fabs(l_f):
            if l_x == bel_x:
                s_try = -n_f*(n_x - l_x)/(n_f - l_f)
            else:
                l_d = (l_f - n_f)/(l_x - n_x)
                bel_d = (bel_f - n_f)/(bel_x - n_x)
                s_try = -n_f*(bel_f - l_f)/(bel_f*l_d - l_f*bel_d)

            # Лучший результат
            if 2*fabs(s_try) < min(3*fabs(s_bis) - delta, fabs(l_s)):
                l_s = n_s
                n_s = s_try
            else:
                l_s = s_bis
                n_s = s_bis

        else:
            l_s = s_bis
            n_s = s_bis

        l_x = n_x
        l_f = n_f

        if fabs(n_s) > delta:
            n_x += n_s
        else:
            if s_bis > 0:
                n_x += delta
            else:
                n_x -= delta
        n_f = f(n_x)
    return n_x, 0, 1




q = []


    

a, b = map(float, input('Введите начало и конец отрезка через пробел : ' ).split())
h = float(input('Введите шаг : '))

a1 = a
a2 = a + h
rnum = 0

root_set1 = set()
time1= 0

root_set2 = set()
time2 = 0

while a2 < b + h/2:
    if f(a1)*f(a2) <= 0:
        rnum += 1
        if rnum == 1:
            shapka()
        begin1 = perf_counter()
        x11, res = scp.brenth(f, a1, a2, xtol=eps, maxiter=max_iter,
                                 full_output=True, disp = False)
            
        time1 += perf_counter() - begin1
        if x11 not in root_set1:
            print('├','─'*7,'┼','─'*11,'┼','─'*10,'┼','─'*10,'┼','─'*14,'┼',
          '─'*10,'┼','─'*12,'┼','─'*8,'┤', sep = '')
            
            if res.converged:
                mistake1 = 0
            else:
                mistake1 = 1
            iters1 = res.iterations    
            if f(a1) == 0 or f(a2) == 0:
                iters1 = 0
            if iters1 > max_iter:
                mistake1 = 1
            stroka(rnum, a1, a2, x11, f(x11), iters1, mistake1)
            root_set1.add(x11)
        else:
            rnum -= 1

        begin2 = perf_counter()
        x12, iters2, mistake2 = brenth_Python(f, a1, a2, eps, max_iter)
        time2 += perf_counter() - begin2
        if x11 not in root_set2:
            stroka('*', a1, a2, x12, f(x12), iters2, mistake2)
            root_set2.add(x12)
    a1 = a2
    a2 += h

    

if f(a1)*f(a2) <= 0:
    rnum += 1
    if rnum == 1:
        shapka()
    begin1 = perf_counter()
    x11, res = scp.brenth(f, a1, a2, xtol=eps, maxiter=max_iter,
                                full_output=True, disp = False)
            
    time1 += perf_counter() - begin1
    if x11 not in root_set1:
        print('├','─'*7,'┼','─'*11,'┼','─'*10,'┼','─'*10,'┼','─'*14,'┼',
          '─'*10,'┼','─'*12,'┼','─'*8,'┤', sep = '')
        
        if res.converged:
            mistake1 = 0
        else:
            mistake1 = 1
        iters1 = res.iterations        
        if f(a1) == 0 or f(a2) == 0:
            iters1 = 0
        if iters1 > max_iter:
            mistake1 = 1
        stroka(rnum, a1, a2, x11, f(x11), iters1, mistake1)
        root_set1.add(x11)
    else:
        rnum -= 1

    begin2 = perf_counter()
    x12, iters2, mistake2 = brenth_Python(f, a1, a2, eps, max_iter)
    print(x12)
    q.append(x12)
    time2 += perf_counter() - begin2
    if x11 not in root_set2:
        stroka('*', a1, a2, x12, f(x12), iters2, mistake2)
        root_set2.add(x12)

if rnum == 0:
    print('Корни на заданном промежутке не найдены.')
else:
    print('└','─'*7,'┴','─'*11,'┴','─'*10,'┴','─'*10,'┴','─'*14,'┴',
          '─'*10,'┴','─'*12,'┴','─'*8, '┘', sep = '')
    

print('Коды ошибок:')
print('   0 - нет ошибок')
print('   1 - точность не была достигнута', end = ' ')
print('за максимальное количество итераций\n\n')


print('Сравнение во времене работы двух сетодов :')
print('  brenth из библиотеки :', '{:9.5f}'.format(time1), ' ms')
print('  brenth, написанный на Python :', '{:9.5f}'.format(time2), ' ms')




print('\n\n\n\n\n\n\n\n\n')
print(q)





















            
        



        
    
    
