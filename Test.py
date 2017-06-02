import sys, pygame
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
player = pygame.Rect(0,0,blockSize,blockSize)
playerCollRectX = player.copy()
playerCollRectY = playerCollRectX.copy()
dx, dy = 0, 0
playerSpeed = [1, 1]  #x,y

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

    #Movement Logic
    if moveLeft:
        dx = -playerSpeed[0]
    if moveRight:
        dx = playerSpeed[0]
    if jump:
        dy = -playerSpeed[1]

    #Print inside screen
    screen.fill(black)

    #Collision
    if falling:
        dy += gravity

    playerCollRectX.x = player.x + dx
    playerCollRectX.y = player.y
    playerCollRectY.y = player.y + dy
    playerCollRectY.x = player.x
    playerCollX = False
    playerCollY = False


    #Handle everything related to the levelblocks
    for block in levelBlocks:
        #Print
        pygame.draw.rect(screen,white,block)
        #Collision
        if playerCollRectX.colliderect(block):
            playerCollX = True
        if playerCollRectY.colliderect(block):
            playerCollY = True


    if not playerCollX:
        player.x = playerCollRectX.x
    if not playerCollY:
        player.y = playerCollRectY.y

    pygame.draw.rect(screen,blue,player)
    pygame.time.Clock().tick(60) #Change?
    pygame.display.flip()
