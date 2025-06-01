import sys

from config import *
from for_test import MyCounter


screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

counter = MyCounter((400, 50), (50, 50), 0)
counter2 = MyCounter((400, 200), (50, 50), 100)


while True:
    
    screen.fill((240, 240, 240))
    counter.draw(screen)
    counter2.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        mouse_held = False
        mouse_held2 = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if counter.is_clicked(event.pos):
                mouse_held = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_held = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if counter2.is_clicked(event.pos):
                mouse_held2 = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_held2 = False

    if mouse_held:
        counter.back() 
    if mouse_held2:
        counter2.back() 

    counter.update()
    counter2.update()

    pygame.display.flip()
    clock.tick(60)
    