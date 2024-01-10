from random import choice
from pygame.sprite import Group, spritecollide

from . game_object import GameObject
from . settings import GHOST_SPEED

class Ghost(GameObject):
    def __init__(self, topleft_x: int, topleft_y: int, sprite_filename: str):
        super().__init__(topleft_x, topleft_y, sprite_filename)
        self.ghost_speed = GHOST_SPEED
        self.direction = (1, 0)
    
    def change_direction(self) -> None:
        x = choice([-1, 0, 1])
        if x:
            y = choice([-1, 0, 1])
        else:
            y = choice([-1, 1])
        self.direction = (x, y)

    def move(self, walls: Group) -> None:
        old_ghost_topleft = self.rect.topleft
        self.rect = self.rect.move(self.direction[0] * self.ghost_speed, self.direction[1] * self.ghost_speed)

        if spritecollide(self, walls, dokill=False):
            self.rect.topleft = old_ghost_topleft
            self.change_direction()
            self.move(walls)