# Import and initialize the pygame library
import pygame
from crypto_solver import shuffle, solve_game
import time


# Colors
BLUE = (0, 0, 200)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)

# Create game
pygame.init()
screen_size = width, height = 500, 500
screen = pygame.display.set_mode(screen_size)

# Fonts
LARGE_FONT = pygame.font.Font(pygame.font.get_default_font(), 70)
SMALL_FONT = pygame.font.Font(pygame.font.get_default_font(), 20)

# Cards and numbers positions
card_target_text = LARGE_FONT.render(f'{e}', True, BLACK)
card_target_text_pos = card_target_text.get_rect()
card_target_text_pos.center = (width/2, 60)
card_target_pos = pygame.Rect((0, 0), (80, 90))
card_target_pos.center = card_target_text_pos.center

card_1_text = LARGE_FONT.render(f'{a}', True, BLUE)
card_1_text_pos = card_1_text.get_rect()
card_1_text_pos.center = (205, 180)
card_1_pos = pygame.Rect((0, 0), (80, 90))
card_1_pos.center = card_1_text_pos.center

card_2_text = LARGE_FONT.render(f'{b}', True, BLUE)
card_2_text_pos = card_2_text.get_rect()
card_2_text_pos.center = (295, 180)
card_2_pos = pygame.Rect((0, 0), (80, 90))
card_2_pos.center = card_2_text_pos.center

card_3_text = LARGE_FONT.render(f'{c}', True, BLUE)
card_3_text_pos = card_3_text.get_rect()
card_3_text_pos.center = (205, 280)
card_3_pos = pygame.Rect((0, 0), (80, 90))
card_3_pos.center = card_3_text_pos.center

card_4_text = LARGE_FONT.render(f'{d}', True, BLUE)
card_4_text_pos = card_4_text.get_rect()
card_4_text_pos.center = (295, 280)
card_4_pos = pygame.Rect((0, 0), (80, 90))
card_4_pos.center = card_4_text_pos.center

cards_pos_list = [card_1_pos, card_2_pos, card_3_pos, card_4_pos]

ops_pos_list = []

# Generate 5 values that have
a, b, c, d, e = shuffle(12)
while not (solve_game(a, b, c, d, target=e) and solve_game(a, b, c, d, target=24)):
    a, b, c, d, e = shuffle(12)

main_menu = True
crypto_game = False
twenty_four_game = False

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with black
    screen.fill(BLACK)

    if main_menu:
        # Crypto game button
        crypto_button_text = LARGE_FONT.render('Play Crypto', True, BLACK)
        crypto_button_rect = crypto_button_text.get_rect()
        crypto_button_rect.center = (width/2, 1/3 * height)
        pygame.draw.rect(screen, WHITE, crypto_button_rect)
        screen.blit(crypto_button_text, crypto_button_rect)

        # 24 game button
        twenty_four_button_text = LARGE_FONT.render('Play 24', True, BLACK)
        twenty_four_button_rect = twenty_four_button_text.get_rect()
        twenty_four_button_rect.center = (width / 2, 2/3 * height)
        pygame.draw.rect(screen, WHITE, twenty_four_button_rect)
        screen.blit(twenty_four_button_text, twenty_four_button_rect)

        # Check if any button was pressed
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            mouse = pygame.mouse.get_pos()
            if crypto_button_rect.collidepoint(mouse):
                time.sleep(0.3)
                pygame.event.get()

                main_menu = False

                crypto_game = True

            elif twenty_four_button_rect.collidepoint(mouse):
                time.sleep(0.3)
                pygame.event.get()
                main_menu = False

                twenty_four_game = True

    if crypto_game or twenty_four_game:

        if twenty_four_game:
            e = 24

        operations_sequence = []

        card_1_color = WHITE if card_1_pos in cards_pos_list else GREEN
        card_2_color = WHITE if card_2_pos in cards_pos_list else GREEN
        card_3_color = WHITE if card_3_pos in cards_pos_list else GREEN
        card_4_color = WHITE if card_4_pos in cards_pos_list else GREEN

        # Plot target Card
        pygame.draw.rect(screen, WHITE, card_target_pos)
        screen.blit(card_target_text, card_target_text_pos)

        # Plot Cards

        pygame.draw.rect(screen, card_1_color, card_1_pos)
        screen.blit(card_1_text, card_1_text_pos)

        pygame.draw.rect(screen, card_2_color, card_2_pos)
        screen.blit(card_2_text, card_2_text_pos)

        pygame.draw.rect(screen, card_3_color, card_3_pos)
        screen.blit(card_3_text, card_3_text_pos)

        pygame.draw.rect(screen, card_4_color, card_4_pos)
        screen.blit(card_4_text, card_4_text_pos)

        # Addition operation
        # TODO

        # Subtraction operation
        # TODO

        # Division operation
        # TODO

        # Multiplication operator
        # TODO

        # Button pressing routine
        click, _, _ = pygame.mouse.get_pressed()
        if click:
            mouse = pygame.mouse.get_pos()
            for card in cards_pos_list:
                if card.collidepoint(mouse):
                    if card == card_1_pos:
                        cards_pos_list.remove(card_1_pos)
                        break
                    if card == card_2_pos:
                        cards_pos_list.remove(card_2_pos)
                        break
                    if card == card_3_pos:
                        cards_pos_list.remove(card_3_pos)
                        break
                    if card == card_4_pos:
                        cards_pos_list.remove(card_4_pos)
                        break

        if len(cards_pos_list) == 0:
            crypto_game = False
            twenty_four_game = False
            final_answer = True


    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()


# NEED TO DRAW OPERATION SIGNS
