from tkinter import *
from math import *
from tkinter import messagebox

remember = '' # for retry_old
check = 0 
rem_last = '' # for new retry and for equall - not to forget last step

# cascade - for menu

def insert_1():
	global remember
	length = len(inputt.get())
	inputt.insert(length, 1)

	remember = 'insert_1()'


def insert_0():
	global remember
	length = len(inputt.get())
	inputt.insert(length, 0)

	remember = 'insert_0()'


def insert_point():
	global remember
	length = len(inputt.get())
	inputt.insert(length, '.')

	remember = 'insert_point()'


def c_one():
	global remember
	length = len(inputt.get())
	inputt.delete(length - 1)

	remember = 'c_one()'


def c_all():
	global remember, answer, check
	length = len(inputt.get())
	while length >= 1:
		inputt.delete(length - 1)
		length = len(inputt.get())
	check = 0
	remember = 'c_all()'
	answer = 0

def insert(x):
	inputt.insert(1, x)

def retry():
	global for_retry, rem_last
	if rem_last == 'plu':
		pluss()
		insert(for_retry)
	elif rem_last == 'min':
		minuss()
		insert(for_retry)
	elif rem_last == 'power':
		power()
		insert(for_retry)


def pluss():
	global res, answer, check, rem_last, flag, for_retry
	if check == 0:
		answer = convert_in(inputt.get())
		length = len(inputt.get())
		while length >= 1:
			inputt.delete(length - 1)
			length = len(inputt.get())
		check = 1
	else:
		for_retry = inputt.get()
		res = convert_in(inputt.get())
		# if flag == 1:
		# 	res *= -1
		# 	flag = 0
		length = len(inputt.get())
		while length >= 1:
			inputt.delete(length - 1)
			length = len(inputt.get())

		answer += res

	rem_last = "plu"

	print(answer)



def minuss():
	global res, answer, check, rem_last, flag
	if check == 0:
		answer = convert_in(inputt.get())
		length = len(inputt.get())
		while length >= 1:
			inputt.delete(length - 1)
			length = len(inputt.get())
		check = 1
	else:
		for_retry = inputt.get()
		res = convert_in(inputt.get())
		# if flag == 1:
		# 	res *= -1
		# 	flag = 0
		length = len(inputt.get())
		while length >= 1:
			inputt.delete(length - 1)
			length = len(inputt.get())
		answer -= res

	rem_last = "min"
	print(answer)



def power():
	global answer, rem_last, check, answer_power, last, flag
	if check == 0:
		answer = convert_in(inputt.get())
		length = len(inputt.get())
		while length >= 1:
			inputt.delete(length - 1)
			length = len(inputt.get())
		check = 1
	else:
		for_retry = inputt.get()
		res = inputt.get()
		length = len(inputt.get())
		while length >= 1:
			inputt.delete(length - 1)
			length = len(inputt.get())
		if last == 'equal':
			answer = answer_power
		# if flag == 1:
		# 	answer *= -1
		# 	flag = 0
		answer *= convert_in(res)
	print(answer)

	rem_last = 'power'



def equall():
	global answer, rem_last, answer_power, last, flag
	if rem_last == "plu":
		res = inputt.get()
		answer += convert_in(res)
	elif rem_last == "min":
		res = inputt.get()
		answer -= convert_in(res)
	elif rem_last == 'power':
		res = inputt.get()
		answer *= convert_in(res)

	ready = ''

	
	length = len(inputt.get())
	while length >= 1:
		inputt.delete(length - 1)
		length = len(inputt.get())


	
	ready = convert_out(answer)
	print(ready)
	inputt.insert(1, ready)
	# if answer < 0:
	# 	flag = 1
	answer_power = answer
	last = 'equal'
	answer = 0



