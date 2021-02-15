import random


class Game:
    # this sets the dealer and player's cards for the game
    def __init__(self):
        self.card1_player = random.randint(1, 11)
        self.card2_player = random.randint(1, 11)
        self.card_sum_player = self.card1_player + self.card2_player
        self.card1_dealer = random.randint(1, 11)
        self.card2_dealer = random.randint(1, 11)
        self.card_sum_dealer = self.card1_dealer + self.card2_dealer

    # this function allows the player to either draw a card or not
    def draw(self):
        while True:
            if self.card_sum_player < 21:
                question = input('Hit or Stay? ').lower()
                if question == 'hit':
                    self.card_sum_player += random.randint(1, 11)
                    break
                elif question == 'stay':
                    return 'stay'
                    break
                else:
                    print('Unknown input, please try again.')

    # this function displays whether the player won or not
    def game_end(self, again_return):
        ending_code = {
            "2": "You Won!",
            "1": "You Lost!",
            "0": "Draw!"
        }
        if again_return == 2:
            ending_input = ending_code['2']
            print(ending_input)
        elif again_return == 1:
            ending_input = ending_code['1']
            print(ending_input)
        elif again_return == 0:
            ending_input = ending_code['0']
            print(ending_input)
        while True:
            message = input('Do you want to continue? (Y/N) ').lower()
            if message == 'y':
                self.renew()
                break
            elif message == 'n':
                return 'end'
                break
            else:
                print('Unknown input, please try again.')

    # this function is simple and just prints score of both player and dealer
    def score(self):
        print('Cards: %d' % self.card_sum_player)
        print("Dealer's Cards: %d" % self.card_sum_dealer)

    # this function 'renews' the values of cards
    def renew(self):
        self.card1_player = random.randint(1, 11)
        self.card2_player = random.randint(1, 11)
        self.card1_dealer = random.randint(1, 11)
        self.card2_dealer = random.randint(1, 11)
        self.card_sum_player = self.card1_player + self.card2_player
        self.card_sum_dealer = self.card1_dealer + self.card2_dealer


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
