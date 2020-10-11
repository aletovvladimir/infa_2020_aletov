import pygame
from pygame.draw import *
from random import randint

FPS = 30
X_SIZE, Y_SIZE = 1000, 800

WHITE_ALPHA = (255, 255, 255, 0)
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

    sizes_of_houses = [
        (X_SIZE // 4, 2 * Y_SIZE // 5),
        (X_SIZE // 6, Y_SIZE // 5)
    ]

    positions_of_houses = [
        (X_SIZE // 15, 3 * Y_SIZE // 7),
        (4 * X_SIZE // 7, 4 * Y_SIZE // 7)
    ]

    positions_of_clouds = [
        (X_SIZE // 5, Y_SIZE // 6),
        (3 * X_SIZE // 5, Y_SIZE // 4),
        (8 * X_SIZE // 9, Y_SIZE // 8),
        (0, 0),
        (X_SIZE // 2, 0)
    ]

    sizes_of_trees = [
        (X_SIZE // 3, Y_SIZE // 2),
        (X_SIZE // 3, Y_SIZE // 2)
    ]

    positions_of_trees = [
        (X_SIZE // 4, Y_SIZE // 3),
        (5 * X_SIZE // 7, 4 * Y_SIZE // 10)
    ]

    draw_background(screen,
                    GREEN, BLUE,
                    sky_height)

    for position in positions_of_clouds:
        cloud = make_cloud(WHITE)
        draw_surface(screen, cloud, position)

    for size, position in zip(sizes_of_houses, positions_of_houses):
        house = make_house(size, BROWN, RED, LIGHT_BLUE)
        draw_surface(screen, house, position)

    for size, position in zip(sizes_of_trees, positions_of_trees):
        tree = make_tree(size, BLACK, DARK_GREEN)
        draw_surface(screen, tree, position)


def make_house(size, color_house, color_roof, color_window):
    """
    Makes a surface of house
    :param size: full width and height of the house
    :param color_house: color of the house
    :param color_roof: color of the house's roof
    :param color_window: color of the house's window
    :return: surface of the house
    """
    width, height = size
    half_width = width // 2
    half_height = height // 2

    x0 = 0
    y0 = half_height

    wind_width = half_width
    wind_height = half_height // 2

    x0_wind = half_width - wind_width // 2
    y0_wind = height - 3 * half_height // 4

    roof_coordinates = [
        (x0, y0),
        (half_width, 0),
        (x0 + width, y0)
    ]

    house = pygame.Surface((width, height), pygame.SRCALPHA)
    house.fill(WHITE_ALPHA)

    rect(house, color_house, (x0, y0, width, half_height))
    polygon(house, color_roof, roof_coordinates)
    rect(house, color_window, (x0_wind, y0_wind, wind_width, wind_height))

    return house


def make_tree(size, color_tree, color_sheet):
    """
    makes a surface of a tree
    :param size: full width and height of the tree
    :param color_tree: color of the trunk
    :param color_sheet: color of the sheets
    :return: surface of a tree
    """
    width, height = size
    half_width = width // 2

    x0 = half_width
    sheet_radius = width // 6
    half_trunk_width = width // 8

    sheet_coordinates = [
        (x0, sheet_radius),
        (half_width - half_trunk_width, 2 * sheet_radius),
        (half_width + half_trunk_width, 3 * sheet_radius),
        (half_width - half_trunk_width, 3 * sheet_radius),
        (half_width + half_trunk_width, 2 * sheet_radius),
        (x0, 4 * sheet_radius)
    ]

    tree = pygame.Surface((width, height), pygame.SRCALPHA)
    tree.fill(WHITE_ALPHA)

    rect(tree, color_tree, (x0 - half_trunk_width, height // 2, 2 * half_trunk_width, height))
    for sheet_x, sheet_y in sheet_coordinates:
        circle(tree, color_sheet, (sheet_x, sheet_y), sheet_radius)

    return tree


def make_cloud(color_cloud):
    """
    makes a surface of a cloud
    :param color_cloud: color of the cloud
    :return: surface of the cloud
    """
    cloud_radius = min(X_SIZE, Y_SIZE) // 15
    width = height = cloud_radius * 5
    quarter_size = height // 4
    num_of_circle_in_cloud = 10

    cloud = pygame.Surface((width, height), pygame.SRCALPHA)
    cloud.fill(WHITE_ALPHA)

    for i in range(num_of_circle_in_cloud):
        x0 = randint(quarter_size, width - quarter_size)
        y0 = randint(quarter_size, height - quarter_size)
        circle(cloud, color_cloud, (x0, y0), cloud_radius)

    return cloud


def draw_background(screen, grass_color, sky_color, sky_height):
    """
    screen - экран отображения
    grass_color - цвет земли
    sky_color - цвет неба
    sky_height - координата начала земли
    """
    rect(screen, grass_color, (0, sky_height, X_SIZE, Y_SIZE))
    rect(screen, sky_color, (0, 0, X_SIZE, sky_height))


def draw_surface(screen, surface, position):
    """
    draws a surface on an active one
    :param screen: active surface
    :param surface: surface to draw
    :param position: position of top left corner of the surface
    :return: none
    """
    screen.blit(surface, position)


main()
