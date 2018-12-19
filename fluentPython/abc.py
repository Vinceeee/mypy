#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections

Card = collections.namedtuple("Card",['rank','suit'])

class Deck(object):
    '''
    Sample in Chapter one 
    '''
    ranks = [str(n) for n in range(3,11)] + list('JQKA2')
    suits = '黑桃 红桃 梅花 方块'.split()

    def __init__(self):
        self._cards = [Card(rank,suit) for rank in self.ranks for suit in self.suits]
    
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self,pos):
        # we could use index / iter to get this
        return self._cards[pos]
    
    def pick(self,count=1):
        cards = []
        for i in range(count):
            cards.append(self._cards.pop())
        return cards
    
def order_high(card):
    # not recommended to use non-ascii character
    suit_value = dict(黑桃=3,红桃=2,梅花=1,方块=0)
    rank_value = Deck.ranks.index(card.rank)
    return rank_value * len(suit_value) + suit_value[card.suit]

def main1():
    deck = Deck()
    import random
    random.shuffle(deck._cards)
    picking = deck.pick(13)

    for card in sorted(picking,key=order_high):
        print(card)

def main2():
    from random import choice

    coin = (0,1)

    s , f = 0,0

    for i in range(1000):
        if choice(coin) == 1:
            s += 1
        else:
            f += 1
    print("s -- {0} ; f -- {1}".format(s,f))


if __name__ == '__main__':
    main1()
