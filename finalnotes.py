#This is the in-class notes for designing Solitaire

import random
import pygame  

class Pile:
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
            
    def touched(self, pos):
        return self.location.collidepoints(pos)
    
    def shuffle(self):
        random.shuffle(self.stack)
    
    def push(self,card):
        self.stack.append(card)
        card.location = self.location
        card.held = False
        
    def pop(self):
        if len(self.stack) > 0:
            card = self.stack.pop()
            card.location = self.location.copy()
            card.held = True
            return card
    
    def react(self, event, clock):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.touched(event.pos):
                if clock.tick() < 500:
                    self.faceup = not self.faceup
                else:
                    self.held = True
        
        elif event.type == pygame.MOUSEBUTTONUP:
            if self.touched(event.pos):
                self.held = False
        
        elif event.type == pygame.MOUSEMOTION:
            if self.held:
                self.location.move_ip(event.rel)

if __name__ == '__main__':
    
    pygame.init()

    scene = pygame.display.set_mode((1400,800))
    pygame.display.set_caption("Test code for cards")
    
    clock = pygame.time.Clock()
    
    pile1 = Pile(100,100)
    
    for suit in ['diamonds', 'clubs', 'hearts']:
        for rank in ['2', '4', '8']:
            card = Pile(suit, rank)
            pile1.push(card)
            
    pile1.shuffle()
    
    pile2 = Pile(400, 100)
    
    

            
    
    card = None

    #pygame.mixer.music.load('music.mp3')

    #pygame.mixer.music.play()

    running = True

    #logo = pygame.image.load('logo.png')
    #logo_frame = logo.get_rect()

    while running:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pile1.touched(event.pos):
                    card = pile1.pop()
                    
            elif event.type == pygame.MOUSEBUTTONUP:
                if card:
                    if pile2.touched(event.pos):
                        pile2.push(card)
                        card = None
                    else:
                        pile1.push(card)
                        card = None
                    
            if card:
                card.react(event, clock)

        
        scene.fill([0,153,0])
        pile1.stage(scene)
        pile2.stage(scene)
        if card:
            card.stage(scene)
        pygame.display.update()
        
    
#Event: the way your program interacts with the world (e.g. if someone presses a key in a game)

#Object oriented programming
#First determine what classes (aka. attributes) are for the object.

#e.g. with a card, you have the classes: suit, rank, color, shape, front / back, print?

#methods: flip card, draw card, stack card, move card to different pile

#we also want multiple stacks of cards.
#location attribute
#pop, flip, push, shuffle, test (if card is in)