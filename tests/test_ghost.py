from pygame.sprite import Group

from game.ghost import Ghost
from game.wall import Wall

def test_Ghost_move():
    walls = Group(*[Wall(x, y, "brick") for (x, y) in Wall.calculate_walls_coordinates(640, 480, 40, 40)])
    ghost = Ghost(100, 100, "monster")

    ghost.move(walls)

    assert ghost.rect == (106, 100, 40, 40)

def test_Ghost_move_to_wall():
    walls = Group(*[Wall(x, y, "brick") for (x, y) in Wall.calculate_walls_coordinates(640, 480, 40, 40)])
    ghost = Ghost(560, 100, "monster")

    ghost.move(walls)

    assert ghost.rect != (506, 100, 40, 40)