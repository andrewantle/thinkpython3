'''
Sets of Objects

Think Python - Chapter 15:
<http://www.greenteapress.com/thinkpython/thinkCSpy/html/chap15.html>
'''

from random import randrange


class Card(object):
    '''A playing card class, with a suit and a rank.'''

    __suits = [
        'Clubs',
        'Diamonds',
        'Hearts',
        'Spades'
    ]

    __ranks = [
        'Joker',
        'Ace',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        '10',
        'Jack',
        'Queen',
        'King'
    ]

    def __init__(self, suit=0, rank=2):
        '''Initialize a new card, by default a 2 of Clubs.'''
        self.suit = suit
        self.rank = rank

    def __str__(self):
        '''Return the string representation of this instance.'''
        rank = self.__ranks[self.rank]
        suit = self.__suits[self.suit]

        return '%s of %s' % (rank, suit)


class Deck(object):

    def __init__(self):
        '''Initialize a new deck.'''
        self.cards = []

        for suit in range(4):
            for rank in range(1, 14):       # Skip the Joker
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        '''Return the string representation of this instance.'''
        to_display = ""

        for card in self.cards:
            to_display += str(card) + '\n'

        return to_display

    def shuffle(self):
        '''Randomly shuffle the deck.'''
        count = len(self.cards)

        for i in range(count):
            j = randrange(i, count)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

