import sys
import os
import pygame

from settings import Settings
from ship import Ship

print(os.getcwd())

class AlienInvasion:
	"""Overall class to manage game assets and behavior."""

	def __init__(self):
		"""Initialize game and create game resources."""
		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption('Alien Invasion')

		self.ship = Ship(self)


	def run_game(self):
		"""Start the main loop for the game."""

		while True:
			# single leading underscore indicates helper method
			self._check_events()
			self._update_screen()

	def _check_events(self):
		"""Respond to keyphrases and mouse events."""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

	def _update_screen(self):
		"""Update images on the screen and flip to the new screen."""
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()

		pygame.display.flip()

if __name__ == '__main__':
	# Make a game instance and run the game
	ai = AlienInvasion()
	ai.run_game()
