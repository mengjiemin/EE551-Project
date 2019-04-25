import pygame
from Code.Break_the_Brick import First_Page

def test_sample():
    WINDOW_LENGTH = 300
    WINDOW_WIDTH = 400
    game_start_font = pygame.font.SysFont('arial', 80)
    game_window = pygame.display.set_mode((WINDOW_LENGTH, WINDOW_WIDTH), 0, 32)
    f = First_Page

    assert(f.Drawtext('START THE GAME.', game_start_font, game_window,
                       WINDOW_WIDTH / 3 + 50 , (WINDOW_LENGTH / 4 + 5)))
