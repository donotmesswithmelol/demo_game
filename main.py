import pygame
import random
from pygame.locals import *
# GLOBAL VARIABLES
COLOR = (255, 100, 98)
SURFACE_COLOR = (167, 255, 100)
WIDTH = 1000
HEIGHT = 500

# Object class
class Sprite(pygame.sprite.Sprite):
	def __init__(self, color, height, width):
		super().__init__()

		self.image = pygame.Surface([width, height])
		self.image.fill(SURFACE_COLOR)
		self.image.set_colorkey(COLOR)

		pygame.draw.rect(self.image,color,pygame.Rect(0, 0, width, height))

		self.rect = self.image.get_rect()


pygame.init()

RED = (255, 0, 0)
BLUE = (0,0,255)

size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Creating lemon soda sprite")

all_sprites_list = pygame.sprite.Group()

object_ = Sprite(BLUE, 20, 30)
object_.rect.x = 200
object_.rect.y = 1

evil = Sprite(RED, 20, 30)
evil.rect.x = 200
evil.rect.y = 1

all_sprites_list.add(object_,evil)

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
	if pygame.key.get_pressed()[K_w]:
		object_.rect.y -= 5

	if pygame.key.get_pressed()[K_s]:
		object_.rect.y += 5

	if pygame.key.get_pressed()[K_a]:
		object_.rect.x -= 5

	if pygame.key.get_pressed()[K_d]:
		object_.rect.x += 5

	if pygame.key.get_pressed()[K_UP]:
		evil.rect.y -= 5

	if pygame.key.get_pressed()[K_DOWN]:
		evil.rect.y += 5

	if pygame.key.get_pressed()[K_LEFT]:
		evil.rect.x -= 5

	if pygame.key.get_pressed()[K_RIGHT]:
		evil.rect.x += 5



	all_sprites_list.update()
	screen.fill(SURFACE_COLOR)
	all_sprites_list.draw(screen)
	pygame.display.flip()
	clock.tick(60)


pygame.quit()
