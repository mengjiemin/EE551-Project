import pygame
from Code.Break_the_Brick import Ball_Collision, Ball, Break_Brick,Paddle,math

a = Ball(move_x = 6, move_y = 6, R = 8, color = (255,200,255))
b = Paddle(paddle_color = (100, 255, 255),paddle_length = 90,paddle_width = 20)


def ball_rect(Ball,Paddle):

    collision_sign_x = 1
    collision_sign_y = 1
    distance = 7

    while distance < Ball.R and collision_sign_y == 1 and collision_sign_x == 1 :
        if collision_sign_x == 1 and Ball.move_x > 0:
            Ball.move_x =   Ball.move_x
            break
        if collision_sign_x == 1 and Ball.move_x < 0:
            Ball.move_y = - Ball.move_y
            break


def test_code_2():
    ball_rect(a,b)
    assert(a.move_y == 6)

test_code_2()