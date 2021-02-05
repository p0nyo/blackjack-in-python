import random

player = 0
dealer = 0
deck = [
    1, 1, 1, 1,
    2, 2, 2, 2,
    3, 3, 3, 3,
    4, 4, 4, 4,
    5, 5, 5, 5,
    6, 6, 6, 6,
    7, 7, 7, 7,
    8, 8, 8, 8,
    9, 9, 9, 9,
    10, 10, 10, 10,
    11, 11, 11, 11,
    12, 12, 12, 12,
    13, 13, 13, 13
]
while True:
    question = input('Hit or Stay? ').lower()
    if question == 'hit':
        card_player = random.choice(deck)
        card_dealer = random.choice(deck)
        deck.remove(card_player)
        deck.remove(card_dealer)
        player += card_player
        dealer += card_dealer
        print(f'You have {player}')
        # print(f'Dealer has {dealer}')
        if player > 21:
            print('You Lost!')
            break
        elif player == 21 and player == dealer:

    elif question == 'stay':
        if player == 21:
            print('You Won!')
        elif player == 21 and player == dealer:
            print('Tie')
        elif player > dealer:
            print('You Won!')
        elif player == dealer:
            print('Tie')
        elif player < dealer:
            print('You lost!')
