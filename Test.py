import sys, pygame
pygame.init()

size = width, height = 320, 240

#Colors
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)

screen = pygame.display.set_mode(size)

player = pygame.Rect(0,0,20,20)
playerSpeed = 2

#Flags
moveLeft = False
moveRight = False

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

    #Logic
    if moveLeft:
        player.x -= playerSpeed
    if moveRight:
        player.x += playerSpeed

    #Print screen
    screen.fill(black)
    pygame.draw.rect(screen,white,player)
    pygame.time.Clock().tick(60) #Change?
    pygame.display.flip()
