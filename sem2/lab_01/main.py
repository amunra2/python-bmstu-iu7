
'''
a, b - границы отрезка
h - шаг
eps - точность для нахождения корня
maxiter - макимальное количество итераций
time1, time 2 - итоговое время на каждый из методов
mistake - значение ошиибки

'''



from tkinter import *
import matplotlib.pyplot as plt
import tkinter.ttk as ttk

import scipy.optimize as scp
from time import perf_counter
from math import sin, fabs, cos


max_iter = 100

# solved with help eval()

# Function
def f(x):
    fun = eval(entry_func.get())
    return(fun)

# f'(X)
def f1(x):
    fun1 = eval(entry_derivative.get())
    return(fun1)

def graphic():

    # Create graph
    a = int(entry1.get())
    b = int(entry2.get())

    eps_graph = 0.001
    step_graph = 0.001
    n = a
    x_graph = []
    y_graph = []

    x_root = []
    y_root = []

    x_points = []
    y_points = []

    x_min = []
    y_min = []

    x_max = []
    y_max = []

    f_min = f(a)
    f_max = f(a)


    while n <= b:
        if abs(f(n)) <= eps_graph:
            if f(n - step_graph)*f(n + step_graph) < 0:
                x_root.append(n)
                y_root.append(f(n))
            else:
                x_points.append(n)
                y_points.append(f(n))

        elif abs(f1(n)) <= eps_graph:
            x_points.append(n)
            y_points.append(f(n))

        else:
            x_graph.append(n)
            y_graph.append(f(n))
                           
        n += step_graph

    n = a


    for i in range(len(y_points)):
        if round(y_points[i], 3) < round(f_min, 3):
            f_min = y_points[i]

            x_min = []
            y_min = []
            x_min.append(x_points[i])
            y_min.append(y_points[i])
            
        elif round(y_points[i], 3) == round(f_min, 3):
            x_min.append(x_points[i])
            y_min.append(y_points[i])


        elif round(y_points[i], 3) > round(f_max, 3):
            f_max = y_points[i]

            x_max = []
            y_max = []
            x_max.append(x_points[i])
            y_max.append(y_points[i])
            
        elif round(y_points[i], 3) == round(f_max, 3):
            x_max.append(x_points[i])
            y_max.append(y_points[i])


    plt.title('Graph $f(x)=sin(x)$', fontsize = 20)
    plt.plot(x_graph, y_graph, 'c')
    plt.plot(x_root, y_root, 'rp')
    plt.plot(x_min, y_min, 'yp')
    plt.plot(x_max, y_max, 'bp')
    plt.plot([a-1,b+1],[0,0],color = 'g')    


    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend(("Graph", "Roots", "Min", "Max", "Axis"), loc='upper right')
    plt.grid()
    plt.show()





def tablee():
    # Create table
    root = Tk()
    root.title('Таблица значений.')
    table = ttk.Treeview(root, height = 30)
    
    table.tag_configure('ttk', background='light gray')

    table['columns'] = ( 'one', 'two', 'three', 'four', 'five',
                        'six', 'seven', 'eight')
    table.column('#0', width=70, minwidth=70, stretch=NO)
    table.column('one', width=85, minwidth=90, stretch=NO)
    table.column('two', width=70, minwidth=50, stretch=NO)
    table.column('three', width=70, minwidth=50, stretch=NO)
    table.column('four', width=120, minwidth=120, stretch=NO)
    table.column('five', width=100, minwidth=100, stretch=NO)
    table.column('six', width=80, minwidth=80, stretch=NO)
    table.column('seven', width=100, minwidth=100, stretch=NO)
    table.column('eight', width=80, minwidth=80, stretch=NO)

    table.heading('#0', text='№ корня', anchor=CENTER)
    table.heading('one', text='Метод', anchor=CENTER)
    table.heading('two', text='A', anchor=CENTER)
    table.heading('three', text='B', anchor=CENTER)
    table.heading('four', text='Значение x', anchor=CENTER)
    table.heading('five', text='f(x)', anchor=CENTER)
    table.heading('six', text='Итераций', anchor=CENTER)
    table.heading('seven', text='Время работы', anchor=CENTER)
    table.heading('eight', text='Код ошибки', anchor=CENTER)



    a = int(entry1.get())
    b = int(entry2.get())
    h = float(entry3.get())
    eps = float(entry4.get())
    max_iter = 100
    
    a1 = a
    a2 = a + h
    rnum = 0

    root_set1 = set()
    time1= 0

    root_set2 = set()
    time2 = 0

    # Filling of a table
    while a2 < b + h/2:
        if f(a1)*f(a2) <= 0:
            rnum += 1
            
            begin1 = perf_counter()
            x11, res = scp.brenth(f, a1, a2, xtol=eps, maxiter=max_iter,
                                     full_output=True, disp = False)
            
            time1 = '{:^3.1e}'.format(perf_counter() - begin1)
            if x11 not in root_set1:
            
                if res.converged:
                    mistake1 = 0
                else:
                    mistake1 = 1
                iters1 = res.iterations    
                if f(a1) == 0 or f(a2) == 0:
                    iters1 = 0
                if iters1 > max_iter:
                    mistake1 = 1

                fx11 = '{:^20.1e}'.format(f(x11))
                
                
                values1 = []
                values1 = ['brenth.Scipy', '{:^20.2f}'.format(a1), '{:^20.2f}'.format(a2), '{:^25.7g}'.format(x11),
                           fx11, iters1, time1, mistake1]
                table.insert('', 'end', tags=('ttk'),
                             text = rnum, values = values1)
                           

                root_set1.add(x11)
            else:
                rnum -= 1
            
            begin2 = perf_counter()
            x12, iters2, mistake2 = brenth_Python(f, a1, a2, eps, max_iter)
            time2 = '{:^3.1e}'.format(perf_counter() - begin2)
            
            if x11 not in root_set2:
                values2 = []
                values2 = ['brenth.Python', '{:^20.2f}'.format(a1), '{:^20.2f}'.format(a2), '{:^25.7g}'.format(x12),
                            '{:^20.1e}'.format(f(x12)), iters2, time2, mistake2]
                table.insert('', 'end', tags=('ttk'), values = values2)

                root_set2.add(x12)
            v = []
            table.insert('', 'end', values = v)
        a1 = a2
        a2 += h
    if rnum != 0:
        table.pack()

    else:
        textt = Label(root, text = 'Корней нет', font=('Arial Bold', 30),
                      fg = 'green')
        textt.grid(column = 3, row =3)
        root.geometry('400x400')
    root.mainloop()
        

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



