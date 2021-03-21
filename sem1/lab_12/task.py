print('Лабораторная работа №12')
print()
print('Название программы : Текст')
print('Назначение программы : Работа с текстом')
print()
print()
print()


text = [' Приветствую каждого читателя. Сегодня я с радостью ',
        '    расскажу Вам прекрасный рецепт лабораторной ',
        '   работы по программированию. Вам точно понадобится 4 + 4',
        '  придумать алгоритм и записать его на нужном ',
        '     языке программирования. Затем Вам нужно написать 7 - 1 ',
        'комментарий к каждому сложному моменту программы. Далее ',
        '  следует описать все 4.454 + 3.2424 переменные. И также Вам пригодится ',
        '   тестовый пример. Питон  Питон Питон !']
'''
def dlina():
    temp = 0
    print(i)
    for j in range(len(t[i])):
        temp = temp + len(t[i][j]) + 1
'''


t = []
for i in range(len(text)):
    t.append(text[i].split())



    
choice = None
while choice != '0':
    print(
        '''
    1) Выравнивание по левому краю
    2) Выравнивание по правому краю
    3) Выравнивание по ширине
    4) Замена слова на другое
    5) Удаление слова
    6) Преобразование арифметических операций
    7) Индивидуальное задание (Coming soon)

    0) Выход
    ''')

    choice = input('Введите пункт меню : ')



    dlin = []
    tmax = len(t[i])
    for i in range(len(t)):
        temp = -1
        for j in range(len(t[i])):
            temp = temp + len(t[i][j]) + 1
        dlin.append(temp)
        if temp > tmax:
            tmax = temp
        



            
    if choice == '1':
        print()
            
        for i in range(len(t)):
            for j in range(len(t[i])):
                print(t[i][j], end = ' ')
            print()
            
            
    elif choice == '2':
        print()

        for i in range(len(t)):
            print(' '*(tmax - dlin[i]), end ='')
            for j in range(len(t[i])):
                  print(t[i][j], end = ' ')
            print()


    elif choice == '3':
        print()
        
        n = 0
        ost = 0
        for i in range(len(t)):
            temp = 0
            temp = tmax - dlin[i] + len(t[i])
            
            n = temp//(len(t[i])-1)
            ost = temp % (len(t[i])-1)
            print((t[i][0]+' '*(n + ost)), end ='')
            for j in range(1, len(t[i])):
                print((t[i][j]+' '*n), end = '')
            print()

        
            

    elif choice == '4':
        print()

        word = input('Введите слово, которое хотите заменить : ')
        wordr = input('Введите слово, на которое хотите заменить : ')
        print('\n\n')
        for i in range(len(t)):
            for j in range(len(t[i])):
                if t[i][j][1:] == word[1:]:
                    t[i][j] = wordr

        
        for i in range(len(t)):
            for j in range(len(t[i])):
                print(t[i][j], end = ' ')
            print()
        print('\n\n')

        t = []
        for i in range(len(text)):
            t.append(text[i].split())


    elif choice == '5':
        print()

        word = input('Введите слово, которое хотите удалить : ')
        print()
        for i in range(len(t)):
            for j in range(len(t[i])):
                if t[i][j][1:] != word[1:]:
                    print(t[i][j], end = ' ')
            print()

    elif choice == '6':
        print()

        for i in range(len(t)):
            for j in range(len(t[i])):
                if '0' <= t[i][j][:1] <= '9':
                    num1 = float(t[i][j])
                    num2 = float(t[i][j+2])
                    if t[i][j+1] == '+':
                        t[i][j] = str(num1 + num2)
                        t[i][j+1] = ''
                        t[i][j+2] = ''
                        
                    if t[i][j+1] == '-':
                        t[i][j] = str(num1 - num2)
                        t[i][j+1] = ''
                        t[i][j+2] = ''

        for i in range(len(t)):
            for j in range(len(t[i])):
                print(t[i][j], end = ' ')
            print()
        print('\n\n')

        t = []
        for i in range(len(text)):
            t.append(text[i].split())



                                
    elif choice == '9':
        print('''\n
            Список задач.
1) В 6 пункте через цикл сделать больше слагаемых
2) Убрать лишние элементы, получаемые в 6 пункте
3) В 5 пункте удалять из массива (наверно)
4) Индивид задание
\n\n''')




        

    elif choice == '8':
        print()
        for i in text:
            print(i)

        print()

        for i in t:
            print(i)

        











            
        
