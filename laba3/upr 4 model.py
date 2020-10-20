import turtle as tr
import math as mt

tr.speed(100000)
tr.goto(-500,0)
tr.goto(500,0)

x0 = -450
y0 = 0
dt = 0.1
alpha = 1.5
ang = mt.pi  / 2.3

tr.goto(x0,y0)
tr.speed(1)

V = 50
V0x = V * mt.cos(ang)
V0y = V * mt.sin(ang)
ay = 10

x = x0
y = y0
Vy = V0y

while y >= -10:
    if y < 0:
        V0x /= 1.05
        Vy = V0y / alpha
        y = y0
        alpha *= 1.1
    else:
        tr.goto(x,y)
        x += V0x * dt
        y += Vy * dt
        Vy -= ay * dt
    if x >= 500:
        y = -11

