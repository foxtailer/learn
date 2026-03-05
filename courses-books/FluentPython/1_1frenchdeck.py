# https://github.com/fluentpython/example-code-2e

import collections


Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    """
    python3 -m doctest 1_1frenchdeck.py

    >>> beer_card = Card('7', 'diamonds')
    >>> beer_card
    Card(rank='7', suit='diamonds')

    >>> deck = FrenchDeck()
    >>> len(deck)
    52

    >>> deck = FrenchDeck()
    >>> len(deck)
    52

    # >>> from random import choice
    # >>> choice(deck)
    # Card(rank='3', suit='hearts')
    
    >>> deck = FrenchDeck()
    >>> for card in reversed(deck):  # doctest: +ELLIPSIS
    ...     print(card)
    Card(rank='A', suit='hearts')
    Card(rank='K', suit='hearts')
    Card(rank='Q', suit='hearts')
    ...

    >>> Card('Q', 'hearts') in deck
    True
    >>> Card('7', 'beasts') in deck
    False
    """
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):  # Composition. FrenchDeck contain list object.
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

