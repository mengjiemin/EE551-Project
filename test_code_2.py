import pygame
from Code.Break_the_Brick import Ball_Collision, Ball, Break_Brick,Paddle,math

a = Ball(move_x = 6, move_y = 6, R = 8, color = (255,200,255))
b = Paddle(paddle_color = (100, 255, 255),paddle_length = 90,paddle_width = 20)


def ball_rect(Ball,Paddle):

    collision_sign_x = 1
    collision_sign_y = 1

    if a.ball_x < (b.paddle_x - b.paddle_length // 2):
        a.closestpoint_x= b.paddle_x - b.paddle_length // 2
        collision_sign_x = 1
    elif a.ball_x > (b.paddle_x + b.paddle_length // 2):
        a.closestpoint_x = b.paddle_x + b.paddle_length // 2
        collision_sign_x = 2

    distance = math.sqrt(
        math.pow(a.closestpoint_x - a.ball_x, 2) + math.pow(a.closestpoint_y - a.ball_y, 2))

    while distance < Ball.R and collision_sign_y == 1 and collision_sign_x == 1 :
        if collision_sign_x == 1 and Ball.move_x > 0:
            Ball.move_x =   Ball.move_x
            Ball.move_y = - Ball.move_y
        if collision_sign_x == 1 and Ball.move_x < 0:
            Ball.move_y = - Ball.move_y


def test_code_2():
    a.ball_x = 7
    a.ball_y = 6
    ball_rect(a,b)
    assert(a.move_x == 6)

test_code_2()