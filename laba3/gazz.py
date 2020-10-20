from random import randint
import turtle as tr
import math

tr.width(5)
tr.speed(10000)
tr.penup()
tr.goto(-300,-300)
tr.pendown()
tr.goto(-300,300)
tr.goto(300,300)
tr.goto(300,-300)
tr.goto(-300,-300)
tr.speed(10)

ang = []
number_of_turtles = 15
steps_of_time_number = 1000

pool = [tr.Turtle(shape='circle') for i in range(number_of_turtles)]

for unit in pool:
    unit.penup()
    unit.speed(50)
    unit.goto(randint(-280, 280), randint(-280, 280))
    
for i in range(number_of_turtles) :
    ang.append(randint(0,360))

j = 0    
for unit in pool:
    unit.left(ang[j])
    j += 1
    
for i in range(steps_of_time_number):
    k = 0 
    for unit in pool:
        unit.forward(2)
        if ((unit.xcor() <= -290)or(unit.xcor() >= 290)or
            (unit.ycor() <= -290)or(unit.ycor() >= 290)):
            unit.left(180 - 2 * ang[k])
        elif (unit.xcor() == unit.ycor())and((unit.xcor() == 290 )or
                                              (unit.xcor() == -290)):
            unit.left(45)
        k += 1
            
