print('Лабораторная работа №11')
print()
print('Название программы : Меню и файлы')
print('Назначение программы : Работа с меню')
print()
print()
print()

# t - для основного файла
# c - для копии файла
# name - имя выбранного файла
# pole - поле, по которому производится поиск
# n - количество новых записей

def copy1():
    t = open('f.txt', 'w')
    c = open('copy1.txt')
    for i in c:
        t.write(i)
    t.close()
    c.close()

def copy2():
    t = open('foot.txt', 'w')
    c = open('copy2.txt')
    for i in c:
        t.write(i)
    t.close()
    c.close()



choice = None
while choice != '0':
    print(
        '''
    1) Выбор файла
    2) Создание в файле новых записей
    3) Добавление записей
    4) Вывод всех записей
    5) Поиск по одному полю
    6) Поиск по двум полям

    0) Выход
    ''')

    choice = input('Введите пункт меню : ')

    if choice == '1':
        print(
            '''
Файлы на выбор:

     f.txt
     foot.txt
    ''')
        name = input('\nВведите имя файла : ')
        if name != 'f.txt':
            if name != 'foot.txt':
                print('\nТакого файла нет.\n\n')
            else:
                print('\nФайл выбран.\n\n')
        else:
            print('\nФайл выбран.\n\n')

        if name == 'f.txt':
            copy1()
        elif name == 'foot.txt':
            copy2()




    elif choice == '2':
        t = open(name, 'w')
        print('\n\nСколько записей Вы собираетесь добавить : ')
        n = int(input())
        
        print('\nВведите записи по одной в строке : ')
        for i in range(n):
            t.write(input()+'\n')

        t.close()


    elif choice == '3':
        t = open(name)

        f = open('temp.txt', 'w')
        for i in t:
            f.write(i)
        
        t.close()
        print('\n\nСколько записей Вы собираетесь добавить : ')
        n = int(input())
        
        print('\nВведите записи по одной в строке : ')
        for i in range(n):
            f.write(input()+'\n')

        f.close()
        
        f = open('temp.txt')
        t = open(name, 'w')

        for i in f:
            t.write(i)
        f.close()
        t.close()


    elif choice == '4':
        t = open(name)
        t = sorted(t)
        print()
        for i in t:
            print(i, end = '')



    elif choice == '5':
        print(
            '''
Выберите пункт, по которому будет производится поиск :

    1. Фамилия футболиста
    2. Клуб
    3. Страна
    
            ''')
        pole = input()
        print('\n')
        t = open(name)
        t = sorted(t)
        k = 0
        a = [0]*3
        c = 1
        


        if pole == '1':
            print('Введите желаемый объект поиска : ', end = '')
            naz = input('')

            print('\n')
            for i in t:
                с = 1
                if naz in i:
                    k += 1
                    
                    a = i.split()
                    
                    for j in range(len(a)):
                        if a[j] != naz:
                            c += 1
                        else:
                            break
                        
                    if (j+1) == 1:
                        print(i, end = '')
                    с = 1
                    a = []
                    
                    
                







                

        if pole == '2':
            print('Введите желаемый объект поиска : ', end = '')
            naz = input('')
            print('\n')
            for i in t:
                с = 1
                if naz in i:
                    k += 1
                    
                    a = i.split()
                    
                    for j in range(len(a)):
                        if a[j] != naz:
                            c += 1
                        else:
                            break
                        
                    if (j+1) == 2:
                        print(i, end = '')
                    с = 1
                    a = []

        if pole == '3':
            print('Введите желаемый объект поиска : ', end = '')
            naz = input('')
            print('\n')
            for i in t:
                с = 1
                if naz in i:
                    k += 1
                    
                    a = i.split()
                    
                    for j in range(len(a)):
                        if a[j] != naz:
                            c += 1
                        else:
                            break
                        
                    if (j+1) == 3:
                        print(i, end = '')
                    с = 1
                    a = []


            
            '''
            print('Введите желаемый объект поиска : ', end = '')
            naz = input('')
            print('\n')
            for i in t:
                if naz in i:
                    k += 1
                    print(i)
            '''

        if k == 0:
            print('Таких записей нет.\n')

        #t.close()

    

    elif choice == '6':
        t = open(name)
        t = sorted(t)
        print(
        '''
Выберите 2 поля, по которым хотите осуществить поиск:

    1. Фамилия футболиста
    2. Клуб
    3. Страна
    '''
        )
        num1,num2 = map(str,input('Выбор: ').split())
        k = 0
        if (num1 == '1' and num2 == '2') or (num1 == '2' and num2 == '1'):
            print('Введите значения полей: ', end = '')
            if num1 == '1' and num2 == '2':
                fam, club = map(str,input('').split())
            else:
                club,fam = map(str,input('').split())
            print()
            for line in t:
                if (club in line) and (fam in line):
                    k += 1
                    print(line)
        elif (num1 == '2' and num2 == '3') or (num1 == '3' and num2 == '2'):
            print('Введите значения полей: ', end = '')
            if num1 == '2' and num2 == '3':
                club,strana = map(str,input().split())
            else:
                strana,club = map(str,input().split())
            print()
            for line in t:
                if (strana in line) and (club in line):
                    k += 1
                    print(line)
        elif (num1 == '1' and num2 == '3') or (num1 == '3' and num2 == '1'):
            print('Введите значения полей: ', end = '')
            if num1 == '1' and num2 == '3':
                fam,strana = map(str,input('').split())
            else:
               strana,fam = map(str,input('').split()) 
            print()
            for line in t:
                if (fam in line) and (strana in line):
                    k += 1
                    print(line)
        if k == 0:
            print('Записей содержащих данные значения полей не существует')
        #t.close()
            
        
            

            
        

    
        
        
        


