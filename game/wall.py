from . game_object import GameObject


class Wall(GameObject):
    def __init__(self, topleft_x: int, topleft_y: int, sprite_filename: str):
        super().__init__(topleft_x, topleft_y, sprite_filename)

    @staticmethod
    def calculate_walls_coordinates(screen_width: int, screen_height: int, block_width: int, block_height: int) -> list[tuple[int, int]]:
        horizontal_wall_blocks_amount = screen_width // block_width
        vertical_wall_blocks_amount = screen_height // block_height - 2

        walls_coordinates = []
        for block_num in range(horizontal_wall_blocks_amount):
            walls_coordinates.extend([
                (block_num * block_width, 0),
                (block_num * block_width, screen_height - block_height),
            ])
        for block_num in range(1, vertical_wall_blocks_amount + 1):
            walls_coordinates.extend([
                (0, block_num * block_height),
                (screen_width - block_width, block_num * block_height),
            ])

        coordinates = [
            (8, 1),
            (8, 10),
            (1, 6),
            (14, 6),
        ]
        for coordinate in coordinates:
            walls_coordinates.append(
                (coordinate[0] * block_width, coordinate[1] * block_height)
            )

        return walls_coordinates
