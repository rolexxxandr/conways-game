import pygame
from random import randint
from copy import deepcopy

# задаємо розміри вікна
WIDTH = 1280 
HEIGHT = 720
TILE = 20 # розмір клітки
W = WIDTH // TILE  # оприділяємо кількість кліток в ширину 
H = HEIGHT // TILE # і висоту
FPS = 10 # задаємо частоту кадрів

pygame.init() #
surface = pygame.display.set_mode((WIDTH, HEIGHT)) # створюємо вікно з переданими розмірами
clock = pygame.time.Clock() #

current_stage = [[randint(0, 1) for i in range(W)] for j in range(H)]
next_stage = [[0 for i in range(W)] for j in range(H)]

# провірка стану клітки
def check_status(current_stage, x, y):
    count = 0
    for j in range(y - 1, y + 2):
        for i in range(x - 1, x + 2):
            if current_stage[j][i]:
                count += 1
    
    if current_stage[y][x]:
        count -= 1
        if count == 2 or count == 3:
            return 1
        return 0
    else:
        if count == 3:
            return 1
        return 0

while True:
    surface.fill(pygame.Color("black")) # заливаємо вікно чорним кольором

    # провірка на закриття
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # малюємо сітку за допомогою горизонтальних і вертикальних ліній, кількість ліній і їх крок буде оприділятися за розміром клітки
    for x in range(0, WIDTH, TILE):
        pygame.draw.line(surface, pygame.Color("black"), (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, TILE):
        pygame.draw.line(surface, pygame.Color("black"), (0, y), (WIDTH, y))

    # малюємо клітини
    for x in range(1, W - 1):
        for y in range(1, H -1):
            if current_stage[y][x]:
                pygame.draw.rect(surface, pygame.Color("green"), (x * TILE + 2, y * TILE + 2, TILE - 2, TILE - 2))
            next_stage[y][x] = check_status(current_stage, x , y)

    current_stage = deepcopy(next_stage)

    pygame.display.set_caption("FPS: " + str(int(clock.get_fps())))
    pygame.display.flip()
    clock.tick(FPS)