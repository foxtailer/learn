import pygame
from pygame.locals import *
from sys import exit
import time

pygame.init()

screen = pygame.display.set_mode((640, 700), 0, 32)
font = pygame.font.SysFont("arial", 20)
copy_btn_main = pygame.image.load(r"../img/copy_.png").convert()
copy_btn_bright = pygame.image.load(r"../img/copy_.png").convert()
copy_btn_dark = pygame.image.load(r"../img/copy_.png").convert()

# Creates images with smooth gradients
def create_scales(height):
    red_scale_surface = pygame.surface.Surface((640, height))
    green_scale_surface = pygame.surface.Surface((640, height))
    blue_scale_surface = pygame.surface.Surface((640, height))
    
    for x in range(640):
        c = int((x/639.) * 255.)
        red = (c, 0, 0)
        green = (0, c, 0)
        blue = (0, 0, c)
        line_rect = Rect(x, 0, 1, height)
        pygame.draw.rect(red_scale_surface, red, line_rect)
        pygame.draw.rect(green_scale_surface, green, line_rect)
        pygame.draw.rect(blue_scale_surface, blue, line_rect)

    return red_scale_surface, green_scale_surface, blue_scale_surface


def darker_color(color, value=0.5):
    red, green, blue = color
    red = int(red*value)
    green = int(green*value)
    blue = int(blue*value)
    return red, green, blue


def brighter_color(color, value=1.5):
    red, green, blue = color
    red = int(min(red*value, 255))
    green = int(min(green*value, 255))
    blue = int(min(blue*value, 255))
    return red, green, blue


red_scale, green_scale, blue_scale = create_scales(80)
color = [127, 127, 127]

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    screen.fill((0, 0, 0))

    # Draw the scales to the screen
    screen.blit(red_scale, (0, 00))
    screen.blit(green_scale, (0, 80))
    screen.blit(blue_scale, (0, 160))
    x, y = pygame.mouse.get_pos()

    # If the mouse was pressed on one of the sliders, adjust the color component
    if pygame.mouse.get_pressed()[0]:
        for component in range(3):
            if y > component*80 and y < (component+1)*80:
                color[component] = int((x/639.)*255.)
                pygame.display.set_caption("PyGame Color Test - "+str(tuple(color)))
        
        # Check copy btn click
        if cbm.collidepoint(x,y):
            print("Main")
        if cbd.collidepoint(x,y):
            print("dark")
        if cbb.collidepoint(x,y):
            print("bright") 

    # Draw a circle for each slider to represent the currentsetting
    for component in range(3):
        pos = ( int((color[component]/255.)*639), component*80+40 )
        pygame.draw.circle(screen, (255, 255, 255), pos, 20)

    # Darker brighter areas
    pygame.draw.rect(screen, tuple(color), (170, 240, 300, 240))
    pygame.draw.rect(screen, darker_color(color), (0, 240, 170, 240))
    pygame.draw.rect(screen, brighter_color(color), (470, 240, 170, 240))   

    # Color captions
    main_color_text = font.render(str(tuple(color)), True, (0, 0, 0))
    darker_color_text = font.render(str(darker_color(color)), True, (0, 0, 0))
    brighter_color_text = font.render(str(brighter_color(color)), True, (0, 0, 0))

    screen.blit(main_color_text, (250, 245))
    screen.blit(darker_color_text, (25, 245))
    screen.blit(brighter_color_text, (495, 245))

    # Blit copy_buttons
    cbm = Rect((440,242), (29,30))
    cbd = Rect((140,242), (29,30))
    cbb = Rect((615,242), (29,30))
    screen.blit(copy_btn_main, (440,242))
    screen.blit(copy_btn_dark, (140,242))
    screen.blit(copy_btn_bright, (615,242))

    # Lerp areas
    pygame.draw.rect(screen, (255, 255, 255), (0, 480, 640, 50))
    pygame.draw.rect(screen, (0,100,0), (0, 530, 170, 240))
    pygame.draw.rect(screen, (100,0,0), (170, 530, 300, 240))
    pygame.draw.rect(screen, (20,40,40), (470, 530, 170, 240))

    pygame.display.update()
    time.sleep(0.1)