from time import time
import pygame
import random
import time
from pygame import mixer
from sys import exit

pygame.mixer.init()
pygame.font.init()
pygame.init()

#Sounds
ball_collide = pygame.mixer.Sound("collide.mp3")
goal = pygame.mixer.Sound("goal.mp3")
#Font Sizes
player_score = 0
player2_score = 0 
game_font = pygame.font.SysFont("freesansbold.ttf", 32)


#make window for game
WIDTH, HEIGHT = 400, 600# width and height of the window

WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # sets the window
pygame.display.set_caption("Ping Pong") #displays the game
BG = pygame.transform.scale(pygame.image.load("black_image.jpeg"), (WIDTH, HEIGHT))

#player
P_HEIGHT = 5
P_WIDTH = 100
PLAYER_VEL = 5 #How fast does the player go in a direction 

#ball parameters
speed = [2.25 , 2.25] #speed of the ball based on the width and height of the screen

"""
Parameter: None
Displays the score for each player
"""

def score():
    player_text  = game_font.render(f"{player_score}", True, "red")
    WIN.blit(player_text,(WIDTH/2, 320))
    player2_text  = game_font.render(f"{player2_score}", True, "blue")
    WIN.blit(player2_text,(WIDTH/2, 280))
    
    
"""
Parameters: player2 - the opponent of the player
Parameters: ball - the ball for ping-pong
Sets up the ai for the opponent player. It is designed by using if 
statements the placement of the center of the player and the ball.
"""

def opponent_ai(player2,ball):
    if player2.left < ball.x: 
        player2.left += PLAYER_VEL
    if player2.right > ball.x:
        player2.right -= PLAYER_VEL

"""
Parameters: player - player that the user is controlling
Parameters: player2 - opponent of the player
Parameters: ball - ball for the game
draws the images of the game
"""
def draw(player, player2, ball):
    line = pygame.Rect(0, 310, 600, 2)
    pygame.draw.rect(WIN, "red", line)
    pygame.draw.rect(WIN, "red", player)
    pygame.draw.rect(WIN, "blue", player2)
    pygame.draw.rect(WIN, "white", ball)
    
    
    
"""
Parameters: ball - ball of the game
places the place to the center of the board once the 
balls the either of the player's boarders
"""
def ball_restart(ball):
    ball.center = (WIDTH/2, HEIGHT/2)
    speed[0] *= random.choice((1,-1))
    speed[1] *= random.choice((1,-1))
    

   
    
    

def main():
    run = True


    player = pygame.Rect(175, HEIGHT - P_HEIGHT, P_WIDTH, P_HEIGHT)
    player2 = pygame.Rect(175, 0 , P_WIDTH, P_HEIGHT)
    ball = pygame.Rect(0, 50 , 20, 20)
    global player_score, player2_score
     
    while run: # while the game is still running
        for event in pygame.event.get(): #monitors the events that are happening in the game
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed() # setup keys
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0: #if the player's x position is less than zero keep moving left
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL
        
        ball = ball.move(speed)
        if ball.top < 0: # if ball touches top of the board, do these commands
            player_score = player_score + 1
            goal.play()
            ball_restart(ball)
        if ball.bottom > HEIGHT: # if ball touches bottom of the board, do these commands
            player2_score = player2_score + 1
            goal.play()
            ball_restart(ball)
        if ball.left < 0 or ball.right > WIDTH: #if ball touchs the left or the right part of the screen, reverse the direction of the ball
            speed[0] = -speed[0]
            ball_collide.play()
        #collision
        if ball.colliderect(player):
            speed[1] = -speed[1]
            ball_collide.play()
        if ball.colliderect(player2):
            speed[1] = -speed[1]
            ball_collide.play()
        WIN.blit(BG,(0,0)) # places background image on the board
        score()
        opponent_ai(player2, ball)
        draw(player, player2, ball)
        pygame.display.update()

      
        

        
    pygame.quit()

if __name__ == "__main__": #code will only run if the filename is the same
    main()
