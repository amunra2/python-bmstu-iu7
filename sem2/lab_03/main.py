from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
from time import perf_counter
from random import randint



def insert_with_barier(a, n):
	for i in range(1, n):
		if a[i - 1] > a[i]:
			a[0] = a[i]
			j = i - 1
			while a[j] > a[0]:
				a[j + 1] = a[j]
				j -= 1
			a[j + 1] = a[0]


def create_array(n):
	a = [0]
	for i in range(n):
		a.append(randint(1, 100))
	return a

def warning():
    messagebox.showwarning("Ошибка ввода", "Массив от 2 до 10 чисел")


def test_sort():
	arr_str = entry_mas.get()
	print('\n')
	print(arr_str)
	entry_mas.delete(0, END)
	arr = []
	temp = ''
	mis = 0

	for i in range(len(arr_str)):
		if arr_str[i] == ' ':
			arr.append(int(temp))
			temp = ''
		temp += arr_str[i]
	arr.append(int(temp))
	if len(arr) < 2 or len(arr) > 10:
		warning()
	else:
		arr = [0] + arr
		n = len(arr)
		insert_with_barier(arr, n)

		arr_str = ''
		for i in range(1, len(arr)):
			arr_str += str(arr[i])
			arr_str += ' '

		entry_mas.insert(0, arr_str)
		entry_mas.delete(len(arr_str) - 1)

def table():
	n = [0, 0, 0]
	n[0] = int(n1_entry.get())
	n[1] = int(n2_entry.get())
	n[2] = int(n3_entry.get())

	print(n)
	table = Tk()
	table['bg'] = "orange"
	table.geometry("570x550")
	table.title("Время сортировки")

	text = Label(table, text = '', font=('Arial Bold', 14), anchor=CENTER, width = 11, height = 3)
	text.place(x = 10, y = 10)

	text = Label(table, text = '''Упорядоченный
массив''', font=('Arial Bold', 12), anchor=CENTER, width = 13, height = 4)
	text.place(x = 10, y = 100)

	text = Label(table, text = '''Случайный
массив''', font=('Arial Bold', 12), anchor=CENTER, width = 13, height = 4)
	text.place(x = 10, y = 190)

	text = Label(table, text = '''Обратный 
массив''', font=('Arial Bold', 12), anchor=CENTER, width = 13, height = 4)
	text.place(x = 10, y = 280)

	x_axis = 150

	for i in n:
		text = Label(table, text = i, font=('Arial Bold', 14), anchor=CENTER, width = 11, height = 3)
		text.place(x = x_axis, y = 10)

		a = []
		for i in range(i):
			a.append(i)

		a = [0] + a
		i = len(a)

		start = perf_counter()
		insert_with_barier(a, i)
		end = perf_counter()
		time = end - start

		text = Label(table, text = '{: .7f}'.format(time), font=('Arial Bold', 14), anchor=CENTER, width = 11, height = 3)
		text.place(x = x_axis, y = 100)

		arr = create_array(i - 1)
		start = perf_counter()
		insert_with_barier(arr, i)
		end = perf_counter()
		time = end - start

		text = Label(table, text = '{: .7f}'.format(time), font=('Arial Bold', 14), anchor=CENTER, width = 11, height = 3)
		text.place(x = x_axis, y = 190)


		a.pop(0)
		a.reverse()
		a = [0] + a

		start = perf_counter()
		insert_with_barier(a, i)
		end = perf_counter()
		time = end - start

		text = Label(table, text = '{: .7f}'.format(time), font=('Arial Bold', 14), anchor=CENTER, width = 11, height = 3)
		text.place(x = x_axis, y = 280)

		x_axis += 140
	table.mainloop()


def graph():

	a = int(left_side_entry.get())
	b = int(right_side_entry.get())

	axis_time = []
	axis_ammount = []

	for i in range(a, b, 50):
		a = create_array(i)

		axis_ammount.append(i)

		start = perf_counter()
		insert_with_barier(a, i)
		end = perf_counter()
		time = end - start

		axis_time.append(time)

	plt.title("Сортировка вставками с барьером")
	plt.xlabel("Количество элементов, шт")
	plt.ylabel("Время сортировки, с")

	plt.plot(axis_ammount, axis_time, 'r')

	plt.show()


# Main

sorting = Tk()
sorting['bg'] = 'orange'
sorting.geometry("500x520")
sorting.title("Insertion sort with the barrier")

text_0 = Label(text = '', bg = 'orange')
text_0.grid(column = 1, row = 1)

text_1 = Label(text = '''Пример сортировки вставками с барьером на массиве
 до 10 элементов''', font=('Arial Bold', 14), anchor=CENTER)
text_1.grid(column = 2, row = 2)

text_0 = Label(text = '', bg = 'orange')
text_0.grid(column = 1, row = 3)
entry_mas = Entry(sorting, width = 25, font=('Arial Bold', 18), bg = 'white', fg = 'blue')
entry_mas.grid(column = 1, row = 4, columnspan = 7)

btn_1 = Button(text = ' Отсортировать ', width = 12, font=('Arial Bold', 16),
               command = test_sort)
btn_1.grid(column = 2, row = 5)

text_0 = Label(text = '', bg = 'orange')
text_0.grid(column = 1, row = 6)

text_2 = Label(text = 'Сортировка по времени', font=('Arial Bold', 14), anchor=CENTER)
text_2.grid(column = 1, row = 7, columnspan = 7)

n1_text = Label(text = 'N1 = ', font=('Arial Bold', 14), anchor=CENTER)
n1_text.place(x = 0, y = 220)
n1_entry = Entry(sorting, width = 10, font=('Arial Bold', 14), bg = 'white', fg = 'blue')
n1_entry.place(x = 50, y = 220)

n2_text = Label(text = 'N2 = ', font=('Arial Bold', 14), anchor=CENTER)
n2_text.place(x = 0, y = 250)
n2_entry = Entry(sorting, width = 10, font=('Arial Bold', 14), bg = 'white', fg = 'blue')
n2_entry.place(x = 50, y = 250)

n3_text = Label(text = 'N3 = ', font=('Arial Bold', 14), anchor=CENTER)
n3_text.place(x = 0, y = 280)
n3_entry = Entry(sorting, width = 10, font=('Arial Bold', 14), bg = 'white', fg = 'blue')
n3_entry.place(x = 50, y = 280)

btn_1 = Button(text = ' Отсортировать ', width = 12, font=('Arial Bold', 14),
               command = table)
btn_1.place(x = 250, y = 250)


text_2 = Label(text = '''График зависимости времени сотрировки
массива от его раазмера''', font=('Arial Bold', 14), anchor=CENTER)
text_2.place(x = 50, y = 350)

left_side_text = Label(text = 'Левая граница = ', font=('Arial Bold', 12), anchor=CENTER)
left_side_text.place(x = 0, y = 410)
left_side_entry = Entry(sorting, width = 10, font=('Arial Bold', 14), bg = 'white', fg = 'blue')
left_side_entry.place(x = 150, y = 410)

right_side_text = Label(text = 'Правая граница = ', font=('Arial Bold', 12), anchor=CENTER)
right_side_text.place(x = 0, y = 440)
right_side_entry = Entry(sorting, width = 10, font=('Arial Bold', 14), bg = 'white', fg = 'blue')
right_side_entry.place(x = 150, y = 440)

btn_1 = Button(text = ' Отсортировать ', width = 12, font=('Arial Bold', 12),
               command = graph)
btn_1.place(x = 120, y = 480)


sorting.mainloop()