# Python Game for AWS server

# Importing the cv2 (OpenCV) library
#import cv2

# Importing the numpy library as np
#import numpy as np

# Importing the Pygame library
import pygame

#Importing the Time Library
import time

# Importing everything from pygame.locals class
#from pygame.locals import *

# Importing the systems library
#import sys

# Importing the Operating Systems Library
#import os

# Initializing all imported pygame modules
pygame.init()


RED = (255, 0, 0)
BLUE = (0, 0, 255)


# Creating our window
# pygame.display.set_mode((Width_of_Window, Height_of_Window))
Window  = pygame.display.set_mode((1000, 900))

# Giving the pygame window a title
# pygame.display.set_caption("Title_of_Pygame_Window")
pygame.display.set_caption("Penis Game")

Screen_Width = 1000
Screen_Height = 900

Player_One_X_Coordinate = 50
Player_Two_X_Coordinate = 50
Player_One_Y_Coordinate = 50
Player_Two_Y_Coordinate = 100
Player_Velocity = 10

Player_Width = 50

Player_Height = 50


Game_Running = True

while Game_Running:
    pygame.time.delay(100)

    for event in pygame.event.get():

        # Checking to see if the player clicks the exit button on the pygame window
        if event.type == pygame.QUIT:
            Game_Running = False



    # Creating the key events for our players

    Keys = pygame.key.get_pressed()

    if Keys[pygame.K_UP] and Player_One_X_Coordinate > Player_Velocity:

        Player_One_Y_Coordinate -= Player_Velocity

    if Keys[pygame.K_DOWN] and Player_One_X_Coordinate < Screen_Width - Player_Width - Player_Velocity:

        Player_One_Y_Coordinate += Player_Velocity

    if Keys[pygame.K_LEFT] and Player_One_Y_Coordinate < Screen_Height - Player_Height- Player_Velocity and Player_One_Y_Coordinate > Player_Velocity:

        Player_One_X_Coordinate -= Player_Velocity

    if Keys[pygame.K_RIGHT] and Player_One_Y_Coordinate > Player_Velocity:

        Player_One_X_Coordinate += Player_Velocity



    # Filling in the pygame window so that we clear all the player's old positions
    Window.fill((0, 0, 0))

    # Drawing & creating our rectangle
    #pygame.draw.rect(Window, (255, 0, 0),(Player_One_X_Coordinate, Player_One_Y_Coordinate, Player_Width, Player_Height))
    pygame.draw.circle(Window, (255, 0, 0), (Player_One_X_Coordinate, Player_One_Y_Coordinate), 20, 0)
    pygame.draw.circle(Window, (0, 0, 255), (Player_Two_X_Coordinate, Player_Two_Y_Coordinate), 20, 0)
    #pygame.draw.rect(Window, (0, 0, 255),(Player_Two_X_Coordinate, Player_Two_Y_Coordinate, Player_Width, Player_Height))

    # Updating our pygame window with the rectangle character that we created
    pygame.display.update()



# Ends the program within the pygame window and closes the pygame window
pygame.quit()


    
