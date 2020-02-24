import os, sys


def prob_54(poker_hands):
    # O(n) solution.
    
    # Useful constants.
    suites = 'CHSD'  # clubs/hearts/spades/diamonds
    royal_flush = ['T', 'J', 'Q', 'K', 'A']
    
    p1_wins = 0
    for hand in poker_hands:
        
        # Format hands.
        p1_rank = sorted(hand[:5])
        p1_nums = [card[0] for card in p1_hand]
        p1_suits = [card[1] for card in p1_hand]
        p1_same_suit = p1_suits.count(p1_suits[0]) == len(p1_suits)
        p2_hand = sorted(hand[5:])
        p2_nums = [card[0] for card in p2_hand]
        p2_suits = [card[1] for card in p2_hand]
        p2_same_suit = p2_suits.count(p2_suits[0]) == len(p2_suits)

        # Check for each hand type.
        if p1_same_suit and p1_nums == royal_flush:





    return p1_wins


card_ranks = {
    '2':0,
    '3':1,
    '4':2,
    '5':3,
    '6':4,
    '7':5,
    '8':6,
    '9':7,
    'T':8,
    'J':9,
    'Q':10,
    'K':11,
    'A':12}
hand_ranks = {
    'highcard':0,
    'pair':1,
    '2pair':2,
    '3ofakind':3,
    'straight':4,
    'flush':5,
    'fullhouse':6,
    '4ofakind':7,
    'straightflush':8,
    'royalflush':9}


def rank_hand(hand):
    pass



if __name__ == '__main__':
    # Answer: 648

    poker_hands = []
    with open(os.path.join(sys.path[0], 'p054_poker.txt')) as f:
        for row in f.read().split('\n'):
            if row == '':
                continue
            poker_hands.append(row.split(' '))

    print(prob_54(poker_hands))
