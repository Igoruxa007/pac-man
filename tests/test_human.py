from game.human import Human
from game.apple import Apple

def test_Human_collided_with_apple():
    human = Human(300, 300, "pacman")
    apple = Apple(300, 300, "apple")

    assert human.is_collided_with(apple) is True