import pygame

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

        self.rect = (self.x, self.y, self.WIDTH, self.HEIGHT)

def redrawWindow(win, player):

    win.fill((255, 255, 255))
    player.draw(win)
    pygame.display.update()

def main():

    run = True
    p = Player(50, 50, 100, 100, (0, 255, 0))

    clock = pygame.time.Clock()


    while run:
        clock.tick(60)
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                run = False
                pygame.quit()
                exit()
        
        p.move()
        redrawWindow(win, p)

main()