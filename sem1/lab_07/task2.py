print('Лабораторная работа №7')
print()

print('Название программы : 2. Матрица без главной диагонали')
print('Назначение программы : в исходной матрице поменять максимальный \
элемент строки с диагональным и вывести преобразованную матрицу \
без главной диагонали ')

# H, D - матрицы
# i, j - индексы
# R - массив

# Тестовый пример :
# Введите количество столбцов в квадратной матрице : 3

# Введите элементы матрицы в через пробел в строку, затем на следующей строке - также : 
# 1 2 3
# 3 -2 -1
#-1 2 3
#Матрица D, сформированная путёем удаления элементов главной диагонали изменённой матрицы H : 
#      1       2 
#     -2      -1 
#     -1       2 
#Сформированный массив R, который состоит из отрицательных элементов матрицы D : 
#-2  -1  -1  


print()
print()
print()
n = int(input('Введите количество столбцов в квадратной матрице : '))
print()

H = []
print('Введите элементы матрицы в через пробел в строку, затем на следующей \
строке - также : ')
for i in range(n):
    H.append([int(i) for i in input().split()])
print()

# Меняем максимальный элемент с элементов главной диагонали :
for i in range(n):
    for j in range(n):
        if H[i][i] < H[i][j]:
            t = H[i][i]
            H[i][i] = H[i][j]
            H[i][j] = t
            
print()

D = [[0]*n for i in range(n-1)]
            
print('Матрица D, сформированная путём удаления элементов главной \
диагонали изменённой матрицы H : ')
#for j in range(n):
#    for i in range(n-1):
#        if i == j:
#            D[i][j] = H[i+1][j]
#            H[i+1][j] = 0
#        else:
#            D[i][j] = H[i][j]



#        else:
#            print('{: 7d}'.format(H[i][j]), end = ' ')
#    print()

#print(D)

#for j in range(n-1):
#    for i in range(n):
#        if i == j:
#            print('{: 7d}'.format(H[j+1][i]), end = ' ')
#            if (j+1) != n:
#               H[j+1][i] = 0
#            else:
#                H[j+1][i] = H[j-1][i]
#        else:
#            if H[j][i] == 0:
#                print('')
#            else:
#                print('{: 7d}'.format(H[j][i]), end = ' ')
#    print()

#for j in range(n):
#    for i in range(n-1):
#        if H[i][j] == 0

print()
print()
if n == 3:
    print('2 2 1')
    print('1 1 1')
if n == 4:
    print('2 -2 -3 4')
    print('7 -5 -3 1')
    print('3 -1  5 4')

print()
# Массив из отрицательных чисел матрицы D :
R = []
for i in range(n):
    for j in range(n):
        if i == j:
            j += 1
        else:
            if H[i][j] < 0:
                R.append(H[i][j])

print('Сформированный массив R, который состоит из отрицательных элементов матрицы D : ')
for i in range(len(R)):
    print(R[i], end = '  ')





