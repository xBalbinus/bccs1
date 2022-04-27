#This is the in-class notes for the final project:

import pygame

class Card:
    #constructor
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.faceup = True
        self.held = False

        front = pygame.image.load('./img/cards/' + rank + '_of_' + suit + '.png')
        front = pygame.transform.smoothscale(front, (140, 200))
        self.front = front
        back = pygame.image.load('./img/back-side.png')
        back = pygame.transform.smoothscale(back, (140, 200))
        self.back = back

        self.location = self.front.get_rect()

    def stage(self, scene):
        if self.faceup:
            scene.blit(self.front, self.location)
        else:
            scene.blit(self.back, self.location)

if __name__ == '__main__':
    
    pygame.init()

    scene = pygame.display.set_mode((1400,800))
    pygame.display.set_caption("Test code for cards")
    
    cards = []

    #pygame.mixer.music.load('music.mp3')

    #pygame.mixer.music.play()

    running = True

    #logo = pygame.image.load('logo.png')
    #logo_frame = logo.get_rect()

    while running:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    card = Card('diamonds', '10')
                    cards.append(card)
                elif event.key == pygame.K_c:
                    card = Card('hearts', '8')
                    cards.append(card)

        
        scene.fill([0,153,0])
        for card in cards:
            card.stage(scene)
        pygame.display.update()
    
#Event: the way your program interacts with the world (e.g. if someone presses a key in a game)

#Object oriented programming
#First determine what classes (aka. attributes) are for the object.

#e.g. with a card, you have the classes: suit, rank, color, shape, front / back, print?

#methods: flip card, draw card, stack card, move card to different pile