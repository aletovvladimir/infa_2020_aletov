from random import randrange as rnd, choice
import tkinter as tk
import math
import time

screen_height = 900
x_size = 1440
SIZE = (x_size, screen_height)
root = tk.Tk()
fr = tk.Frame(root)
root.geometry(str(SIZE[0])+'x'+str(SIZE[1]))
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)

bullet_radius = 10
bullet_live_time = 100
bullets = []
gun_x = 20
gun_y = 450
start_x_bullet = gun_x
start_y_bullet = gun_y

class Bullet():
    def __init__(self, x = start_x_bullet, y = start_y_bullet):
        """ Конструктор класса снарядов
        x, у - начальные координаты снаряда
        vx - состовляющая скорости, направленная вдоль Ох
        vy - состовляющая скорости, направленная вдоль Оу
        live_time - продлжительность жизни снаряда
        surface - поверхность, на которой рисуется снаряд
        """
        self.x = x
        self.y = y
        self.r = bullet_radius
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.surface = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill = self.color
        )
        self.live_time = bullet_live_time

    def set_coords(self):
        """ Установка положения полотна, на котором рисуется снаряд """
        canv.coords(
                self.surface,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

    def remove_bullet (self):
        canv.delete(self.surface)
        bullets.pop (bullets.index(self))

    def move(self):
        """
            Переместить мяч по прошествии единицы времени.
            Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
            self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
            и стен по краям окна (размер окна 800х600).
            Метод учитывает тот факт, что снаряд жив или нет, а также гравитацию
        """

        if self.live_time <= 0:
            bullets.pop (bullets.index(self))
            canv.delete(self.surface)
        else:
            if self.y >= screen_height - self.r or self.y <= self.r:
                self.vy = -self.vy
            if self.x >= x_size - self.r:
                self.vx = -self.vx
                
            self.x += self.vx
            self.y -= self.vy

            self.vy -= 1
            self.live_time -= 1

            self.set_coords()

    def hittest(self, obj):
        """
            Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
            Args:
                obj: Обьект, с которым проверяется столкновение.
            Returns:
                Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        dist_object_bullet = ((obj.x - self.x) ** 2 + (obj.y - self.y)**2) ** 0.5
        if dist_object_bullet <= self.r + obj.r:
            return True
        else:
            return False


class Gun():
    def __init__(self, force = 10, readiness = 0, an = 1):
        """
            Конструктор класса пушки
            force - сила выстрела (= полная скорость снаряда)
            readiness - готовность пушки к стрельбе (1 - готова, 0 - нет)
            an - угол между осью пушки и землёй
            surface - поверхность, на которой рисуется пушка
        """
        self.force = force
        self.readiness = readiness
        self.an = an
        self.surface = canv.create_line(20, 450, 50, 420, width = 7)

    def fire2_start(self, event):
        self.readiness = 1

    def fire2_end(self, event):
        """
            Выстрел снарядом.
            Происходит при отпускании кнопки мыши.
            Начальные значения компонент скорости мяча vx и vy зависят от положения курсора.
            quan_bullets - количество использованых снарядов
        """
        global bullets, quan_bullets
        new_bullet = Bullet()
        quan_bullets += 1
        new_bullet.r += 5

        if event.x - new_bullet.x == 0:
            self.an = 90
        else:
            self.an = math.atan((event.y - new_bullet.y) / (event.x - new_bullet.x))
        new_bullet.vx = self.force * math.cos(self.an)
        new_bullet.vy = - self.force * math.sin(self.an)
        bullets += [new_bullet]
        self.readiness = 0
        self.force = 10

    def targetting(self, event = 0):
        """
            Прицеливание. Зависит от положения курсора
            Поворачивает пушку
        """
        if event:
            if event.x - gun_x == 0:
                self.an = 90
            else:
                self.an = math.atan((event.y - gun_y) / (event.x-gun_x))
        canv.coords(self.surface, gun_x, gun_y,
                    gun_x + max(self.force, 20) * math.cos(self.an),
                    gun_y + max(self.force, 20) * math.sin(self.an)
                    )

    def force_up(self):
        """
            Увеличение силы выстрела
        """
        if self.readiness:
            if self.force < 100:
                self.force += 1
            canv.itemconfig(self.surface, fill='orange')
        else:
            canv.itemconfig(self.surface, fill='black')


class Target():

    def __init__(self, alive = 1):

        """
            Конструктор класса целей
            points - количество поражённых целей
            points_surface - поверхность, на которой рисуются очки
            alive - факт жизни цели (1 - цель жива, 0 - нет)
        """
        self.alive = 1
        self.surface = canv.create_oval(0,0,0,0)
        self.new_target()

    def new_target(self):
        """ Инициализация новой мишени """
        x = self.x = rnd(400, 780)
        y = self.y = rnd(100, 550)
        r = self.r = rnd(20, 50)
        vx = self.vx = rnd(5,10)
        vy = self.vy = rnd(5,10)
        color = self.color = 'red'
        canv.coords(self.surface, x - r, y - r, x + r, y + r)
        canv.itemconfig(self.surface, fill = color)

    def set_coords(self):
        """ Установка положения полотна, на котором рисуется мишень """
        canv.coords(
                self.surface,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )


    def hit(self, points=1):
        """Попадание шарика в цель"""
        canv.coords(self.surface, -10, -10, -10, -10)

    
    def move(self):
        """
            Переместить мишень по прошествии единицы времени.
            Метод описывает перемещение мишени за один кадр перерисовки. То есть, обновляет значения
            self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
            и стен по краям окна (размер окна 800х600).
        """

        if self.alive:
            if self.y >= screen_height - self.r or self.y <= self.r:
                self.vy = -self.vy
            if self.x >= x_size - self.r or self.x <= self.r:
                self.vx = -self.vx
                
            self.x += self.vx
            self.y -= self.vy

            self.vy -= 1

            self.set_coords()

target1 = Target()
target2 = Target()
target3 = Target()
gun = Gun()
bullets = []
points = 0
quan_bullets = 0
some_target_hit = False
canv.create_text(32, 30, text = 'points:' + str(points), font = '28')
canv.create_text(32, 60, text = 'quan_bullets:' + str(quan_bullets), font = '28')

def new_game(event=''):
    global gun, target1, target2, screen1, bullets, quan_bullets, points
    target1.new_target()
    target2.new_target()
    bullets = []
    canv.bind('<Button-1>', gun.fire2_start)
    canv.bind('<ButtonRelease-1>', gun.fire2_end)
    canv.bind('<Motion>', gun.targetting)


    z = 0.03
    target1.alive = 1
    target2.alive = 1
    target3.alive = 1
    while target1.alive or target2.alive or target3.alive:
        for b in bullets:
            b.move()
            if b.hittest(target1) and target1.alive:
                some_target_hit = True
                target1.alive = 0
                target1.hit()
                points += 1
                canv.create_rectangle(0, 0, 100, 100,
                                      outline = 'white', fill = 'white')
                canv.create_text(30, 30, text = 'points:' + str(points), font = '28')
            if b.hittest(target2) and target2.alive:
                some_target_hit = True
                target2.alive = 0
                target2.hit()
                points += 1
                canv.create_rectangle(0, 0, 100, 100,
                                      outline = 'white', fill = 'white')
                canv.create_text(30, 30, text = 'points:' + str(points), font = '28')
            if b.hittest(target3) and target3.alive:
                some_target_hit = True
                target3.alive = 0
                target3.hit()
                points += 1
                canv.create_rectangle(0, 0, 100, 100,
                                      outline = 'white', fill = 'white')
                canv.create_text(30, 30, text = 'points:' + str(points), font = '28')

                
            if some_target_hit:
                for b in bullets:
                    b.remove_bullet()
                
        canv.create_rectangle(0, 0, 100, 100,
                                      outline = 'white', fill = 'white')
        canv.create_text(40, 60, text = 'quan_bullets:' + str(quan_bullets), font = '28')
        canv.create_text(32, 30, text = 'points:' + str(points), font = '28')

        some_target_hit = False
        
        if target1.alive:
            target1.move()
        if target2.alive:
            target2.move()
        if target3.alive:
            target3.move()
            
        canv.update()
        time.sleep(z)
        gun.targetting()
        gun.force_up()
    canv.delete(gun)
    root.after(750, new_game)


new_game()

