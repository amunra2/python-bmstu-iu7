print('Лабораторная работа №10')
print()
print('Название программы : Файл и процедуры')
print('Назначение программы : Отсортировать файл по возрастанию')
print()
print()
print()


# xmin - минимальный элемент
# xmax - максимальный элемент
# G - файл R.txt
# t - дополнительный файл t.txt

def Sorter(t):
    # Нахождение минимального и максимального элементов матрицы :
    xmax = int(File().readline())
    xmin = int(File().readline())
    print(xmin, xmax)
    for i in File():
        if int(i) > xmax:
            xmax = int(i)
        if int(i) < xmin:
            xmin = int(i)
    print(xmin, xmax)
    # Вписывание элементов в новый файл :
    x = xmin - 1
    xmin = xmax + 1
    print(xmin, xmax)
    for i in range(M):
        q = 0
        for j in File():
            if int(j) < xmin and int(j) > x:
                xmin = int(j)
                q = 1
            elif int(j) == xmin:
                q += 1
        for i in range(q):
            t.write(str(xmin)+'\n')


        x = xmin
        xmin = xmax + 1
       
def File():
    G = open('R.txt')
    return(G)

def InputV(M):
    G = open('R.txt', 'w')
    for i in range(M):
        G.write(str(input()))
        G.write('\n')
    G.close()
    
def OutputP(M):
    t = open('t.txt', 'r')
    G = open('R.txt', 'r')
    print('Исходный файл :')
    for i in G:
        print(i)
    print('\n\n')
    print('Отсортированный по возрастанию файл :')
    for i in t:
        print(i)
    t.close

M = int(input('Введите количество чисел (от 1 до 8) :'))

print('Введите элементы по одному в строке :')
InputV(M)
t = open('t.txt', 'w')
Sorter(t)
t.close()
OutputP(M)

























#    p = int(G.readline())

#    for i in range(M-1):
#        for j in range(M-i-1):
#            s = int(G.readline())
#            if s < p:
#                s, p = p, s
#            
#            t.write(str(p))
#            p = s



#    for i in range(M-1):
#        for j in range(M-i-1):
#                j += 1
#            else:
#                if int(s[j]) > int(s[j+1]):
#                    s[j],s[j+1] = s[j+1],s[j]


