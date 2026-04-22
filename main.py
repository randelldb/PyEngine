import random

import pygame

from ball import Ball

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

gravity = 200
ground = 550
bounce = 0.7
dt = 0


balls = []

for i in range(10000):
    balls.append(Ball(random.randint(0, 1280), random.randint(0, 200), 1, 20, 0))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    for ball in balls:
        ball.update(dt, gravity, ground, bounce)
        ball.draw(screen)

    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0, 550, 1280, 10))

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
