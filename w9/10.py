import pygame

pygame.init()

screen = pygame.display.set_mode((400, 300))
done = False

clock = pygame.time.Clock()

font = pygame.font.SysFont("comicsansms", 50)
text = font.render("Hello, World", False, (0, 255, 0))

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    is_blue = not is_blue
        
        screen.fill((255, 255, 255)) 

        screen.blit(text, (200 - text.get_width() // 2, 150 - text.get_height() // 2))


        pygame.display.flip()
        #1/60 seconds
        clock.tick(60)