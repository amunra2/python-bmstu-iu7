print('Лабораторная работа №9')
print()
print('Название программы : Файлы и Множества')
print('Назначение программы : 1. Создать новый файл с поменяными строками')
print()
print()
print()

# newf, oldf - новый и старый файлы
# n, m - переменные для нахождения строк




newf = open('R.txt', 'w')
oldf = open('Sf.txt', 'r')

n = 1

# Вписываем нечётные строки :
for i in oldf:
    if n % 2 != 0:
        newf.write(i)
    n +=1

oldf.close()
print()

m = 1

# Вписываем чётные строки :
oldf = open('Sf.txt', 'r')
for j in oldf:
    if m % 2 == 0:
        newf.write(j)
    m += 1
    
oldf.close()   
newf.close()



    
