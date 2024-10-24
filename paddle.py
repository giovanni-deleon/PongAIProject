#AUTHORS: Giovanni De Leon
#PONG AI PROJECT
#DATE: 9-18-24
#FILE DESCRIPTION: Paddle Class
#SOURCES:Tech With Tim on Youtube for Pong code

import pygame
pygame.init()

class Paddle:
    WHITE = (255, 255, 255)

    COLOR = WHITE
    VELOCITY = 4

    def __init__(self, x, y, width, height):
      self.x = self.original_x = x
      self.y = self.original_y = y  
      self.width = width
      self.height = height

    def draw(self, win): 
         pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))

    # Moving paddle up or down
    def move(self, up=True):
        if up:
            self.y -= self.VELOCITY
        else:
            self.y += self.VELOCITY

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
