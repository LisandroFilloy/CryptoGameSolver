from crypto import solve_game, shuffle

if __name__ == '__main__':

    for _ in range(10):
        card1, card2, card3, card4 = shuffle()
        print(card1, card2, card3, card4)
        print(solve_game(card1, card2, card3, card4), '\n')