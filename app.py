from utils import Game


def main():
    game = Game()
    while True:
        print('Cards: %d' % game.card_sum_player)
        if game.draw() == 'stay':  # when stay is called from the game.draw() function
            if game.card_sum_player > game.card_sum_dealer:  # the condition for winning after staying
                game.score()
                if game.game_end(2) == 'end':
                    break
            elif game.card_sum_player < game.card_sum_dealer:  # the condition for losing after staying
                if game.game_end(1) == 'end':
                    break
            elif game.card_sum_player == game.card_sum_dealer:  # the condition for a draw after staying
                break
        if game.card_sum_player > 21:  # if exceeds 21 then lost
            game.score()
            if game.game_end(1) == 'end':
                break
        elif game.card_sum_player == 21:  # if is 21 then win
            if game.card_sum_dealer == 21:  # unless dealer also gets 21
                if game.game_end(0) == 'end':
                    break
            game.score()
            if game.game_end(2) == 'end':
                break


if __name__ == '__main__':
    main()
