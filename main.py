import pygame
from network import Network

WIDTH = 500
HEIGHT = 500

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Client')

clientNumber = 0

class Player():
    def __init__(self, x, y, WIDTH, HEIGHT, color):

        self.x = x
        self.y = y
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.color = color
        self.rect = (x, y, WIDTH, HEIGHT)
        self.vel = 3

    def draw(self, win):

        pygame.draw.rect(win, self.color, self.rect)

    def move(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.x -= self.vel

        if keys[pygame.K_d]:
            self.x += self.vel

        if keys[pygame.K_w]:
            self.y -= self.vel

        if keys[pygame.K_s]:
            self.y += self.vel

        self.update()

    def update(self):

        self.rect = (self.x, self.y, self.WIDTH, self.HEIGHT)

def read_pos(str):
    str = str.split(',')
    return int(str[0]), int(str[1])

def make_pos(tup):
    return str(tup[0]) + ',' + str(tup[1])

def redrawWindow(win, player, player2):

    win.fill((255, 255, 255))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()

def main():

    run = True
    n = Network()
    startPos = read_pos(n.getPos())
    p = Player(startPos[0], startPos[1], 100, 100, (0, 255, 0))
    p2 = Player(0, 0, 100, 100, (255, 0, 0))
    p2.update()

    clock = pygame.time.Clock()


    while run:
        clock.tick(60)

        p2Pos = n.send(make_pos((p.x, p.y)))
        p2.x = p2Pos[0]
        p2.y = p2Pos[1]

        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                run = False
                pygame.quit()
                exit()
        
        p.move()
        redrawWindow(win, p, p2)

main()