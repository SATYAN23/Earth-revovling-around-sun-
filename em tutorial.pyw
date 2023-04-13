import os
import math as m
import pygame
from datetime import datetime
import time
import pyautogui
from pygame.locals import *

width, height = pyautogui.size()
pygame.init()

i_icon = os.getcwd() + '.\p.png'
icon = pygame.image.load(i_icon)
pygame.display.set_icon(icon)

speed = 0


def main():
    global speed
    color = (0, 255, 0)

    width = 1000
    height = 1000
    r = 300

    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("earth-moon-relation")
    font = pygame.font.SysFont("Segoe UI", 25)
    clock = pygame.time.Clock()
    cpt = win.get_rect().center

    speed = 2 * 3.14 * r / (8000 / 2100)
    speed = str(speed)
    print("velocity of circle around solid circle" + speed)

    run = True
    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for i in range(0, 360):
            win.fill((255, 255, 255))

            S = "velocity of circle " + " : " + str(speed) + "units"
            draw3 = font.render(str(S), True, color)
            win.blit(draw3, (10, 10))

            earth = pygame.image.load("E.png")
            earth = pygame.transform.scale(earth, (60, 60))
            win.blit(earth, (r + 130 + r * m.sin(m.radians(i)), r + 130 + r * m.cos(m.radians(i))))

            sun = pygame.image.load("S.png")
            sun = pygame.transform.scale(sun, (100, 100))
            win.blit(sun, [450, 450])
            pygame.draw.circle(win, (51, 255, 51), [500, 500], 200, 2)

            earth_rect = earth.get_rect(x = r + 150 + r * m.sin(m.radians(i)), y = r + 140 + r * m.cos(m.radians(i)))
            ear = (earth_rect[0], earth_rect[1])
            moon = pygame.image.load("M.png")
            moon = pygame.transform.scale(moon, (20, 20))
            win.blit(moon, ear)
            pygame.draw.circle(win, (51, 255, 51), ear,80,3)
            pygame.display.update()

            pygame.display.update()

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
