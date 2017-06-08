import math, pygame

def addVectors(r1, r2):
    """ Returns the sum of two vectors """
    """ [0] = angle, [1] = lenght """
    x  = math.sin(r1[0]) * r1[1] + math.sin(r2[0]) * r2[1]
    y  = math.cos(r1[0]) * r1[1] + math.cos(r2[0]) * r2[1]
    
    angle  = 0.5 * math.pi - math.atan2(y, x)
    length = math.hypot(x, y)

    return (angle, length)

class Player:

    def __init__(self, pos, size, color):
        self.rect = pygame.Rect(pos[0],pos[1],size,size)
        self.speed = 0
        self.angle = 0

    def move(self):
        self.rect.x += math.sin(self.angle) * self.speed
        self.rect.y -= math.cos(self.angle) * self.speed

    def accelerate(self, vector):
        """ Change angle and speed by a given vector """
        (self.angle, self.speed) = addVectors((self.angle, self.speed), vector)

