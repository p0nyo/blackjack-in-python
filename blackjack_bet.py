import random


class Game:

    def __init__(self):
        self.card1_player = random.randint(1, 11)
        self.card2_player = random.randint(1, 11)
        self.card_sum_player = self.card1_player + self.card2_player
        self.card1_dealer = random.randint(1, 11)
        self.card2_dealer = random.randint(1, 11)
        self.card_sum_dealer = self.card1_dealer + self.card2_dealer

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

    def renew(self):
        self.card1_player = random.randint(1, 11)
        self.card2_player = random.randint(1, 11)
        self.card1_dealer = random.randint(1, 11)
        self.card2_dealer = random.randint(1, 11)
        self.card_sum_player = self.card1_player + self.card2_player
        self.card_sum_dealer = self.card1_dealer + self.card2_dealer

    def score(self):
        print('Cards: %d' % self.card_sum_player)
        print("Dealer's Cards: %d" % self.card_sum_dealer)

    # def money(self):


def main():
    game = Game()
    while True:
        print('Cards: %d' % game.card_sum_player)
        if game.draw() == 'stay':  #NOTE when stay is called
            if game.card_sum_player > game.card_sum_dealer:
                game.score()
                if game.game_end(2) == 'end':  #NOTE win
                    break
            elif game.card_sum_player < game.card_sum_dealer:
                if game.game_end(1) == 'end':  #NOTE lose
                    break
            elif game.card_sum_player == game.card_sum_dealer:
                if game.game_end(0) == 'end':  #NOTE draw
                    break
        if game.card_sum_player > 21:
            game.score()
            game.game_end(1)
            if game.game_end(0) == 4:
                break
        elif game.card_sum_player == 21:
            game.score()
            game.game_end(2)
            if game.game_end(0) == 4:
                break


if __name__ == '__main__':
    main()
