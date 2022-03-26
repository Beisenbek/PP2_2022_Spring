import pygame

pygame.init()


pygame.mixer.music.load('sounds/m1.ogg')
pygame.mixer.music.play(0)


screen = pygame.display.set_mode((400, 300))
done = False

clock = pygame.time.Clock()

image = pygame.image.load('images/ball.png')

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    is_blue = not is_blue
        
        screen.fill((255, 255, 255)) 

        screen.blit(image, (20, 20))

        pygame.display.flip()
        #1/60 seconds
        clock.tick(60)