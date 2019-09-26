import pygame

class Ship:
	"""A class to manage the space ship."""

	def __init__(self, ai_game):
		"""Initialize the ship and set its starting position."""
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()

		# Load the ship image and get its rect.
		# Pygame lets you treat all game elements as rectangles
		# Resize image to fit screen
		self.image = pygame.image.load('images/rocket.bmp')
		self.image = pygame.transform.scale(self.image, (50, 30))
		self.rect = self.image.get_rect()

		# Start each new ship at bottom center of the screen.
		self.rect.midbottom = self.screen_rect.midbottom


	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)