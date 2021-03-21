print('Лабораторная работа №12')
print()
print('Название программы : Текст')
print('Назначение программы : Работа с текстом')
print()
print()
print()


text = [' Приветствую каждого читателя. Сегодня я с радостью ',
        '    расскажу Вам прекрасный рецепт лабораторной ',
        '   работы по программированию на Питоне! Вам точно понадобится',
        '  придумать алгоритм и записать его на нужном ',
        '     языке программирования. Затем Вам нужно написать',
        'комментарий к каждому сложному моменту программы. Далее ',
        '  следует описать все переменные. И также Вам пригодится ',
        '   тестовый пример. Мы все обожаем Питон!']


t = []
for i in range(len(text)):
    t.append(text[i].split())

choice = None
while choice != '0':
    print('''
    Индивидуальное задание : поменять местами самое короткое слово самой \
    длинной строки и самое длинное слово самой короткой строки

    1) Показать текст
    2) Показать результат
    
    0) Выход
    ''')
    choice = input('Введите пункт меню : ')



    if choice == '1':
        print()
            
        for i in range(len(t)):
            for j in range(len(t[i])):
                print(t[i][j], end = ' ')
            print()
        print('\n\n\n')

    elif choice == '2':
        print()

# Самое длинное предложение и самое короткое предложение
        predl = []
        k = 0
        for i in range(len(t)):
            for j in range(len(t[i])):
                predl.append(t[i][j])

        signs = ['.','!','?']
        temp = 0
        maxw = 0
        minw = 100
        num1 = 0
        num2 = 0
        for i in range(len(predl)):
            temp += 1
            if predl[i][-1:] in signs:
                if maxw < temp:
                    maxw = temp
                    num1 = i
                elif minw > temp:
                    minw = temp
                    num2 = i
                temp = 0
        prmin = []
        prmax = []


        for i in range(num1-maxw+1, num1+1):
            prmax.append(predl[i])

        for i in range(num2-minw+1, num2+1):
            prmin.append(predl[i])

#        print(prmin, '\n', prmax)

        
        
            
# Самое короткое слово самой длинной строки и самое длинное слово самой \
# короткой строки

        mina = 100
        maxa = 0
        for i in range(len(prmin)):
            if len(prmin[i]) > maxa:
                maxa = len(prmin[i])
                slvmax = prmin[i]
#        print(slvmax)


        for i in range(len(prmax)):
            if len(prmax[i]) < mina:
                mina = len(prmax[i])
                slvmin = prmax[i]
#        print(slvmin)

        for i in range(len(t)):
            for j in range(len(t[i])):
                if t[i][j] == slvmax:
                    print(slvmin, end = ' ')
                elif t[i][j] == slvmin:
                    print(slvmax, end = ' ')
                else:
                    print(t[i][j], end = ' ')
            print()
        

        

    
