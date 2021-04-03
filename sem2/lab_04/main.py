from tkinter import *
from tkinter import messagebox
from math import *

point_coords = []
circle_coords = []
circle_rad = []

def click_point(event):
    x = int(event.x)
    y = int(event.y)
    point_coords.append([x, y])
    R = 3
    canvas_win.create_oval(x - R, y - R, x + R, y + R, width=1.5, fill = 'green')


def click_circle(event):
    x = int(event.x)
    y = int(event.y)
    circle_coords.append([x, y])
    R = 50
    circle_rad.append(R)
    canvas_win.create_oval(x - R, y - R, x + R, y + R, width=1.5)


def clear_all():
    point_coords.clear()
    circle_coords.clear()
    circle_rad.clear()
    canvas_win.delete("all")


def build_point():
    try:
        x = int(x_point.get())
        y = int(y_point.get())
        point_coords.append([x, y])
        R = 3
        canvas_win.create_oval(x - R, y - R, x + R, y + R, width=1.5, fill = 'green')
        x_point.delete(0, END)
        y_point.delete(0, END)
        x_point.focus()
    except:
        messagebox.showwarning(message = 'Координаты - целые числа')

def build_circle():
    try:
        x = int(x_circle.get())
        y = int(y_circle.get())
        circle_coords.append([x, y])
        R = int(r_circle.get())
        circle_rad.append(R)
        canvas_win.create_oval(x - R, y - R, x + R, y + R, width=1.5)
        x_circle.delete(0, END)
        y_circle.delete(0, END)
        r_circle.delete(0, END)
        x_circle.focus()
    except:
        messagebox.showwarning(message = 'Координаты и радиус - целые числа')


def build_line():
#    print(point_coords) 
    max_circles = 0

    if len(point_coords) < 2:
        messagebox.showwarning(message = 'Нужно ввести еще минимум ' + str(2 - len(point_coords)) + ' точек')
    elif len(circle_coords) < 1:
        messagebox.showwarning(message = 'Нужно ввести еще минимум 1 окружность')
    for i in range(len(point_coords) - 1):
#       print(point_coords[i], end = ' ')
        x1_line = point_coords[i][0]
        y1_line = point_coords[i][1]
        for j in range(i + 1, len(point_coords)):
#            print(point_coords[j])
            x2_line = point_coords[j][0]
            y2_line = point_coords[j][1]

            circles_touched = touch_circles(x1_line, y1_line, x2_line, y2_line)

            if circles_touched > max_circles:
                max_circles = circles_touched
                rem_x1 = x1_line
                rem_x2 = x2_line
                rem_y1 = y1_line
                rem_y2 = y2_line
#    print('Макс число окружностей ' + str(max_circles))

    if max_circles != 0:
        if rem_x1 != rem_x2:
            y1_l = rem_x1 * (rem_y1 - rem_y2) / (rem_x2 - rem_x1) + rem_y1
            y2_l = (rem_x1 - 900) * (rem_y1 - rem_y2) / (rem_x2 - rem_x1) + rem_y1
            canvas_win.create_line(0, y1_l, 900, y2_l, width = 2, fill = "blue")
        else:
            canvas_win.create_line(rem_x1, 0, rem_x2, 600, width = 2, fill = "blue")


def touch_circles(x1_line, y1_line, x2_line, y2_line):
    circles_touched = 0
    for i in range(len(circle_coords)):
        length = length_between_center_and_line(x1_line, y1_line, x2_line, y2_line, circle_coords[i][0], circle_coords[i][1])

        if length <= circle_rad[i]:
            circles_touched += 1
    return circles_touched


def length_between_center_and_line(x1_line, y1_line, x2_line, y2_line, x_center, y_center):
    length = abs(((x2_line - x1_line) * (y_center - y1_line) \
     - (y2_line - y1_line) * (x_center - x1_line)) / \
    sqrt(pow((x2_line - x1_line), 2) + pow((y2_line - y1_line), 2)))
    return length




win = Tk()
win['bg'] = 'lightgrey'
win.geometry("900x600")
win.title("Touch circles")
win.resizable(False, False)

canvas_win = Canvas(win, width = 600, height = 600, bg = "orange")
canvas_win.place(x = 0, y = 0)

canvas_win.bind('<1>', click_point)
canvas_win.bind('<3>', click_circle)

# Point
point_text = Label(win, text = "Построить точку", font = ("Times New Roman", 16))
point_text.place(x = 650, y = 5)

x_point_text = Label(win, text = "X:", font = ("Times New Roman", 14))
x_point_text.place(x = 615, y = 35)

x_point = Entry(win, font = 14)
x_point.place(x = 640, y = 35, width = 150, height = 25)

y_point_text = Label(win, text = "Y:", font = ("Times New Roman", 14))
y_point_text.place(x = 615, y = 70)

y_point = Entry(win, font = 14)
y_point.place(x = 640, y = 70, width = 150, height = 25)

point_place = Button(text = "Поставить точку", font = ("Times New Roman", 14), command = build_point)
point_place.place(x = 650, y = 110)

#Circle
circle_text = Label(win, text = "Построить окружность", font = ("Times New Roman", 16))
circle_text.place(x = 650, y = 200)

x_circle_text = Label(win, text = "X:", font = ("Times New Roman", 14))
x_circle_text.place(x = 615, y = 235)

x_circle = Entry(win, font = 14)
x_circle.place(x = 640, y = 235, width = 150, height = 25)

y_circle_text = Label(win, text = "Y:", font = ("Times New Roman", 14))
y_circle_text.place(x = 615, y = 270)

y_circle = Entry(win, font = 14)
y_circle.place(x = 640, y = 270, width = 150, height = 25)

r_circle_text = Label(win, text = "R:", font = ("Times New Roman", 14))
r_circle_text.place(x = 615, y = 300)

r_circle = Entry(win, font = 14)
r_circle.place(x = 640, y = 300, width = 150, height = 25)

circle_place = Button(text = "Поставить круг", font = ("Times New Roman", 14), command = build_circle)
circle_place.place(x = 650, y = 340)

# Buttons

text = Label(text = "_" * 30 , font = ("Times New Roman", 14), bg = "lightgrey")
text.place(x = 602, y = 460)

clear_button = Button(text = "Очистить поле", font = ("Times New Roman", 16), command = clear_all)
clear_button.place(x = 670, y = 410)

build_button = Button(text = "Построить прямую", font = ("Times New Roman", 16), bg = "lightblue", command = build_line)
build_button.place(x = 650, y = 500)

win.mainloop()