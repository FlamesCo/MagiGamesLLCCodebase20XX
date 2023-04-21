import pygame
import random

# initialize pygame
pygame.init()

# set window size
window_width = 800
window_height = 600

# set window title
pygame.display.set_caption("Harry Potter vs AVGN")

# create the game window
game_window = pygame.display.set_mode((window_width, window_height))

# set the background color
background_color = (0, 0, 0)

# define the colors
black = (0, 0, 0)
white = (255, 255, 255)

# set the font
font = pygame.font.SysFont('comicsans', 30)

# create the player and enemy objects
class Player:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.vel = 5
        self.health = 100
    
    def draw(self, game_window):
        pygame.draw.rect(game_window, self.color, (self.x, self.y, self.width, self.height))

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

class Enemy:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.vel = 5
        self.health = 100
    
    def draw(self, game_window):
        pygame.draw.rect(game_window, self.color, (self.x, self.y, self.width, self.height))

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

# create the player and the enemy
player = Player(300, 500, 40, 40, white)
enemy = Enemy(300, 50, 40, 40, white)

# create the spell list
spells = ['toontoon-emu']

# create the game loop
game_loop = True
while game_loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False
    
    # draw the background
    game_window.fill(background_color)

    # draw the player and enemy
    player.draw(game_window)
    enemy.draw(game_window)

    # move the player and the enemy
    player.move()
    enemy.move()

    # draw the spell list
    pygame.draw.rect(game_window, white, (50, 500, 200, 50))
    text = font.render("Spells: ", True, black)
    game_window.blit(text, (50, 500))
    for i, spell in enumerate(spells):
        text = font.render(spell, True, black)
        game_window.blit(text, (50 + i * 20, 530))

    # calculate the distance between the player and the enemy
    dist = ((player.x - enemy.x) ** 2 + (player.y - enemy.y) ** 2) ** 0.5

    # draw the distance on the screen
    text = font.render('Distance: ' + str(int(dist)), True, white)
    game_window.blit(text, (50, 550))

    # cast the spell when the player is close enough to the enemy
    if dist < 50:
        if 'toontoon-emu' in spells:
            spells.remove('toontoon-emu')
            enemy.health -= random.randint(20, 50)

    # update the screen
    pygame.display.update()

# exit the game
pygame.quit()
