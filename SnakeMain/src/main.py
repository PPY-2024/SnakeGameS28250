import pygame
from game import Game
from src.mongoDB import init_database_from_mongo


def get_user_input():
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("Snake Game Setup")
    font = pygame.font.Font(None, 32)
    label_font = pygame.font.Font(None, 24)

    input_box_name = pygame.Rect(100, 120, 200, 32)
    input_box_size = pygame.Rect(100, 200, 200, 32)

    active_name = False
    active_size = False
    player_name = ''
    board_size = ''
    done = False

    while not done:
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box_name.collidepoint(event.pos):
                    active_name = not active_name
                else:
                    active_name = False

                if input_box_size.collidepoint(event.pos):
                    active_size = not active_size
                else:
                    active_size = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if active_name:
                        active_name = False
                    elif active_size:
                        active_size = False
                        done = True
                elif event.key == pygame.K_BACKSPACE:
                    if active_name:
                        player_name = player_name[:-1]
                    elif active_size:
                        board_size = board_size[:-1]
                else:
                    if active_name:
                        player_name += event.unicode
                    elif active_size:
                        board_size += event.unicode

            if event.type == pygame.QUIT:
                pygame.quit()
                return None, None

        screen.fill((30, 30, 30))

        label_name = label_font.render("Enter Player Name:", True, (255, 255, 255))
        label_size = label_font.render("Enter Board Size (NxN):", True, (255, 255, 255))
        screen.blit(label_name, (input_box_name.x, input_box_name.y - 30))
        screen.blit(label_size, (input_box_size.x, input_box_size.y - 30))

        txt_surface_name = font.render(player_name, True, (255, 255, 255))
        txt_surface_size = font.render(board_size, True, (255, 255, 255))
        screen.blit(txt_surface_name, (input_box_name.x + 5, input_box_name.y + 5))
        screen.blit(txt_surface_size, (input_box_size.x + 5, input_box_size.y + 5))
        pygame.draw.rect(screen, (255, 255, 255), input_box_name, 2)
        pygame.draw.rect(screen, (255, 255, 255), input_box_size, 2)

        pygame.display.flip()

    return player_name, board_size


def main():
    init_database_from_mongo()
    player_name, board_size = get_user_input()
    if player_name is None or board_size is None:
        print("cancelled")
        return

    board_size = board_size.split('x')
    if len(board_size) == 2 and board_size[0].isdigit() and board_size[1].isdigit():
        width = int(board_size[0])
        height = int(board_size[1])
        if 5 <= width <= 25 and 5 <= height <= 25:
            game = Game(width, height, player_name)
            game.run()
        else:
            print("min 5x5, max 25x25")
    else:
        print("invalid format")


main()
