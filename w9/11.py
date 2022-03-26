import pygame

pygame.init()

screen = pygame.display.set_mode((400, 300))
done = False

clock = pygame.time.Clock()

color = (255, 255, 255)

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:#left
                            color = (255, 0, 0)
                    elif event.button == 3:#right
                            color = (0, 0, 255)

        pygame.draw.rect(screen, color, pygame.Rect(10, 10, 60, 120))        

        pygame.display.flip()
        #1/60 seconds
        clock.tick(60)