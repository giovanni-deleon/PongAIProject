#AUTHORS: Giovanni De Leon, Max
#PONG AI PROJECT
#DATE: 9-18-24
#DESCRIPTION: Training AI to play Pong
#SOURCES:Tech With Tim on Youtube

import pygame
pygame.init()

# CREATING THE WINDOW(GUI)
# Declaring variables this way for extra moveablility.
WIDTH, HEIGHT = 700, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# FPS variable...
FPS = 60

# Drawing stuff on the screen
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddle Variables
PADDLE_WIDTH, PADDLE_HEIGHT= 20, 100

# We gotta figure out how to use encapsulation for this class
# Creating paddle
# Note to self: I love Pygame
class Paddle:
    COLOR = WHITE
    VELOCITY = 4

    def __init__(self, x, y, width, height):
      self.x = x
      self.y = y  
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

def draw(win, paddles):
    win.fill(BLACK)

    # Draw paddles
    for paddle in paddles:
        paddle.draw(win)

    pygame.display.update()

# Handles paddle movement logic
# Weird extra stuff is just calcs to keep play from going off screen
def handlePaddleMovement(keys, leftPaddle, rightPaddle):
    if keys[pygame.K_w] and (leftPaddle.y - leftPaddle.VELOCITY) >= 0:
        leftPaddle.move(up=True)
    if keys[pygame.K_s] and leftPaddle.y + leftPaddle.VELOCITY + leftPaddle <= HEIGHT:
        leftPaddle.move(up=False)

    if keys[pygame.K_UP] and rightPaddle.y - rightPaddle.VELOCITY >= 0:
        rightPaddle.move(up=True)
    if keys[pygame.K_DOWN] and rightPaddle.y + rightPaddle.VELOCITY + rightPaddle <= HEIGHT:
        rightPaddle.move(up=False)



def main():
    # Constantly checks events until we quit the game
    run = True

    # (Clock) Regulates framerate for every machine
    clock = pygame.time.Clock()

    # Doing calcs to perfectly center the graphic
    leftPaddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    rightPaddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)

    while run:
        clock.tick(FPS)
        draw(WIN, [leftPaddle, rightPaddle]) # Basically refresh rate

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break


        keys = pygame.key.get_pressed()
        handlePaddleMovement(keys, leftPaddle, rightPaddle)

    pygame.quit()    

# Makes it so main can only be ran from this proj...or something 
if __name__ == '__main__':
    main()