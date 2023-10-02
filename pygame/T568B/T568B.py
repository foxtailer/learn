import pygame
from pygame.locals import *
from sys import exit
import time
import random

pygame.init()

screen = pygame.display.set_mode((310, 500), 0, 32)
font = pygame.font.SysFont("arial", 20)
bg = pygame.image.load(r"C:\Users\yaroslav\Desktop\python\GIT\learn\pygame\T568B\img\empty.jpg").convert()
orange_white = pygame.image.load(r"C:\Users\yaroslav\Desktop\python\GIT\learn\pygame\T568B\img\0.jpg").convert()
orange = pygame.image.load(r"C:\Users\yaroslav\Desktop\python\GIT\learn\pygame\T568B\img\1.jpg").convert()
green_white = pygame.image.load(r"C:\Users\yaroslav\Desktop\python\GIT\learn\pygame\T568B\img\2.jpg").convert()
blue = pygame.image.load(r"C:\Users\yaroslav\Desktop\python\GIT\learn\pygame\T568B\img\3.jpg").convert()
blue_white = pygame.image.load(r"C:\Users\yaroslav\Desktop\python\GIT\learn\pygame\T568B\img\4.jpg").convert()
green = pygame.image.load(r"C:\Users\yaroslav\Desktop\python\GIT\learn\pygame\T568B\img\5.jpg").convert()
brown_white = pygame.image.load(r"C:\Users\yaroslav\Desktop\python\GIT\learn\pygame\T568B\img\6.jpg").convert()
brown = pygame.image.load(r"C:\Users\yaroslav\Desktop\python\GIT\learn\pygame\T568B\img\7.jpg").convert()
shuffle = pygame.image.load(r"C:\Users\yaroslav\Desktop\python\GIT\learn\pygame\T568B\img\shuffle.jpg").convert()

positions = [(41, 160),(70, 160), (99, 160),(125, 160), (154, 160), (180, 160), (210, 160), (238, 160)]
original_order = (orange_white, orange, green_white, blue, blue_white, green, brown_white, brown)
randomize = list(original_order)
random.shuffle(randomize)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    screen.blit(bg, (0,0))
    
    for i in range(len(positions)):
        screen.blit(randomize[i], positions[i])

    pygame.display.update()
    time.sleep(0.1)