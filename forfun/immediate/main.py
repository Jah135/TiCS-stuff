import pygame
from gui import Quad, Text, compose, draw_to_surface
from layout import offset

pygame.init()

surface = pygame.display.set_mode((300, 300))
running = True


while running:
    composition = compose(
        Quad(0, 0, 50, 50, "red"),
        Quad(100, 100, 50, 50, "green", 10),
        Text(0, 0, pygame.Font(), "hello", "white"),
    )

    offset(composition, *pygame.mouse.get_pos())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    surface.fill("black")

    draw_to_surface(composition, surface)

    pygame.display.flip()
