import pygame

class Ship:
	"""A class to manage the space ship."""

	def __init__(self, ai_game):
		"""Initialize the ship and set its starting position."""
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		# Load the ship image and get its rect.
		# Pygame lets you treat all game elements as rectangles
		# Resize image to fit screen
		self.image = pygame.image.load('images/rocket.bmp')
		self.image = pygame.transform.scale(self.image, (30, 50))
		self.rect = self.image.get_rect()

		# Start each new ship at bottom center of the screen.
		self.rect.midbottom = self.screen_rect.midbottom

		# Store a decimal value for ship's horizontal position
		self.x = float(self.rect.x)

		# Movement flag
		self.moving_right = False
		self.moving_left = False

	def update(self):
		"""Update the ship's position based on movement flag."""
		# Update the ship's value not the rect
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed

		# Update rect object from self.x
		self.rect.x = self.x

	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)