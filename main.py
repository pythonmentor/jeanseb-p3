import os

import pygame

from Game import Game


def main():
    running = True
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('The Hack Lab')
    pygame.mouse.set_visible(0)
    game_folder = os.path.dirname(__file__)
    print(game_folder)
    img_folder = os.path.join(game_folder, "assets")
    print(img_folder)
    background = pygame.image.load(os.path.join(img_folder, "bg.jpg"))
    while running:
        screen.blit(background, (0, 0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    # game = Game()
    # game.initialize()
    # game.launch()


if __name__ == '__main__':
    main()
