# inisialisasi
import pygame
from random import randint
import time 

pygame.init()
screen = pygame.display.set_mode([600,500])
clock = pygame.time.Clock()
 
running = True
warna_bg = (255,255,255)
warna_bola = (0,0,255)

while running: # selama running bernilai True, ulangi proses
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill( warna_bg )   

    n = 1
    while n<30:
        pygame.draw.circle(screen,warna_bola, (randint(10,600), randint(10,500)),10)
        n +=1

    pygame.display.flip()
    time.sleep(1)

pygame.quit()
