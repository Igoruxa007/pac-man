import random
import pygame
from pygame.sprite import Group, spritecollide

from game.human import Human
from game.wall import Wall
from game.ghost import Ghost
from game.apple import Apple
from game.text import Text


def draw_whole_screen(screen: pygame.surface.Surface, score: int, *args: Human|Apple|Ghost|Group) -> None:
    screen.fill("blue")
    for arg in args:
        arg.draw(screen)
    Text(str(score), (10, 10)).draw(screen)



def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    running = True
    score = 0
    pacman = Human(screen.get_width() // 2, screen.get_height() // 2, "pacman")
    walls = Group(*[Wall(x, y, "brick") for (x, y) in Wall.calculate_walls_coordinates(screen.get_width(), screen.get_height(), 40, 40)])
    ghost = Ghost(200, 100, "monster")
    apple = Apple(200, 200, "apple")

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_whole_screen(screen, score, pacman, walls, ghost, apple)
        pygame.display.flip()
        pacman.move(walls)
        ghost.move(walls)

        if pacman.is_collided_with(apple):
            score += 1
            while apple.is_collided_with(pacman) or spritecollide(apple, walls, dokill=False):
                apple.rect.topleft = (
                    random.randint(Wall.width, screen.get_width() - Wall.width * 2),
                    random.randint(Wall.height, screen.get_height() - Wall.height * 2),
                )
        
        if pacman.is_collided_with(ghost):
            score = 0
            ghost.rect.topleft = (100, 100)
            apple.rect.topleft = (200, 200)
            pacman.rect.topleft = (screen.get_width() // 2, screen.get_height() // 2)

        clock.tick(60) / 1000

    pygame.quit()


if __name__ == "__main__":
    main()