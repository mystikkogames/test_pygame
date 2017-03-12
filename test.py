#!/usr/bin/env python

import pygame
from pygame.locals import *

def main():
	pygame.init()
	pygame.mixer.init()
	s = pygame.display.set_mode((500, 500))
	pygame.display.set_caption('test')	
	bg = pygame.Surface(s.get_size())
	bg = bg.convert()
	x, dx = 0, 1
	try:
		pygame.mixer.music.load('test.wav')
		pygame.mixer.music.play(-1)
	except pygame.error, message:
		print message		
	while 1:
		for e in pygame.event.get():
			if e.type == QUIT: return	
		bg.fill((0, 0, 0))
		x += dx
		dx = -dx if x < 0 or x > 450 else dx
		pygame.draw.rect(bg, (255, 255, 255), (x, 250, 50, 50))
		s.blit(bg, (0, 0))
		pygame.display.flip()
		
if __name__ == '__main__':
	main()
	pygame.mixer.quit()
	pygame.quit()
