#AUTHORS: Giovanni De Leon
#PONG AI PROJECT
#DATE: 9-18-24
#FILE DESCRIPTION: Ball Class
#SOURCES:Tech With Tim on Youtube for Pong code

import pygame
pygame.init()

# Creating Ball
class Ball:
    MAX_VELOCITY = 5
    WHITE = (255, 255, 255)
    COLOR = WHITE

    def __init__(self, x, y, radius):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.radius = radius
        self.x_vel = self.MAX_VELOCITY
        self.y_vel = 0

    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.radius)

    # Moving the ball
    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.y_vel = 0
        self.x_vel *= -1
