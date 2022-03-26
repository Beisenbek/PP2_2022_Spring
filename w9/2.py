import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
is_blue = True

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    is_blue = not is_blue

        if is_blue:
            pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(30, 30, 60, 120))
        else:
            pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(30, 30, 60, 120))

        pygame.display.flip()