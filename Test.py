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
dx, dy = 0, 0
playerSpeed = [1, 1]  #x,y

#Variables
gravity = 0.1

#Flags
moveLeft = False
moveRight = False
moveUp = False
moveDown = False

#Level
level = [[1,2,3,4,1,1,1,1,1,1,1,1,1,1,1,1],
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
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

levelBlocks = []
blockOffsetX = 0
blockOffsetY = 0
for x in range (0,16):
    for y in range (0,16):
        print (level[x][y])
        if level[x][y] == 1:
            levelBlocks.append(pygame.Rect(blockOffsetX,blockOffsetY, 16, 16))
            #print("x: ",blockOffsetX,"y: ",blockOffsetY)
        blockOffsetX += blockSize
    blockOffsetX = 0
    blockOffsetY += blockSize

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
                moveUp = True
            if event.key == pygame.K_DOWN:
                moveDown = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moveLeft = False
                dx = 0
            if event.key == pygame.K_RIGHT:
                moveRight = False
                dx = 0
            if event.key == pygame.K_UP:
                moveUp = False
                dy = 0
            if event.key == pygame.K_DOWN:
                moveDown = False
                dy = 0

    #Movement Logic
    if moveLeft:
        dx = -playerSpeed[0]
    if moveRight:
        dx = playerSpeed[0]
    if moveUp:
        dy = -playerSpeed[1]
    if moveDown:
        dy = playerSpeed[1]

    #Collision
    if 0 < player.x + dx and player.x + player.width + dx < width:
        player.x += dx
    if 0 < player.y + dy and player.y + player.height + dy < height:
        player.y += dy

    #Print inside screen
    screen.fill(black)

    for block in levelBlocks:
        pygame.draw.rect(screen,white,block)

    pygame.draw.rect(screen,blue,player)
    pygame.time.Clock().tick(60) #Change?
    pygame.display.flip()
