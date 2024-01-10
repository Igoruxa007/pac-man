import pygame
from pygame.sprite import Group, spritecollide

from . game_object import GameObject
from . settings import PLAYER_SPEED

class Human(GameObject):
    def __init__(self, topleft_x: int, topleft_y: int, sprite_filename: str):
        super().__init__(topleft_x, topleft_y, sprite_filename)
        self.player_speed = PLAYER_SPEED

    def move(self, walls: Group) -> None:
        keys = pygame.key.get_pressed()

        old_player_topleft = self.rect.topleft
        if keys[pygame.K_w]:
            self.rect = self.rect.move(0, -1 * self.player_speed)
        if keys[pygame.K_s]:
            self.rect = self.rect.move(0, self.player_speed)
        if keys[pygame.K_a]:
            self.rect = self.rect.move(-1 * self.player_speed, 0)
        if keys[pygame.K_d]:
            self.rect = self.rect.move(self.player_speed, 0)

        if spritecollide(self, walls, dokill=False):
            self.rect.topleft = old_player_topleft
