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
        player += card_player
        if dealer < 17:
            deck.remove(card_dealer)
            dealer += card_dealer
        elif 19 > dealer > 17:
            dealer_choice = random.randint(1, 2)
            if dealer_choice == 1:
                deck.remove(card_dealer)
                dealer += card_dealer
                if dealer > 21:
                    
            elif dealer_choice == 2:
                new_dealer = dealer
                
        print(f'You have {player}')
        print(f'Dealer has {dealer}')
        if player > 21:
            print('You Lost!')
            ans1 = input('Do you want to continue? (Y/N) ').lower()
            if ans1 == 'y':
                None
            elif ans1 == 'n':
                break
            else:
                print('Error, please try again.')
                None
        elif player == 21 and player == dealer:
            print('tie')
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
    else:
        print('Error, please try again.')

