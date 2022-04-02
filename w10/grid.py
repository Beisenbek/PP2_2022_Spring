import pygame

BLACK = (0, 0, 0)
WHITE = (50, 50, 50)
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400


def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    while True:
        drawGrid()
        drawSnake()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()


def drawGrid():
    blockSize = 20 #Set the size of the grid block
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)

def drawSnake():
    block_size = 20
    snake = [(10,11), (10,12), (10,13), (10,14), (10,15)]

    # head

    x, y = snake[0]
    rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
    pygame.draw.rect(SCREEN, (100,0,0), rect)

    # tail

    for x, y in snake[1:]:
        rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
        pygame.draw.rect(SCREEN, (0,100,0), rect)
main()