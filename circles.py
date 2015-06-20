import math
import random
import sys
import pygame
from pygame import gfxdraw
from pygame import Color

pygame.init()
# window size
window_width = 1200
window_height = 900
# background color
bg_color = Color(0, 0, 0, 255)
# foreground color
fg_color = Color(0, 0, 255, 255)
# number of circles
circle_number = 2500

def find_radius(circ_list, x, y):
    """This function returns the maximum radius that a circle centered at
    (x, y) can have while still not crossing another circle.

    """
    # The circles also do not cross the sides of the screen.
    min_tangent_radius = min([x, window_width - x, y, \
                              window_height - y])
    
    # For each circle already drawn:
    for c_x, c_y, c_r in circ_list:
        # Compute the distance between the two centers
        d_cent = int(round(math.sqrt((c_x - x) ** 2 + (c_y - y) ** 2)))
        # Compute the radius that the current circle should have in
        # order to be tangent the circle (c_x, c_y, c_r). We need to
        # check whether (x, y) is in (c_x, c_y, c_r) to do this
        # computation.
        current_min_radius = d_cent - c_r if d_cent > c_r else c_r - d_cent
        if current_min_radius < min_tangent_radius:
            min_tangent_radius = current_min_radius

    return min_tangent_radius

def gen_image(window, circ_number):
    """This function generates the final image.

    """
    circ_list = []

    for _ in xrange(circ_number):
        # Generate the center coordinates randomly.
        random_x = random.randint(0, window_width - 1)
        random_y = random.randint(0, window_height - 1)

        # Find the maximum radius that this circle can have.
        radius = find_radius(circ_list, random_x, random_y)
        # Add it to the circle list.
        circ_list.append((random_x, random_y, radius))
        # Get the color of the center on the screen. If it is the
        # background color, draw the circle using the foreground color
        # and if it is the foreground color, draw the circle using the
        # background color.
        center_color = window.get_at((random_x, random_y))
        gfxdraw.filled_circle(window, random_x, random_y, radius,
                              fg_color if center_color == bg_color else bg_color)

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

