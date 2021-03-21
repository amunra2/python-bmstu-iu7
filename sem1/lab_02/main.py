# Название программы : Подсчёты в треугольнике
print('Название программы : Подсчёты в треугольнике')
print()

# Назначение программы : Произвести необходимые подсчеты в треугольнике
print('Назначение программы : Произвести необходимые подсчёты в треугольнике')
print()

# ax, ay, bx, by, cx, cy, dx, dy - координаты точек
# a, b, c - длины сторон тругольника 
# h - длина высоты, проведенной из наименьшего угла
# l - расстояние от 4 точки до наиболее удаленной стороны или её продолжения
# d, e, f - необходимые значения для формулы принадлежности точки треугольнику
# p - полупериметр
# da, db, dc - расстояния от точки d до сторон тругольника
# maxdist - расстояние до наиболее удалённой стороны треугольника
# minside - наименьшая сторона треугольника
# s - площадь получившегомся треугольника

# Тестовый пример :

# Введите координату X точки A : 0
# Введите координату Y точки A : 0
# Введите координату X точки B : 0
# Введите координату Y точки B : 4
# Введите координату X точки C : 3
# Введите координату Y точки C : 0

# Длина стороны 1 :   4
# Длина стороны 2 :   5
# Длина стороны 3 :   3

# Длина высоты из наименьшего угла :  4

# Треугольник не равносторонний.

# Введите координату X дополнительной точки D : 2
# Введите координату Y дополнительной точки D : 1

# Точка принадлежит треугольнику.

# Расстояние от точки D до наиболее удалённой стороны :   2



from math import sqrt
# Считываем координаты 3 точек :
ax = int(input('Введите координату X точки A : '))
ay = int(input('Введите координату Y точки A : '))
bx = int(input('Введите координату X точки B : '))
by = int(input('Введите координату Y точки B : '))
cx = int(input('Введите координату X точки C : '))
cy = int(input('Введите координату Y точки C : '))
print()
# Вычисляем длины сторон треугольника :
a = sqrt((bx - ax)**2 + (by - ay)**2)
b = sqrt((cx - bx)**2 + (cy - by)**2)
c = sqrt((cx - ax)**2 + (cy - ay)**2)
# Для начала найдем полупериметр треугольника :
p = (a + b + c)/2
# Вычислим площадь получившегося треугольника :
s = sqrt(p*(p - a)*(p - b)*(p - c))
# Если площадь равна нулю, то треугольник не получился :
if s == 0:
    print('Такого треугольника не существует.')
else:
    # Выводим длины сторон треугольника :
    print('Длина стороны 1 : ','{: 4.4f}'.format(a))
    print('Длина стороны 2 : ','{: 4.4f}'.format(b))
    print('Длина стороны 3 : ','{: 4.4f}'.format(c))
    print()
    # Против наименьшей стороны лежит наименьший угол :
    minside = min(a, b, c)
    # Находим высоту из наименьшего угла :
    h = (2/minside)*sqrt(p*(p - a)*(p - b)*(p - c))
    print('Длина высоты из наименьшего угла :','{: 4.4f}'.format(h))
    print()
    # Проверяем : треугольник равносторонний или нет :
    if a == b and b == c and a == c:
        print('Треугольник равносторонний.')
    else:
        print('Треугольник не равносторонний.')
    print()
    # Введём координаты точки для проверки ее принадлежности тругольнику :
    dx = int(input('Введите координату X дополнительной точки D : '))
    dy = int(input('Введите координату Y дополнительной точки D : '))
    print()
    # С помощью формулы вычислим значения d, e, f :
    d = (ax - dx)*(by - ay) - (bx - ax)*(ay - dy)
    f = (bx - dx)*(cy - by) - (cx - bx)*(by - dy)
    e = (cx - dx)*(ay - cy) - (ax - cx)*(cy - dy)
    # Если все три значения одинаковы по знаку или равны нулю, то точка \
    # принадлежит треугольнику :
    if (d >= 0 and e >= 0 and f >= 0) or (d < 0 and e < 0 and f < 0) :
        print('Точка принадлежит треугольнику.')
        print()
        # Найдём расстояние от точки D до каждой стороны треугольника :
        da = (abs((by - ay)*dx - (bx - ax)*dy + bx*ay - by*ax)) \
          /(sqrt((bx - ax)**2 + (by - ay)**2))
        db = (abs((cy - by)*dx - (cx - bx)*dy + cx*by - cy*bx)) \
          /(sqrt((cx - bx)**2 + (cy - by)**2))
        dc = (abs((ay - cy)*dx - (ax - cx)*dy + ax*cy - ay*cx)) \
          /(sqrt((cx - ax)**2 + (cy - ay)**2))
        # Найдем наибольшее расстояние и выведем его : 
        maxdist = max(da, db, dc)
        print('Расстояние от точки D до наиболее удалённой стороны : ', '{: .4f}'.format(maxdist))
    else:
        print('Точка не принадлежит треугольнику.')
    
        
        







































    
    

