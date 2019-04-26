# Reference: momobaba2018, (2018). Based on Python Game. [Online] Available at csdn blog <04/22/2019>

# Import Modules
import pygame
from pygame.locals import *
import sys, random, time, math



WINDOW_LENGTH = 800
WINDOW_WIDTH = 600
text_color = (255, 0, 255)


class Break_Brick():
    # Class for the game's window
    def __init__(self, window_length, window_width,game_window,window_color):
        # Draw the window of the game，define the size of the window
        self.window_length = WINDOW_LENGTH
        self.window_width = WINDOW_WIDTH
        self.game_window = pygame.display.set_mode((self.window_length, self.window_width))

        # Write the title of the game
        pygame.display.set_caption("Break the Brick")

        # Define the color of the window
        self.window_color = (0, 0, 0)

    def canvas_color(self):
        # Fill the color of the window
        self.game_window.fill(self.window_color)


class Ball():
    #  Class for the ball
    def __init__(self,color,move_x = 6,move_y = 6,R = 8):
        # Define the color and move rate of x-axis and y-axis and the radius of the ball
        self.move_x = move_x
        self.move_y = move_y
        self.R = R
        self.color = (255, 200, 255)



    def location_of_ball(self):
        # First time x-axis of the ball is wherever the mouse is、
        self.ball_x = 200

        #First time the y-axis of ball is exactly on the paddle
        self.ball_y = 400

        # Use function to draw a ball
        pygame.draw.circle(self.game_window, self.color, (self.ball_x, self.ball_y), self.R)

    def motation_of_ball(self):
        # Decide the location for x-axis and y-axis when the ball bounce back
        pygame.draw.circle(self.game_window, self.color, (self.ball_x, self.ball_y), self.R)
        self.ball_x += self.move_x
        self.ball_y -= self.move_y

        # Use collision function
        self.ball_window()
        self.ball_rect()

        # Set failure condition and show character " Good Game! "
        if self.ball_y > 600:
            self.gameover = self.over_font.render("Good Game!", False, (0, 255, 0))
            self.game_window.blit(self.gameover, (100, 250))
            self.over_sign = 1


