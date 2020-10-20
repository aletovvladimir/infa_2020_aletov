import turtle as tr
import math as mt

tr.penup()
tr.goto(-250,0)
tr.pendown()
def number(s : str):
    
    ang1 = 45
    ang2 = -135
    ang3 = -90
    ang4 = -180
    fd1 = mt.sqrt(2) * 50
    fd2 = 100
    fd3 = 50
    n = []

    numbers = ([0, fd3, ang3, fd2, ang3, fd3, ang3, fd2,
                ang3, fd3, ang3, fd2, 0, 0, 0, 0, 0, 0],
               [ang1, fd1, ang2, fd2,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, fd3, ang3, fd3, -ang1, fd1,
                -ang2, fd3, 0, 0, 0, 0, 0, 0, 0, ang3, 0, 0],
               [0, fd3, ang2, fd1, -ang2, fd3, ang2, fd1, 0, 0, 0, 0,
                0, 0, 0, -ang2, fd3, ang3],
               [ang3, fd3, -ang3, fd3, -ang3, fd3, ang4, fd2, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0],
               [0, fd3, ang4, fd3, -ang3, fd3, -ang3, fd3, ang3, fd3,
                ang3, fd3, 0, 0, 0, ang4, fd3, ang3],
               [ang2, fd1, ang1, fd3, -ang3, fd3, -ang3, fd3,
                -ang3, fd3, -ang3, fd3, -ang3, fd3, 0, ang3, 0, 0],
               [0, fd3, ang2, fd1, ang1, fd3, 0, 0, 0, 0, 0, 0, 0, 0,
                0, -ang3, fd3, ang3],
               [ang3, fd2, -ang3, fd3, -ang3, fd3, -ang3, fd3, ang3, fd3,
                ang3, fd3 ,ang3, fd2, 0, 0, 0, 0],
               [0, fd3, ang3, fd3, ang3, fd3, ang3, fd3, ang3, fd3,
                ang3, fd3, -ang1, fd1, 0, -ang2, fd3, ang3])
    for i in range(len(s)):
        n.append(int(s[i]))
        print(n)
    
    for i in range(len(s)):
        j = 0
        k = n[i]
        if n[i] == 1:
            tr.penup()
            tr.left(ang3)
            tr.forward(fd3)
            tr.right(ang3)
            tr.pendown()
        elif n[i] == 6:
            tr.penup()
            tr.forward(fd3)
            tr.pendown()
        while j < 13:
            tr.left(numbers[k][j])
            j += 1
            tr.forward(numbers[k][j])
            j += 1
        tr.penup()
        while j < 18:
            tr.forward(numbers[n[i]][j])
            j += 1
            tr.left(numbers[n[i]][j])
            j += 1   
        tr.back(100)
        tr.left(90)
        tr.fd(25)
        tr.pendown()

s = input()
number(s)

    



