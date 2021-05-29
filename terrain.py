import pygame, random, numpy as np
pygame.init()

WORLD_LENGTH = 20
WORLD_HEIGHT = 15
SEA_LEVEL = 24
MEAN_HEIGHT = 9

PLAINS = random.randint(-1,1)

game = pygame.display.set_mode((960,720))
pygame.display.set_caption("Discount Minecraft")
clock = pygame.time.Clock()

# 0 = air, 1 = dirt, 2 = grass, 3 = stone
dirt = pygame.image.load('assets/dirt.png')
dirt_grass = pygame.image.load('assets/dirt_grass.png')
stone = pygame.image.load('assets/stone.png')

world = [[0]*WORLD_HEIGHT]*WORLD_LENGTH

class worldGenerator():
    def __init__(self, x, y, block, biome):
        self.x = x
        self.y = y
        self.block = block
        self.biome = biome
# 0 = air, 1 = dirt, 2 = grass, 3 = stone
    def generate():
        RANDOM_HEIGHT = MEAN_HEIGHT + random.randint(-2,2)
        for x in range(WORLD_LENGTH):
            for y in range(WORLD_HEIGHT):
                pass
            for i in range(RANDOM_HEIGHT):
                if i - 1 <= RANDOM_HEIGHT:
                    world[x][y] = 2
                elif i -2 <= RANDOM_HEIGHT:
                    world[x][y] = 1
                else:
                    world[x][y] = 3

    def draw():
        for x in range(WORLD_LENGTH):
            for y in range(WORLD_HEIGHT):
                if world[x][y] == 1:
                    game.blit(dirt,(x*48,y*48))
                elif world[x][y] == 2:
                    game.blit(dirt_grass,(x*48,y*48))
                elif world[x][y] == 3:
                    game.blit(stone,(x*48,y*48))

game.fill((102,255,255))
worldGenerator.generate()
worldGenerator.draw()

run = True
while run:
    clock.tick(24)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False