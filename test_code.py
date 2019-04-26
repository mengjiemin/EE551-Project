import pygame
from Code.Break_the_Brick import Ball_Collision, Ball, Break_Brick


a = Ball(move_x = 6, move_y = 6, R = 9, color = (255,200,255))
a.window_length = 800
a.window_width = 600
a.game_window = pygame.display.set_mode((a.window_length, a.window_width))
b = Ball_Collision


def ball_window(Ball):
    if Ball.ball_x <= Ball.R or Ball.ball_x >= (Ball.window_length - Ball.R):
        Ball.move_x = -Ball.move_x
    if Ball.ball_y <= Ball.R:
        Ball.move_y = -Ball.move_y



def test_sample():
    a.ball_x = 7
    a.ball_y = 6
    ball_window(a)
    assert(a.move_x == -6)



test_sample()