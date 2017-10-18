import pygame
import random
def subok():
    pygame.init()
    size_R = int(input('X '))
    size_U = int(input('Y '))
    box_size = int(input('Box size '))
    screen = pygame.display.set_mode((size_R, size_U))
    done = False
    is_blue = True
    x = 30
    y = 30

    clock = pygame.time.Clock()

    while not done:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                         done = True
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                         is_blue = not is_blue

            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_UP] and y!=0: y -= 2
            if pressed[pygame.K_DOWN] and y != int((size_U-box_size)): y += 2
            if pressed[pygame.K_LEFT] and x!=0 : x -= 2
            if pressed[pygame.K_RIGHT]and x != int((size_R-box_size)): x += 2
            print(x,y)

            screen.fill((0, 0, 0))
            if is_blue: color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            else: color = (random.randint(0,1), random.randint(0,1), random.randint(0,1))
            pygame.draw.rect(screen, color, pygame.Rect(x, y, box_size, box_size))

            pygame.display.flip()
            clock.tick(60)
subok()