def convert_in(res):
	result = 0

	if '-' in res:
		res = res[1:]
	mistake = 0
	try:
		a = float(res)
	except:
		warning()
		mistake = 1

	if mistake == 0:
		mas =['2','3','4','5','6','7','8','9']
		for i in mas:
			if i in str(res):
				warning()
				mistake = 1
				break
	if mistake == 0:
		i = 0
		if '.' not in res:
		    len_num = len(res)
		    
		    while len_num > 0:
		        result += int(res[len_num - 1]) * pow(2, i)
		        i += 1
		        len_num -= 1
		    print('\n', result)
		        
		else:
		    k = 0
		    while res[k] != '.':
		        k += 1
		    q = k + 1    
		    while k > 0:
		        result += int(res[k - 1]) * pow(2, i)
		        i += 1
		        k -= 1

		    i = -1
		    result_p = 0
		    while q < len(res):
		        result_p += int(res[q]) * pow(2, i)
		        i -= 1
		        q += 1
		        
		        
		    result = result + result_p

	return result



def convert_out(x):
	sign = x
	x = abs(x)
	if x == 0:
		return '0'
	resu = ''
	pnt = x
	i = 0

	while x > 0:
		resu = ('0' if x % 2 == 0 else '1') + resu
		x //= 2

	resu += '.'

	x = pnt - int(pnt)

	lon = 6

	while lon > 0:
		resu += str(int(x * 2))
		x = x * 2 - int(x * 2)
		lon -= 1

	if abs((pnt - int(pnt))) < 1e-7:
		i = 0
		while resu[i] != '.':
			i += 1
		resu = resu[:i]

	if sign < 0:
		resu = '-' + resu

	return resu


def info():
    messagebox.showinfo("Информация о программе", "Данная программа выполняет \
сложение, вычитание и умножение действительных чисел в двочиной системе \
счисления.\n\nРазработчик \n Цветков Иван \n Группа : ИУ7-23Б")


def warning():
    messagebox.showwarning("Ошибка ввода", "Вводятся только числа 1 и 0")


# Main
if __name__ == "__main__":
	calc = Tk()
	calc['bg'] = 'pink'
	calc.geometry('780x400')
	calc.title('Calculator')

	text0 = Label(text = '', font=('Arial Bold', 18),
				fg = 'green', bg = 'pink', anchor=CENTER)
	text0.grid(column = 1, row = 1)

	inputt = Entry(calc, width = 25, font=('Arial Bold', 24), bg = 'white', fg = 'blue')
	inputt.grid(column = 1, row = 2, columnspan = 7)
	inputt.focus()


	text0 = Label(text = '', font=('Arial Bold', 18),
				fg = 'green', bg = 'pink', anchor=CENTER)
	text0.grid(column = 1, row = 3)


	# Input
	one = Button(text = ' 1 ', width = 15, font=('Arial Bold', 18),
				command = insert_1)
	one.grid(column = 2, row = 5)

	zero = Button(text = ' 0 ', width = 15, font=('Arial Bold', 18),
				command = insert_0)
	zero.grid(column = 2, row = 4)

	point = Button(text = ' . ', width = 15, font=('Arial Bold', 18),
				command = insert_point)
	point.grid(column = 2, row = 6)


	# Operations
	plus = Button(text = ' + ', width = 15, font=('Arial Bold', 18),
				command = pluss)
	plus.grid(column = 4, row = 4)

	minus =  Button(text = ' - ', width = 15, font=('Arial Bold', 18),
				command = minuss)
	minus.grid(column = 4, row = 5)

	power = Button(text = ' * ', width = 15, font=('Arial Bold', 18),
				command = power)
	power.grid(column = 4, row = 6)

	clear_one = Button(text = ' Стереть последнее ', width = 15, font=('Arial Bold', 18), bg = "orange",
				command = c_one)
	clear_one.grid(column = 6, row = 4)

	clear_all = Button(text = ' Очистить всё ', width = 15, font=('Arial Bold', 18), bg = "orange",
				command = c_all)
	clear_all.grid(column = 6, row = 5)

	repeat = Button(text = ' Повторить ', width = 15, font=('Arial Bold', 18), bg = "orange",
				command = retry)
	repeat.grid(column = 6, row = 6)

	# Result

	equal = Button(text = ' = ', width = 15, font=('Arial Bold', 18), bg = "orange",
				command = equall)
	equal.grid(column = 6, row = 7)

	# Information

	menu = Menu(calc)
	calc.config(menu = menu)
	menu.add_command(label = 'Информация', command = info)

	calc.mainloop()
