#This is the in-class notes for the final project:

import pygame

pygame.init()

scene = pygame.display.set_mode((1400,800))
pygame.display.set_caption("My new caption!")

pygame.mixer.music.load('music.mp3')

pygame.mixer.music.play()

running = True

logo = pygame.image.load('logo.png')
logo_frame = logo.get_rect()

while running:
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False

    
    scene.fill([0,153,0])
    scene.blit(logo, logo_frame)
    
    pygame.display.update()
    
#Event: the way your program interacts with the world (e.g. if someone presses a key in a game)
