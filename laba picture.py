import pygame
from pygame.draw import *
from random import randint

FPS = 30
X_SIZE, Y_SIZE = 1000, 800

WHITE = (255, 255, 255)
GRAY = (210, 210, 210)
RED = (220, 20, 20)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200)
LIGHT_BLUE = (0, 0, 120)
BROWN = (200, 120, 200)
DARK_GREEN = (50, 255, 50)


def main():
    pygame.init()

    screen = pygame.display.set_mode((X_SIZE, Y_SIZE))
    screen.fill(GRAY)

    draw_scene(screen)

    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False

    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

    pygame.quit()


def draw_scene(screen):
    sky_height = 2 * Y_SIZE // 3
    house_x_coord, house_y_coord = X_SIZE // 5, 3 * Y_SIZE // 4
    house_width, house_height = X_SIZE // 4, Y_SIZE // 3

    draw_background(screen, GREEN, BLUE, sky_height)
    draw_house(screen,
               house_x_coord, house_y_coord,
               house_width, house_height,
               BROWN, RED, LIGHT_BLUE)
    tree(screen, 550, 750, 50, 150, BLACK, DARK_GREEN)
    clouds(screen, 500, 200, WHITE)


def draw_background(screen, grass_color, sky_color, sky_height):
    '''
    screen - экран отображения
    grass_color - цвет земли
    sky_color - цвет неба
    sky_height - координата начала земли
    '''
    rect(screen, grass_color, (0, sky_height, X_SIZE, Y_SIZE))
    rect(screen, sky_color, (0, 0, X_SIZE, sky_height))


def draw_house(screen,
               x, y,
               width, height,
               color_house, color_roof, color_window):
    '''
    рисует дом
    x, y - координаты середины нижней стороны
    height, width - полная высота и ширина дома
    color_house, color_roof, color_window - цвета дома, крыши и окна соответсвенно
    '''
    half_width = width // 2
    half_height = height // 2

    x0 = x - half_width
    y0 = y - half_height

    wind_width = half_width
    wind_height = half_height // 2

    x0_wind = x - wind_width // 2
    y0_wind = y - half_height // 2

    roof_coordinates = [
        (x0, y0),
        (x, y - height),
        (x0 + width, y0)
    ]

    rect(screen, color_house, (x0, y0, width, height))
    polygon(screen, color_roof, roof_coordinates)
    rect(screen, color_window, (x0_wind, y0_wind, wind_width, wind_height))


def tree(screen,
         x, y,
         width, height,
         color_tree, color_sheet):
    '''
    рисует дерево
    x, y - координаты середины нижней стороны ствола
    width, height - ширина и высота дерева
    color_tree, color_sheet - цвет ствола и листьев соотвественно
    '''
    x0 = x - int(width / 2)
    y0 = y - height
    rect(screen, color_tree, (x0, y0, width, height))
    R = 60
    xall = (x, x - width, x + width, x - width, x + width, x, x)
    yall = (y0 - 3 * R, y0 - 25, y0 - 25, y0 - 2 * R, y0 - 2 * R, y0 - R)
    for k in range(0, 6):
        i = yall[k]
        j = xall[k]
        circle(screen, color_sheet, (j, i), R)


def clouds(screen,
           x, y,
           color_cloud):
    '''
    рисует облака
    x, y - координаты "центра облака"
    color_cloud - цвет облака
    '''
    R = 50
    for i in range(0, 10):
        x0 = randint(x - R, x + R)
        y0 = randint(y - R, y + R)
        circle(screen, color_cloud, (x0, y0), R)


main()
