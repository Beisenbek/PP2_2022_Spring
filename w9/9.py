import pygame

pygame.init()

screen = pygame.display.set_mode((400, 300))
done = False

clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    is_blue = not is_blue
        
        screen.fill((255, 255, 255)) 

        pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(30, 30, 60, 60))
        pygame.draw.circle(screen, (0, 0, 255), (100, 100), 25)

        points = [(130, 30), (160, 0), (190, 30)]
        pygame.draw.polygon(screen, (0, 0, 255), points)


        pygame.display.flip()
        #1/60 seconds
        clock.tick(60)