if __name__ == "__main__":

    Input = Tk()
    #Input['bg'] = 'cyan'
    Input.geometry('700x400')

    text0 = Label(text = 'Уточнение корней', font=('Arial Bold', 18),
                fg = 'green', anchor=CENTER)
    text0.grid(column = 3, row = 2)

    # left point
    text1 = Label(text = '    Введите левую границу  : ',
                font=('Arial Bold', 14), fg = 'green')
    text1.grid(column = 2, row = 3)

    entry1 = Entry(Input, width = 30, font=('Arial Bold', 12), bg = 'white')
    entry1.grid(column = 3, row = 3)
    entry1.focus()

    # right point
    text2 = Label(text = '    Введите правую границу  : ',
                font=('Arial Bold', 14), fg = 'green')
    text2.grid(column = 2, row = 5)

    entry2 = Entry(Input, width = 30, font=('Arial Bold', 12), bg = 'white')
    entry2.grid(column = 3, row = 5)

    # step
    text3 = Label(text = '  Введите шаг: ', font=('Arial Bold', 14), fg = 'green')
    text3.grid(column = 2, row = 6)

    entry3 = Entry(Input, width = 30, font=('Arial Bold', 12), bg = 'white')
    entry3.grid(column = 3, row = 6)

    # eps
    text4 = Label(text = '  Введите eps : ', font=('Arial Bold', 14), fg = 'green')
    text4.grid(column = 2, row = 7)

    entry4 = Entry(Input, width = 30, font=('Arial Bold', 12), bg = 'white')
    entry4.insert(1, '1e-3')
    entry4.grid(column = 3, row = 7)

    # input function
    text_func = Label(text = '  Введите функцию : ', font=('Arial Bold', 14), fg = 'green')
    text_func.grid(column = 2, row = 8)
    entry_func = Entry(Input, width = 30, font=('Arial Bold', 12), bg = 'white')
    entry_func.insert(1, 'sin(x)')
    entry_func.grid(column = 3, row = 8)


    # input derivative (производная)
    text_derivative = Label(text = '  Введите производную : ', font=('Arial Bold', 14), fg = 'green')
    text_derivative.grid(column = 2, row = 9)
    entry_derivative = Entry(Input, width = 30, font=('Arial Bold', 12), bg = 'white')
    entry_derivative.insert(1, 'cos(x)')
    entry_derivative.grid(column = 3, row = 9)

    # graph
    graph = Button(text = 'Создать график.', font=('Arial Bold', 12),
                command = graphic)
    graph.grid(column = 3, row = 15)

    # table
    tabl = Button(text = 'Создать таблицу.', font=('Arial Bold', 12),
                command = tablee)
    tabl.grid(column = 3, row = 16)

    ext = Button(text = 'Выйти', font=('Arial Bold', 12), command = exit)
    ext.grid(column = 3, row = 17)
    msg1 = Label(text='\nВиды ошибок:' + ' ' * 18 + '\n0. Нет ошибок'
                + ' ' * 23 + '\n 1. Число итераций превышает максимальное\n',
                font=('Arial Bold', 12), fg = 'green')
    msg1.grid(column=2, row=19, columnspan=3)
    Input.mainloop()


















            
        



        
    
    
