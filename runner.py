import pygame
import sys
import time

import tictactoe as ttt

pygame.init()
size = width, height = 750, 550

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)
blue = (60, 0, 60)
red = (100, 0, 0)

screen = pygame.display.set_mode(size)

smallFont = pygame.font.Font("Writterine-Regular.ttf", 25)
middleFont = pygame.font.Font("Writterine-Regular.ttf", 28)
bigFont = pygame.font.Font("Writterine-Regular.ttf", 50)
largeFont = pygame.font.Font("Writterine-Regular.ttf", 85)
moveFont = pygame.font.Font("Writterine-Regular.ttf", 110)

user = None
board = ttt.initial_state()
ai_turn = False

# Завантаження зображення фону
background_image = pygame.image.load("background_image.jpg").convert()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Відображення зображення фону
    screen.blit(background_image, (0, 0))

    # Let user choose a player.
    if user is None:

        # Draw title
        title = largeFont.render("Play Tic-Tac-Toe", True, black)
        title2 = smallFont.render("https://github.com/ArtemLeo/python-game-tic-tac-toe", True, black)
        titleRect = title.get_rect()
        titleRect2 = title.get_rect()
        titleRect.center = ((width / 2), 180)
        titleRect2.center = ((width / 2), 270)
        screen.blit(title, titleRect)
        screen.blit(title2, titleRect2)

        # Draw buttons
        playXButton = pygame.Rect((width / 5), (height / 2) + 100, width / 5, 50)
        playX = middleFont.render("Play as X", True, white)
        playXRect = playX.get_rect()
        playXRect.center = playXButton.center
        pygame.draw.rect(screen, black, playXButton)
        screen.blit(playX, playXRect)

        playOButton = pygame.Rect(5 * (width / 8), (height / 2) + 100, width / 5, 50)
        playO = middleFont.render("Play as O", True, white)
        playORect = playO.get_rect()
        playORect.center = playOButton.center
        pygame.draw.rect(screen, black, playOButton)
        screen.blit(playO, playORect)

        # Check if button is clicked
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            mouse = pygame.mouse.get_pos()
            if playXButton.collidepoint(mouse):
                time.sleep(0.2)
                user = ttt.X
            elif playOButton.collidepoint(mouse):
                time.sleep(0.2)
                user = ttt.O

    else:

        # Draw game board
        tile_size = 130
        tile_origin = (width / 2 - (1.5 * tile_size),
                       height / 2 - (1.5 * tile_size))
        tiles = []
        for i in range(3):
            row = []
            for j in range(3):
                rect = pygame.Rect(
                    tile_origin[0] + j * tile_size,
                    tile_origin[1] + i * tile_size,
                    tile_size, tile_size
                )
                pygame.draw.rect(screen, white, rect, 2)

                if board[i][j] != ttt.EMPTY:
                    move = moveFont.render(board[i][j], True, yellow)
                    moveRect = move.get_rect()
                    moveRect.center = rect.center
                    screen.blit(move, moveRect)
                row.append(rect)
            tiles.append(row)

        game_over = ttt.terminal(board)
        player = ttt.player(board)

        # Show title
        if game_over:
            winner = ttt.winner(board)
            if winner is None:
                title = f"Game Over: Tie."
            else:
                title = f"Game Over: {winner} wins."
        elif user == player:
            title = f"Play as {user}"
        else:
            title = f"Computer thinking..."
        title = bigFont.render(title, True, black)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 40)
        screen.blit(title, titleRect)

        # Check for AI move
        if user != player and not game_over:
            if ai_turn:
                time.sleep(0.5)
                move = ttt.minimax(board)
                board = ttt.result(board, move)
                ai_turn = False
            else:
                ai_turn = True

        # Check for a user move
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1 and user == player and not game_over:
            mouse = pygame.mouse.get_pos()
            for i in range(3):
                for j in range(3):
                    if board[i][j] == ttt.EMPTY and tiles[i][j].collidepoint(mouse):
                        board = ttt.result(board, (i, j))

        if game_over:
            againButton = pygame.Rect(width / 3, height - 65, width / 3, 45)
            again = middleFont.render("Play Again ...", True, white)
            againRect = again.get_rect()
            againRect.center = againButton.center
            pygame.draw.rect(screen, black, againButton)
            screen.blit(again, againRect)
            click, _, _ = pygame.mouse.get_pressed()
            if click == 1:
                mouse = pygame.mouse.get_pos()
                if againButton.collidepoint(mouse):
                    time.sleep(0.2)
                    user = None
                    board = ttt.initial_state()
                    ai_turn = False

    pygame.display.flip()