class Paddle():
    # Class of the paddle
    def __init__(self, paddle_color,paddle_length,paddle_width):
        self.paddle_color = (100, 255, 255)
        self.paddle_length = 90
        self.paddle_width = 20

    # does not move the paddle, only detects what the mouse does, and calls move_paddle
    def motation_of_paddle(self):
        # Get the position of the mouse
        self.paddle_x, self.paddle_y = pygame.mouse.get_pos()
        # Make the boundary of paddle and draw the paddle

        # Make sure the paddle inside of the right boundary of the window
        if self.paddle_x >= self.window_length - self.paddle_length // 2:
            self.paddle_x = self.window_length - self.paddle_length // 2

        # Make sure the paddle inside of the left boundary of the window
        if self.paddle_x <= self.paddle_length // 2:
            self.paddle_x = self.paddle_length // 2

        pygame.draw.rect(self.game_window, self.paddle_color, (
        (self.paddle_x - self.paddle_length // 2), (self.window_width - self.paddle_width), self.paddle_length, self.paddle_width))

class Ball_Collision():
    # Collision between window and ball
    def ball_window(self):
        if self.ball_x <= self.R or self.ball_x >= (self.window_length - self.R):
            self.move_x = -self.move_x
            print(self.move_x)
        if self.ball_y <= self.R:
            self.move_y = -self.move_y

    # Collision between ball and paddle
    def ball_rect(self):

        # Define Collision Sign
        self.collision_sign_x = 0
        self.collision_sign_y = 0

        if self.ball_x < (self.paddle_x - self.paddle_length // 2):
            self.closestpoint_x = self.paddle_x - self.paddle_length // 2
            self.collision_sign_x = 1
        elif self.ball_x > (self.paddle_x + self.paddle_length // 2):
            self.closestpoint_x = self.paddle_x + self.paddle_length // 2
            self.collision_sign_x = 2
        else:
            self.closestpoint_x = self.ball_x
            self.collision_sign_x = 3

        if self.ball_y < (self.window_width - self.paddle_width):
            self.closestpoint_y = (self.window_width - self.paddle_width)
            self.collision_sign_y = 1
        elif self.ball_y > self.window_width:
            self.closestpoint_y = self.window_width
            self.collision_sign_y = 2
        else:
            self.closestpoint_y = self.ball_y
            self.collision_sign_y = 3

        self.distance = math.sqrt(
            math.pow(self.closestpoint_x - self.ball_x, 2) + math.pow(self.closestpoint_y - self.ball_y, 2))

        # Ball above and on the left of the paddle:
        while self.distance < self.R and self.collision_sign_y == 1 and (
                self.collision_sign_x == 1 or self.collision_sign_x == 2):
            if self.collision_sign_x == 1 and self.move_x > 0:
                self.move_x = - self.move_x
                self.move_y = - self.move_y
            if self.collision_sign_x == 1 and self.move_x < 0:
                self.move_y = - self.move_y
            if self.collision_sign_x == 2 and self.move_x < 0:
                self.move_x = - self.move_x
                self.move_y = - self.move_y
            if self.collision_sign_x == 2 and self.move_x > 0:
                self.move_y = - self.move_y

        # Ball above and on the left end of the paddle:
        if self.distance < self.R and self.collision_sign_y == 1 and self.collision_sign_x == 3:
            self.move_y = - self.move_y

        # Ball on the left or right end of the paddle
        if self.distance < self.R and self.collision_sign_y == 3:
            self.move_x = - self.move_x

    def ball_brick(self):
        # Define the collision sign
        self.collision_sign_bx = 0
        self.collision_sign_by = 0

        if self.ball_x < self.brick_x:
            self.closestpoint_bx = self.brick_x
            self.collision_sign_bx = 1
        elif self.ball_x > self.brick_x + self.brick_length:
            self.closestpoint_bx = self.brick_x + self.brick_length
            self.collision_sign_bx = 2
        else:
            self.closestpoint_bx = self.ball_x
            self.collision_sign_bx = 3

        if self.ball_y < self.brick_y:
            self.closestpoint_by = self.brick_y
            self.collision_sign_by = 1
        elif self.ball_y > self.brick_y + self.brick_width:
            self.closestpoint_by = self.brick_y + self.brick_width
            self.collision_sign_by = 2
        else:
            self.closestpoint_by = self.ball_y
            self.collision_sign_by = 3

        # Distance between the closest point on brick with the center of the ball
        self.distance_b = math.sqrt(
            math.pow(self.closestpoint_bx - self.ball_x, 2) + math.pow(self.closestpoint_by - self.ball_y, 2))

        # Upper left, Upper right and above the brick
        if self.distance_b < self.R and self.collision_sign_by == 1 and (
                self.collision_sign_bx == 1 or self.collision_sign_bx == 2):
            if self.collision_sign_bx == 1 and self.move_x > 0:
                self.move_x = - self.move_x
                self.move_y = - self.move_y
            if self.collision_sign_bx == 1 and self.move_x < 0:
                self.move_y = - self.move_y
            if self.collision_sign_bx == 2 and self.move_x < 0:
                self.move_x = - self.move_x
                self.move_y = - self.move_y
            if self.collision_sign_bx == 2 and self.move_x > 0:
                self.move_y = - self.move_y
        if self.distance_b < self.R and self.collision_sign_by == 1 and self.collision_sign_bx == 3:
            self.move_y = - self.move_y

        # Under left, Under right and Below the brick
        if self.distance_b < self.R and self.collision_sign_by == 2 and (
                self.collision_sign_bx == 1 or self.collision_sign_bx == 2):
            if self.collision_sign_bx == 1 and self.move_x > 0:
                self.move_x = - self.move_x
                self.move_y = - self.move_y
            if self.collision_sign_bx == 1 and self.move_x < 0:
                self.move_y = - self.move_y
            if self.collision_sign_bx == 2 and self.move_x < 0:
                self.move_x = - self.move_x
                self.move_y = - self.move_y
            if self.collision_sign_bx == 2 and self.move_x > 0:
                self.move_y = - self.move_y
        if self.distance_b < self.R and self.collision_sign_by == 2 and self.collision_sign_bx == 3:
            self.move_y = - self.move_y

        # Ball in the middle of two bricks
        if self.distance_b < self.R and self.collision_sign_by == 3:
            self.move_x = - self.move_x


class Brick():
    def __init__(self, brick_color, brick_list,brick_length, brick_width):
        self.brick_color = (150,0, 255)
        self.brick_list = [[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],
                           [1, 1, 1, 1, 1, 1, 1],[1,1,1,1,1,1,1]]
        self.brick_length = 80
        self.brick_width = 20

    def Insert_bricks(self):
        for i in range(7):
            for j in range(7):
                self.brick_x = j * (self.brick_length + 35)
                self.brick_y = i * (self.brick_width + 20) + 40
                if self.brick_list[i][j] == 1:
                    # Draw the brick
                    pygame.draw.rect(self.game_window, self.brick_color,
                                     ((self.brick_x+15), self.brick_y, self.brick_length, self.brick_width))
                    # Call collision function
                    self.ball_brick()
                    if self.distance_b < self.R:
                        self.brick_list[i][j] = 0
                        self.score += self.point
        # Define win the game
        if self.brick_list == [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],
                               [0, 0, 0, 0, 0, 0, 0],[0,0,0,0,0,0,0]]:
            self.win = self.win_font.render("Winner Winner!", False, (0, 255, 0))
            self.game_window.blit(self.win, (100, 130))
            self.win_sign = 1



class Score():
    def __init__(self,score,score_font,point):
        # Initial score is 0
        self.score = 0
        # Character of the score
        self.score_font = pygame.font.SysFont('arial', 20)
        # Initial point
        self.point = 1


    def countscore(self):
        # Show the score
        my_score = self.score_font.render("Numbers you break the break is:"+str(self.score) + "  " +"pieces", False, (255, 100, 150))
        self.game_window.blit(my_score, (10, 15))


class Good_Game():
    def __init__(self,over_font,over_sign):
        self.over_font = pygame.font.SysFont('arial', 80)
        self.over_sign = 0


class Win():
    def __init__(self,win_font, win_sign):
        self.win_font = pygame.font.SysFont('arial', 80)
        self.win_sign = 0


class First_Page():
    def __init__(self):
        self.window_length = WINDOW_LENGTH
        self.window_width = WINDOW_WIDTH
        self.game_window = pygame.display.set_mode((self.window_length, self.window_width))
        self.window_color = (0, 0, 0)

    def Drawtext(self,text,font,game_window,x,y):
        self.text_obj = font.render(text,1,text_color)
        self.text_rect = self.text_obj.get_rect()
        self.text_rect.topleft = (x,y)
        self.game_window.blit(self.text_obj,self.text_rect)
        return True

    def Terminate(self):
        self.pygame.quit()
        self.sys.exit()

    def WaitForPlayerToPressKey(self,window_length,window_width):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.Terminate()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.Terminate()
                    return







class Main(Break_Brick, Paddle, Ball, Brick, Ball_Collision, Score, Win, Good_Game):
    def __init__(self):
        super(Main, self).__init__(window_length= 600, window_width=500,
                                   game_window=pygame.display.set_mode(),
                                   window_color=(0,0,0))
        super(Break_Brick, self).__init__(paddle_color = (255,0,0),paddle_length = 100,paddle_width = 10)
        super(Paddle, self).__init__(color=(255, 200, 255), move_x=6, move_y=6, R=10)
        super(Ball, self).__init__(brick_color=(150, 0, 255),
                                   brick_list=[[1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1],
                                               [1, 1, 1, 1, 1, 1, 1],
                                               [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]],
                                   brick_length=80, brick_width=20
                                   )
        super(Brick, self).__init__(score = 0, score_font = ("arial",20), point = 1,)
        super(Ball_Collision, self).__init__(score = 0, score_font = ("arial",20), point = 1,
                                             )
        super(Score, self).__init__(win_font = pygame.font.SysFont('arial', 80), win_sign = 0)
        super(Win, self).__init__(over_font = 1, over_sign = 1)

        game_start_font = pygame.font.SysFont(None, 48)
        game_window = pygame.display.set_mode((WINDOW_LENGTH , WINDOW_WIDTH ), 0, 32)
        f = First_Page()
        f.Drawtext('LET US START THE GAME', game_start_font, game_window,
                   ( WINDOW_WIDTH / 3 + 20) , (WINDOW_LENGTH / 4 + 5))
        f.Drawtext('Press any key to start', game_start_font, game_window,
                   (WINDOW_WIDTH / 3) + 30, (WINDOW_LENGTH / 3) + 15)
        pygame.display.update()
        f.WaitForPlayerToPressKey(WINDOW_LENGTH, WINDOW_WIDTH)
        # Define the sign for starting the game
        start_sign = 0

        while True:
            self.canvas_color()
            self.motation_of_paddle()
            self.countscore()

            if self.over_sign == 1 or self.win_sign == 1:
                break
            # Statue of the Game Window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    pressed_array = pygame.mouse.get_pressed()
                    if pressed_array[0]:
                        start_sign = 1
            if start_sign == 0:
                self.location_of_ball()
            else:
                self.motation_of_ball()

            self.Insert_bricks()

            pygame.display.update()
            time.sleep(0.010)


if __name__ == '__main__':
    pygame.init()
    pygame.font.init()
    catchball = Main()


