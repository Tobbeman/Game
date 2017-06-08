import sys, pygame
from player import Player

pygame.init()

#Colors
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)

#
blockSize = 16

#Screen
size = width, height = 16 * blockSize, 16 * blockSize
screen = pygame.display.set_mode(size)

#Player
player = Player((40,40), blockSize, blue)
player.accelerate((10.0,2))

#Variables
gravity = 0.1

#Flags
moveLeft = False
moveRight = False
jump = False
playerCollX = False
playerCollY = False
falling = True

#Level
level = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
         [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

levelBlocks = []
blockOffsetX = 0
blockOffsetY = 0
for x in range (0,16):
    for y in range (0,16):
        if level[y][x] == 1:
            levelBlocks.append(pygame.Rect(blockOffsetX,blockOffsetY, blockSize, blockSize))
        if level[y][x] == 2:
            player.x = blockOffsetX
            player.y = blockOffsetY
        blockOffsetY += blockSize
    blockOffsetY = 0
    blockOffsetX += blockSize

#Main loop
while 1:
    #Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moveLeft = True
            if event.key == pygame.K_RIGHT:
                moveRight = True
            if event.key == pygame.K_UP:
                jump = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moveLeft = False
                dx = 0
            if event.key == pygame.K_RIGHT:
                moveRight = False
                dx = 0
            if event.key == pygame.K_UP:
                jump = False
                dy = 0



    

    
    player.move()
    

    
    #Print inside screen
    screen.fill(black)

    #Handle everything related to the levelblocks
    for block in levelBlocks:
        #Print
        pygame.draw.rect(screen,white,block)
    

    pygame.draw.rect(screen,blue,player.rect)
    pygame.time.Clock().tick(60) #Change?
    pygame.display.flip()
