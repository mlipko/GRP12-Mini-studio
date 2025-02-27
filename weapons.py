import pygame
from rectangle import *

class Weapon:
    def __init__(self, tear, bullet):
        self.tear = tear
        self.bullet = bullet

    def fire(self, position, direction):
        if self.ammo_count > 0:
            ammo = self.ammo_class(self.screen, position[0], position[1], 5, 5, 10)
            ammo.direction = direction
            self.ammo_count -= 1
            return ammo



class Bullet(Rectangle):
    def __init__(self, screen, x, y, width, height, speed, side):
        Rectangle.__init__(self, screen, x, y, width, height, speed)
        self.side =side
            
    def go_on(self):
        if self.side == "ally":
            self.move_right()
        else :
            self.move_left()
        self.draw((255, 255, 255))

classic = Weapon(15, Bullet)



class VerticalBullet(Rectangle):
    def __init__(self, screen, x, y, width, height, speed, side):
        Rectangle.__init__(self, screen, x, y, width, height, speed)
        self.side =side
            
    def go_on(self):
        self.move_down()
        self.draw((255, 255, 255))