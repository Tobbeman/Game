import math

class Player:

    def __init__(self, (x,y), size, color):
        self.x = x
        self.y = y
        self.size = size
        self.speed = 0
        self.angle = 0

    def move(self):
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed

    def accelerate(self, vector):
        """ Change angle and speed by a given vector """
        (self.angle, self.speed) = addVectors((self.angle, self.speed), vector)

