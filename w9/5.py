import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
is_blue = True

x = 30
y = 30
dx = 0
dy = 0
step = 3

clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    is_blue = not is_blue
        
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]: 
            dx = 0
            dy = -1
        elif pressed[pygame.K_DOWN]: 
            dx = 0
            dy = 1
        elif pressed[pygame.K_LEFT]:
            dx = -1
            dy = 0
        elif pressed[pygame.K_RIGHT]:
            dx = 1
            dy = 0

        x += step * dx
        y += step * dy
       
        screen.fill((0,0,0)) 

        if is_blue:
            color = (0, 0, 255)
        else:
            color = (0, 255, 0)
        
        pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 120))
        pygame.display.flip()
        #1/60 seconds
        clock.tick(10)