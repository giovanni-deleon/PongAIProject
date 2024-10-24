#AUTHORS: Giovanni De Leon
#PONG AI PROJECT
#DATE: 9-18-24
#FILE DESCRIPTION: Main file to play Pong
#SOURCES:Tech With Tim on Youtube for Pong code

import pygame
pygame.init()
from paddle import Paddle
from ball import Ball

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

# Ball Radius..
BALL_RADIUS = 7

SCORE_FONT = pygame.font.SysFont("comicsans", 50)
WINNING_SCORE = 10


def draw(win, paddles, ball, left_score, right_score):
    win.fill(BLACK)

    # Need to study this
    left_score_text = SCORE_FONT.render(f"{left_score}", 1, WHITE)
    right_score_text = SCORE_FONT.render(f"{right_score}", 1, WHITE)
    win.blit(left_score_text, (WIDTH//4 - left_score_text.get_width()//2, 20))
    win.blit(right_score_text, (WIDTH * (3/4) - right_score_text.get_width()//2, 20))

    # Draw paddles
    for paddle in paddles:
        paddle.draw(win)

    # Draw dotted line in the middle of the screen
    for i in range(10, HEIGHT, HEIGHT//20):
        if i % 2 == 1:
            continue
        pygame.draw.rect(win, WHITE, (WIDTH//2 - 5, i, 10, HEIGHT//20))


    ball.draw(win)
    pygame.display.update()

# Collision logic
# STUDY THIS FUNCTION: Note to self
def handleCollision(ball, leftPaddle, rightPaddle):
    # Ceiling collision handeling
    if ball.y + ball.radius >= HEIGHT:
        ball.y_vel *= -1
    elif ball.y - ball.radius <=0:
        ball.y_vel *= -1

    if ball.x_vel < 0:
        if ball.y >= leftPaddle.y and ball.y <= leftPaddle.y + leftPaddle.height:
            if ball.x - ball.radius <= leftPaddle.x + leftPaddle.width:
                ball.x_vel *= -1

                # Y values
                middle_y = leftPaddle.y + leftPaddle.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (leftPaddle.height / 2) / ball.MAX_VELOCITY
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = -1 * y_vel
    else:
        if ball.y >= rightPaddle.y and ball.y <= rightPaddle.y + rightPaddle.height:
            if ball.x + ball.radius >= rightPaddle.x:
                ball.x_vel *= -1

                # Y values
                middle_y = rightPaddle.y + rightPaddle.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (rightPaddle.height / 2) / ball.MAX_VELOCITY
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = -1 * y_vel


# Handles paddle movement logic
# Weird extra stuff is just calcs to keep play from going off screen
def handlePaddleMovement(keys, leftPaddle, rightPaddle):
    if keys[pygame.K_w] and ((leftPaddle.y ) >= 0):
        leftPaddle.move(up=True)
    if keys[pygame.K_s] and ((leftPaddle.y + leftPaddle.height) <= HEIGHT):
        leftPaddle.move(up=False)

    if keys[pygame.K_UP] and ((rightPaddle.y) >= 0):
        rightPaddle.move(up=True)
    if keys[pygame.K_DOWN] and ((rightPaddle.y + rightPaddle.height) <= HEIGHT):
        rightPaddle.move(up=False)



def main():
    # Constantly checks events until we quit the game
    run = True

    # (Clock) Regulates framerate for every machine
    clock = pygame.time.Clock()

    # Doing calcs to perfectly center the graphic
    leftPaddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    rightPaddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)

    # Initializing Ball
    ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS)

    # Scoring
    left_score = 0
    right_score = 0

    while run:
        clock.tick(FPS)
        draw(WIN, [leftPaddle, rightPaddle], ball, left_score, right_score) # Basically refresh rate

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break


        keys = pygame.key.get_pressed()
        handlePaddleMovement(keys, leftPaddle, rightPaddle)

        ball.move()
        handleCollision(ball, leftPaddle, rightPaddle)

        if ball.x < 0:
            right_score += 1
            ball.reset()
        elif ball.x > WIDTH:
            left_score += 1
            ball.reset()


        won = False
        if left_score >= WINNING_SCORE:
            won = True
            win_text = "Left Player Won!"
        elif right_score >= WINNING_SCORE:
            won = True
            win_text = "Right Player Won!"

        if won:
            text = SCORE_FONT.render(win_text, 1, WHITE)
            WIN.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height() //2))
            pygame.display.update()
            pygame.time.delay(5000)
            ball.reset()
            leftPaddle.reset()
            rightPaddle.reset()
            left_score = 0
            right_score = 0


    pygame.quit()    

# Makes it so main can only be ran from this proj...or something 
if __name__ == '__main__':
    main()