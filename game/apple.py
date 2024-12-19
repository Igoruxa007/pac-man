from . game_object import GameObject


class Apple(GameObject):
    def __init__(self, topleft_x: int, topleft_y: int, sprite_filename: str):
        super().__init__(topleft_x, topleft_y, sprite_filename)
