import pygame 
from pygame.locals import * 
from sys import exit 

background_image_filename = r'E:\GIT\learn\pygame\Kinsley_pg\Chapter_03\sushiplate.jpg' 

pygame.init() 
screen = pygame.display.set_mode((640, 480), 0, 32) 
background = pygame.image.load(background_image_filename).convert()  
 
Fullscreen = False 
 
while True: 
 
     for event in pygame.event.get(): 
          if event.type == QUIT:
               pygame.quit()
               exit() 
          if event.type == KEYDOWN: 
               if event.key == K_UP: 
                    Fullscreen = not Fullscreen  
               if Fullscreen:
                    print('1')
                    screen = pygame.display.set_mode((640, 480), FULLSCREEN, 32) 
               else: 
                    screen = pygame.display.set_mode((640, 480), 0, 32) 
 
     screen.blit(background, (0,0)) 
     pygame.display.update()
