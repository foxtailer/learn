import collections
import random
import doctest


Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    '''
    >>> deck = FrenchDeck()
    >>> len(deck)
    52
    >>> deck[0]
    Card(rank='2', suit='spades')
    >>> deck[-1]
    Card(rank='A', suit='hearts')
    ''' 
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')    
    suits = 'spades diamonds clubs hearts'.split()
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


    def __init__(self): 
        # Composing list functionality       
        self._cards = [Card(rank, suit) for suit in self.suits 
                                        for rank in self.ranks]
        
    def __len__(self):        
        return len(self._cards)
    
    def __getitem__(self, position):        
        return self._cards[position] 
    
    def spades_high(self, card): 
        '''
        system of ranking cards is by rank (with aces being
        highest), then by suit in the order of spades (highest), then hearts, diamonds, and clubs
        (lowest). returning 0 for the 2 of clubs and 51 for the ace of spades.
        '''
        rank_value = FrenchDeck.ranks.index(card.rank)    
        return rank_value * len(self.suit_values) + self.suit_values[card.suit] 
    
    def __str__(self):
        return str(self._cards)


deck = FrenchDeck()

# We can use a lot of standart functions becose of implementing
# __len__ and __getitem__
for card in sorted(deck, key=deck.spades_high):
   print(card)

print(f'Some card: {random.choice(deck)}')

random.shuffle(deck)
print(deck)

doctest.testmod()


###
"""for built-in types like list, str, bytearray, and so on, the interpreter takes a short‐
cut: the CPython implementation of len() actually returns the value of the ob_size
field in the PyVarObject C struct that represents any variable-sized built-in object in
memory. This is much faster than calling a method."""