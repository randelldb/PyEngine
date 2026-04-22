import pygame


class Ball:
    def __init__(self, x, y, radius, velocity_x=0, velocity_y=0):
        self.x = x
        self.y = y
        self.radius = radius

        self.velocity_x = velocity_x
        self.velocity_y = velocity_y

    def update(self, dt, gravity, ground, bounce):
        self.velocity_y = self.velocity_y + gravity * dt

        self.x = self.x + self.velocity_x * dt
        self.y = self.y + self.velocity_y * dt

        self.y = self.y + self.velocity_y * dt

        if self.y + self.radius >= ground:
            self.y = ground - self.radius
            self.velocity_y = -self.velocity_y * bounce

    def draw(self, screen):
        pygame.draw.circle(
            screen, (255, 255, 255), (int(self.x), int(self.y)), self.radius
        )
