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

#Screen
size = width, height = 320, 240
screen = pygame.display.set_mode(size)

#Player
player = pygame.Rect(0,0,20,20)
dx = 0
dy = 0
playerSpeed = [1, 1]  #x,y

#Variables
gravity = 0.1

#Flags
moveLeft = False
moveRight = False
moveUp = False
moveDown = False

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

    #Print screen
    screen.fill(black)
    pygame.draw.rect(screen,white,player)
    pygame.time.Clock().tick(60) #Change?
    pygame.display.flip()
