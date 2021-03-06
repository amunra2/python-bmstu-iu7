print('Лабораторная работа №7')
print()
print('Название программы : 1. Матрица по формуле')
print('Назначение программы : написать матрицу по формуле и образовать \
вектор W')
print()
print()
print()

# f - матрица
# W - вектор
# z - массив
# n - количество строк в матрице
# y - параметр функции f[m][k] = z[k]*log(y)
# s - сумма
# maxs, mins - максимальная и минимальная сумма элементов в строке матрицы
# m, k, i, c, t - цикловые переменные




# Тестовый пример :

# При матрице из 2 строк и элемментах массива z 1, 2

# Массив, образованный по формуле f[m][k] = z[k]*log(y) : 

#  -2.3026      -4.6052    
#  -1.8971      -3.7942    

# Вектор W, который образован так : сначала элементы строки матрицы
# с наибольшей суммой, затем - с наименьшей  : 

# -1.8971 -3.7942 -2.3026 -4.6052 





from math import log

n = int(input('Введите количество строк (не больше 12) : '))
z = input('Введите массив значений z в строчку через пробел (не больше 10) : ')
z = list(z.split())
y = 0.1
f = [[0]*len(z) for i in range(n)]

print()
print()
print('Матрица, образованнаая по формуле f[m][k] = z[k]*log(y) : ')
print()

# Вывод сформированной матрицы :

for m in range(n):
    for k in range(len(z)):
        f[m][k] = float(z[k])*log(y)
        print('{: 9.4f}'.format(f[m][k]), end = '    ')
    print()
    y += 0.05

W = [0]*len(z)*2

s = 0

# Поиск начального значения максимума и минимума суммы :

for k in range(len(z)):
    s += f[1][k]
    maxs = s
    mins = s
    t = 1
    c = 1

# Нахождение максимума и минумамы суммы :

for m in range(n):
    for k in range(len(z)):
        s += f[m][k]
    if s > maxs:
        maxs = s
        t = m
    if s < mins:
        mins = s
        c = m
    s = 0

print()
print('Вектор W, который образован так : сначала элементы строки матрицы с \
наибольшей суммой, затем - с наименьшей  : ')
print()

# Вывод сформированного вектора :
for i in range(len(W)):
    if i < len(z):
        W[i] = f[t][i]
        j = 0
    else: 
        W[i] = f[c][j]
        j += 1
    print('{: 5.4f}'.format(W[i]), end = ' ')
    
        
        

        


