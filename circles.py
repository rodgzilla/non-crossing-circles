import math
import random
import sys
import pygame
from pygame import gfxdraw
from pygame import Color

pygame.init()
window_width = 1200
window_height = 900
bg_color = Color(0, 0, 0, 255)
fg_color = Color(0, 0, 255, 255)
circle_number = 2500

def find_radius(circ_list, x, y):
    min_tangent_radius = min([x, window_width - x, y, window_height - y])

    for c_x, c_y, c_r in circ_list:
        dist_centers = int(round(math.sqrt((c_x - x) ** 2 + (c_y - y) ** 2)))
        current_min_tangent_radius = dist_centers - c_r if dist_centers > c_r else c_r - dist_centers
        if current_min_tangent_radius < min_tangent_radius:
            min_tangent_radius = current_min_tangent_radius

    return min_tangent_radius

def gen_image(window, circ_number):
    circ_list = []

    for i in range(circ_number):
        random_x = random.randint(0, window_width - 1)
        random_y = random.randint(0, window_height - 1)

        radius = find_radius(circ_list, random_x, random_y)
        circ_list.append((random_x, random_y, radius))
        center_color = window.get_at((random_x, random_y))
        gfxdraw.filled_circle(window, random_x, random_y, radius, fg_color if center_color == bg_color else bg_color)

if __name__ == '__main__':
    window = pygame.display.set_mode((window_width, window_height))
    pygame.draw.rect(window, bg_color, (0, 0, window_width, window_height))
    gen_image(window, circle_number)
    pygame.display.flip()
    pygame.image.save(window, 'render.bmp')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

