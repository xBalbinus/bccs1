import pygame
from notes import Card

class Pile:
    
    def __init__(self, x, y):
        
        self.stack = []
        self.top_visible = False
        
        self.location = pygame.Rect(x, y, 140, 200)
        
    def stage(self, scene):
        if len(self.stack) > 0:
            self.stack[-1].stage(scene)
        else:
            pygame.draw.rect(scene, [0, 53, 0], self.location)
            
    def touched(self, pos):
        return self.location.collidepoint(pos)
    
    def push(self, card):
        self.stack.append(card)
        card.location = self.location
        card.held = False

        
if __name__ == '__main__':
    
    pygame.init()

    scene = pygame.display.set_mode((1400,800))
    pygame.display.set_caption("Test code for cards")
    
    pile1 = Pile(100, 100)
    
    pile2 = Pile(400, 100)
    
    for suit in ['diamonds', 'clubs', 'hearts']:
        for rank in ['2', '4', '8']:
            card = Card(suit, rank)
            pile1.push(card)

    #pygame.mixer.music.load('music.mp3')

    #pygame.mixer.music.play()

    running = True

    #logo = pygame.image.load('logo.png')
    #logo_frame = logo.get_rect()

    while running:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False

        
        scene.fill([0,153,0])
        pile1.stage(scene)
        pile2.stage(scene)
        pygame.display.update()