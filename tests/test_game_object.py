from game.game_object import GameObject

def test_GameObject_collided():
    object_1 = GameObject(200, 200, "apple")
    object_2 = GameObject(200, 200, "apple")

    assert object_1.is_collided_with(object_2) is True 