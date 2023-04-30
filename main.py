# MAKE A TIMER FOR HW


import pygame
import time
import random

from pygame.locals import *

# GLOBAL VARIABLES
COLOR = (255, 100, 98)
SURFACE_COLOR = (167, 255, 100)
WIDTH = 1000
HEIGHT = 500
starttime = time.time()


# Object class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(SURFACE_COLOR)
        self.image.set_colorkey(COLOR)

        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))

        self.rect = self.image.get_rect()


pygame.init()

RED = (255, 0, 0)
BLUE = (0, 0, 255)

size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Creating lemon soda sprite")
all_sprites_list = pygame.sprite.Group()
imp = pygame.image.load("C:\\Users\\saran_fecfs6i\\PycharmProjects\\website\\OBAMAMAMAM.jpg").convert()

object_ = Sprite(BLUE, 20, 30)
object_.rect.x = 100
object_.rect.y = 200

evil = Sprite(RED, 20, 30)
evil.rect.x = 0
evil.rect.y = 0

all_sprites_list.add(object_, evil)
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Cops and Robbers', RED, BLUE)
textRect = text.get_rect()
textRect.center = (WIDTH / 2, 20)
exit = True
clock = pygame.time.Clock()

while exit:
    for event in pygame.event.get():
        # if event.type == pygame.KEYDOWN:
        # 	if event.key == pygame.K_w:
        # 		object_.rect.y -= 10
        # 	if event.key == pygame.K_s:
        # 		object_.rect.y += 10
        # 	if event.key == pygame.K_a:
        # 		object_.rect.x += -10
        # 	if event.key == pygame.K_d:
        # 		object_.rect.x += 10
        if event.type == pygame.QUIT:
            exit = False
    screen.fill(SURFACE_COLOR)
    screen.blit(text, textRect)
    totaltime = round((time.time() - starttime), 2)
    if totaltime > 60:
        print("You lose")
    if pygame.key.get_pressed()[K_w]:
        if (object_.rect.y >= 0):
            object_.rect.y -= 5

    if pygame.key.get_pressed()[K_s]:
        if (object_.rect.y <= HEIGHT - 30):
            object_.rect.y += 5

    if pygame.key.get_pressed()[K_a]:
        if object_.rect.x >= 0:
                object_.rect.x -= 5

    if pygame.key.get_pressed()[K_d]:
        if (object_.rect.x <= WIDTH - 30):
             object_.rect.x += 5

    if pygame.key.get_pressed()[K_UP]:
        if (evil.rect.y >= 0):
            evil.rect.y -= 5

    if pygame.key.get_pressed()[K_DOWN]:
        if (evil.rect.y <= HEIGHT - 30):
            evil.rect.y += 5

    if pygame.key.get_pressed()[K_LEFT]:
        if (evil.rect.x >= 0):
            evil.rect.x -= 5

    if pygame.key.get_pressed()[K_RIGHT]:
        if (evil.rect.x <= WIDTH  -30):
            evil.rect.x += 5

    # this is now the next part for tfy

    # print((object_.rect.x))
    # print((evil.rect.x))

    all_sprites_list.update()
    if abs(object_.rect.x - evil.rect.x) < 20 and abs(object_.rect.y - evil.rect.y) < 20:
        print("YOUR DONE GAME OVERRRRRRRRRRRRRRRRRRRRRRRRR")
        screen.blit(imp, (500, 200))
        all_sprites_list.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        image_time = 0
        time.sleep(3)  # Sleep for 3 seconds
        exit(1)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)
    image_time = 0
