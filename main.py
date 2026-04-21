import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

ball_x = 400
ball_y = 400
ball_radius = 20

velocity = 0
gravity = 500

ground = 550
bounce = 0.7

dt = 0


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # physics
    velocity = velocity + gravity * dt
    ball_y =  ball_y + velocity * dt

    if ball_y >= ground:
        ball_y = ground
        velocity = -velocity * bounce

    # print(f"y={ball_y:.1f}, v={velocity:.1f}")

    screen.fill("black")

    pygame.draw.circle(screen, (255, 255, 255), (ball_x, ball_y), ball_radius)
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0,550 + ball_radius,1280,10))

    pygame.display.flip()

    dt = clock.tick(60) / 1000



pygame.quit()