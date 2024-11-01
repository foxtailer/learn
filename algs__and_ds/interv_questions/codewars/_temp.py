"""
A famous casino is suddenly faced with a sharp decline of their revenues. They decide to offer Texas 
hold'em also online. Can you help them by writing an algorithm that can rank poker hands?

Task
Create a poker hand that has a method to compare itself to another poker hand:

compare_with(self, other_hand)
A poker hand has a constructor that accepts a string containing 5 cards:

PokerHand("KS 2H 5C JD TD")
The characteristics of the string of cards are:

Each card consists of two characters, where
The first character is the value of the card: 2, 3, 4, 5, 6, 7, 8, 9, T(en), J(ack), Q(ueen), K(ing), A(ce)
The second character represents the suit: S(pades), H(earts), D(iamonds), C(lubs)
A space is used as card separator between cards
The result of your poker hand compare can be one of these 3 options:

[ "Win", "Tie", "Loss" ]
"""


from collections import namedtuple


class PokerHand:
    RESULT = ["Loss", "Tie", "Win"]

    HAND_VALUES = {
        'High_card': 1,
        'Pair': 2,
        'Two_pairs': 3,
        'Set': 4,
        'Straight': 5,
        'Flush': 6,
        'Full_house': 7,
        'Kare': 8,
        'Straight_flush': 9,
        'Royal_flush': 10
    }

    CARD_RANKS = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')  # 12

    def __init__(self, hand):  # hand -> "KS 2H 5C JD TD"
        Card = namedtuple('Card', ['rank', 'suit'])
        hand = hand.split()
        hand = [Card(card[0], card[1]) for card in hand]
        hand.sort(key=lambda card: self.CARD_RANKS.index(card.rank))
        self.hand = hand  # hand -> [Card('K', 'S'), Card('2', 'H'), Card('5', 'C'), Card('J', 'D'), Card('T', 'D')]
        self.ranks_array = tuple([card.rank for card in self.hand])
        self.suits_array = tuple([card.suit for card in self.hand])
    
    def straight(self):
        """
        >>> PokerHand('3H 4H 5H 6H 7H').straight()
        (True, 5, None)
        >>> PokerHand('9H TH JH QH KH').straight()
        (True, 11, None)
        >>> PokerHand('2S 3H 4H 5S AD').straight()
        (True, 3, None)
        >>> PokerHand('3H 3H 5H 6H 7H').straight()
        (False, 0, None)
        """
        if self.ranks_array == self.__class__.CARD_RANKS[:4] + (self.__class__.CARD_RANKS[-1],):
            return True,\
                   self.__class__.CARD_RANKS.index(self.ranks_array[-2]),\
                   None
        
        for i in range(9):
            if self.__class__.CARD_RANKS[i:i + 5] == self.ranks_array:
                return True,\
                       self.__class__.CARD_RANKS.index(self.ranks_array[-1]),\
                       None
        return False, 0, None
    
    def flush(self):
        """
        >>> PokerHand('3S 4H 5D 6C 7H').flush()
        (False, 0, (1, 2, 3, 4))
        >>> PokerHand('9H TH JH QH KH').flush()
        (True, 11, (7, 8, 9, 10))
        >>> PokerHand('3H 3H 5H 6H 7H').flush()
        (True, 5, (1, 1, 3, 4))
        """
        highest_card_range = tuple((PokerHand.CARD_RANKS.index(rank) for rank in self.ranks_array[:-1]))

        return (check := self.suits_array.count(self.suits_array[0]) == 5),\
                PokerHand.CARD_RANKS.index(self.hand[-1].rank) if check else 0,\
                highest_card_range
    
    def kare(self):
        """
        >>> PokerHand('3S QH QD QC QH').kare()
        (True, 10, (1,))
        >>> PokerHand('9H 9H 9H 9H KH').kare()
        (True, 7, (11,))
        >>> PokerHand('3H 3H 5H 6H 7H').kare()
        (False, None, None)
        """
        for i in range(2):
            if self.ranks_array.count(self.ranks_array[i]) == 4:
                return True,\
                       PokerHand.CARD_RANKS.index(self.ranks_array[i]),\
                       (PokerHand.CARD_RANKS.index(self.ranks_array[0]),) if i == 1 else (PokerHand.CARD_RANKS.index(self.ranks_array[-1]),)
        return False, None, None
    
    def full_house(self):
        """
        >>> PokerHand('3S 3H 3D 7C 7H').full_house()
        (True, 1, (5,))
        >>> PokerHand('2H 2H 3H 3D 3H').full_house()
        (True, 1, (0,))
        >>> PokerHand('3H 3H 5H 6D 7H').full_house()
        (False, None, None)
        """
        match self.ranks_array:
            case [a, b, c, d, e] if a == b == c and d == e: 
                return True,\
                       PokerHand.CARD_RANKS.index(a),\
                       (PokerHand.CARD_RANKS.index(e),)
            
            case [a, b, c, d, e] if c == d == e and a == b:
                return True,\
                       PokerHand.CARD_RANKS.index(e),\
                       (PokerHand.CARD_RANKS.index(a),)
            
            case _: return False, None, None

    def _set(self):
        """
        >>> PokerHand('3S 3H 3D 7C KH')._set()
        (True, 1, (5, 11))
        >>> PokerHand('2H 3H 3C 3D 5H')._set()
        (True, 1, (0, 3))
        >>> PokerHand('2H 3H 7H 7D 7S')._set()
        (True, 5, (0, 1))
        >>> PokerHand('2H 3H 6H 7D 8S')._set()
        (False, None, None)
        """
        match self.ranks_array:
            case [a, b, c, d, e] if a == b == c and d != e:
                 return True,\
                        PokerHand.CARD_RANKS.index(a),\
                        tuple((PokerHand.CARD_RANKS.index(card)) for card in (d, e))
            
            case [a, b, c, d, e] if c == d == e and a != b:
                 return True,\
                        PokerHand.CARD_RANKS.index(e),\
                        tuple((PokerHand.CARD_RANKS.index(card)) for card in (a, b))
            
            case [a, b, c, d, e] if b == c == d and a != e:
                 return True,\
                        PokerHand.CARD_RANKS.index(c),\
                        tuple((PokerHand.CARD_RANKS.index(card)) for card in (a, e))
            
            case _: return False, None, None

    def two_pairs(self):
        """
        >>> PokerHand('3S 3H 4D 4C KH').two_pairs()
        (True, 2, (11, 1))
        >>> PokerHand('2H 3H 3C 5D 5H').two_pairs()
        (True, 3, (0, 1))
        >>> PokerHand('3D 3H 7H 8D 8S').two_pairs()
        (True, 6, (5, 1))
        >>> PokerHand('2H 3H 6H 7D 8S').two_pairs()
        (False, None, None)
        """
        match self.ranks_array:
            case [a, b, c, d, e] if a == b != c and d == e != c:
                return True,\
                       PokerHand.CARD_RANKS.index(e),\
                       (PokerHand.CARD_RANKS.index(c), PokerHand.CARD_RANKS.index(a))

            case [a, b, c, d, e] if a == b != c and c == d != e:
                return True,\
                       PokerHand.CARD_RANKS.index(c),\
                       (PokerHand.CARD_RANKS.index(e), PokerHand.CARD_RANKS.index(a))

            case [a, b, c, d, e] if a != b == c and d == e != c:
                return True,\
                       PokerHand.CARD_RANKS.index(d),\
                       (PokerHand.CARD_RANKS.index(a), PokerHand.CARD_RANKS.index(b))

            case _: return False, None, None
         
    def pair(self):
        """
        >>> PokerHand('3S 3H 4D QC KH').pair()
        (True, 1, (2, 10, 11))
        >>> PokerHand('2H 3H 3C 5D QH').pair()
        (True, 1, (0, 3, 10))
        >>> PokerHand('2D 3H 7H 8D 8S').pair()
        (True, 6, (0, 1, 5))
        >>> PokerHand('2H 3H 6H 7D 8S').pair()
        (False, None, None)
        """
        pair_count = 0
        card_count = 0
        pair_indexes = []
        
        for i in range(len(self.ranks_array)-1):
            if self.ranks_array[i] == self.ranks_array[i+1]:
                card_count += 1
                pair_count += 1
                pair_indexes.append(i)
            else:
                card_count = 0
            
            if pair_count > 1 or card_count > 1:
                return False, None, None
        else:
            if pair_count == 0:
                return False, None, None
            return pair_count == 1,\
                   PokerHand.CARD_RANKS.index(self.ranks_array[pair_indexes[0]]),\
                   tuple((PokerHand.CARD_RANKS.index(rank) for rank in [self.ranks_array[i] for i in range(len(self.ranks_array)) if i != pair_indexes[0] and i != pair_indexes[0] + 1]))
    
    def high_card(self):
        """
        >>> PokerHand('3S 5H 8D QC KH').high_card()
        (True, 11, (1, 3, 6, 10))
        >>> PokerHand('2H 2H 6H 7D 8S').high_card()
        (False, None, None)
        """
        match self.ranks_array:
            case [a, b, c, d, e] if (a != b != c != d != e) and\
                            not self.flush()[0] and\
                            not self.straight()[0]: 
                return True,\
                       PokerHand.CARD_RANKS.index(self.ranks_array[-1]),\
                       tuple((PokerHand.CARD_RANKS.index(rank) for rank in self.ranks_array[:-1]))
            case _: return False, None, None

    def hand_name(self):
        hand = self.hand

        match hand:
            case hand if self.straight()[0] and (b := self.flush())[0]: 
                return self.HAND_VALUES['Straight_flush'], b[1], None

            case hand if (a := self.straight())[0] and not self.flush()[0]: 
                return self.HAND_VALUES['Straight'], a[1], None

            case hand if not self.straight()[0] and (b := self.flush())[0]: 
                return self.HAND_VALUES['Flush'], b[1], b[2]

            case hand if (a := self.kare())[0]: 
                return self.HAND_VALUES['Kare'], a[1], a[2]

            case hand if (a := self.full_house())[0]:
                return self.HAND_VALUES['Full_house'], a[1], a[2]

            case hand if (a := self._set())[0]:
                return self.HAND_VALUES['Set'], a[1], a[2]

            case hand if (a := self.two_pairs())[0]:
                return self.HAND_VALUES['Two_pairs'], a[1], a[2]

            case hand if (a := self.pair())[0]:
                return self.HAND_VALUES['Pair'], a[1], a[2]

            case hand if (a := self.high_card())[0]:
                return self.HAND_VALUES['High_card'], a[1], a[2]
            
            case _: return -1

    def compare_with(self, other):
        """
        >>> PokerHand('2H 3H 4H 5H 6C').compare_with(\
            PokerHand('2H 3H 4H 5H QH'))
        'Loss'
        >>> PokerHand('2H 3H 4H 5H 6H').compare_with(\
            PokerHand('2H 3H 4H 5H 6H'))
        'Tie'
        >>> PokerHand('2H 3H 4H 5H 6C').compare_with(\
            PokerHand('2H 3H 4H 5H 6C'))
        'Tie'
        >>> PokerHand('3H 4H 5H 6H 7H').compare_with(\
            PokerHand('2H 3H 4H 5H 6H'))
        'Win'
        >>> PokerHand('3H 4H 5H 6H 7C').compare_with(\
            PokerHand('2H 3H 4H 5H 6C'))
        'Win'
        >>> PokerHand('2S 3H 4H 5S AD').compare_with(\
            PokerHand('AH AC 5H 6H AS'))
        'Win'
        >>> PokerHand('3H 4H 5H 6H 7H').compare_with(\
            PokerHand('2H 2H 2H 2H 6C'))               # Kare
        'Win'
        >>> PokerHand('2H 2H 2H 2H 6C').compare_with(\
            PokerHand('3H 4H 5H 6H 7H'))
        'Loss'
        >>> PokerHand('2H 2H 2H 2H 6C').compare_with(\
            PokerHand('2H 2H 2H 2H 6C'))
        'Tie'
        >>> PokerHand('2H 2H 2H 2H 6C').compare_with(\
            PokerHand('3H 3H 3H 3H 6C'))
        'Loss'
        >>> PokerHand('2H 2H 2H 2H 7C').compare_with(\
            PokerHand('2H 2H 2H 2H 6C'))
        'Win'
        >>> PokerHand('3H 3H 3C 3H QH').compare_with(\
            PokerHand('2H 2H 3H 3H 3C'))              # Full house
        'Win'
        >>> PokerHand('2C 2H 4D 4H 4C').compare_with(\
            PokerHand('2H 3H TH QH AH'))
        'Win'
        >>> PokerHand('2C 2H 4D 4H 4S').compare_with(\
            PokerHand('2H 2C QD QS QC'))
        'Loss'
        >>> PokerHand('2C 2H 4D 4H 4S').compare_with(\
            PokerHand('3C 3H 4D 4H 4S'))
        'Loss'
        >>> PokerHand('3H 3D 3S QH KH').compare_with(\
            PokerHand('2H 2C 3H 3D 3C'))              # Set
        'Loss'
        >>> PokerHand('3H 3D 3S QH KH').compare_with(\
            PokerHand('4H 4D 4S QH KH'))
        'Loss'
        >>> PokerHand('3H 3D 3S JH KH').compare_with(\
            PokerHand('3H 3D 3S QH KH'))
        'Loss'
        >>> PokerHand('3H 3D 3S JH KH').compare_with(\
            PokerHand('3H 3D 3S JH KH'))
        'Tie'
        >>> PokerHand('3H 3D 4S 4H KH').compare_with(\
            PokerHand('3H 3D 3S QH KH'))              # Two pairs
        'Loss'
        >>> PokerHand('3H 3D 4S 4H KH').compare_with(\
            PokerHand('3H 3D 4S 4H KH'))
        'Tie'
        >>> PokerHand('3H 3D 4S 4H KH').compare_with(\
            PokerHand('3H 3D 5S 5H KH'))
        'Loss'
        >>> PokerHand('3H 3D 4S 4H KH').compare_with(\
            PokerHand('2H 2D 4S 4H KH'))
        'Win'
        >>> PokerHand('2H 2D 4S 4H KH').compare_with(\
            PokerHand('2H 2D 4S 4H QH'))
        'Win'
        >>> PokerHand('2H 2D 4S 5H KH').compare_with(\
            PokerHand('3H 3D 3S QH KH'))              # Pair
        'Loss'
        >>> PokerHand('2H 2D 4S 5H KH').compare_with(\
            PokerHand('2C 2S 4S 5H KH'))
        'Tie'
        >>> PokerHand('2H 2D 4S 5H KH').compare_with(\
            PokerHand('2C 2S 4S 5H AH'))
        'Loss'
        >>> PokerHand('2H 2D 4S 5H KH').compare_with(\
            PokerHand('2C 2S 3S 5H KH'))
        'Win'
        >>> PokerHand('2H 3D 4S 8H KH').compare_with(\
            PokerHand('3H 3D 3S QH KH'))              # High card
        'Loss'
        >>> PokerHand('2H 3D 4S QH KH').compare_with(\
            PokerHand('2H 3D 4S QH KH'))
        'Tie'
        >>> PokerHand('2H 3D 4S QH AH').compare_with(\
            PokerHand('2H 3D 4S QH KH'))
        'Win'
        """
        x = self.hand_name()
        y = other.hand_name()

        if x[0] > y[0]:
            return self.RESULT[2]
        elif x[0] < y[0]:
            return self.RESULT[0]
        else:
            if x[1] > y[1]:
                return self.RESULT[2]
            elif x[1] < y[1]:
                return self.RESULT[0]
            else:
                if x[2] and y[2]:
                    i = len(x[2])-1
                    while i >= 0:
                        if x[2][i] > y[2][i]:
                            return self.RESULT[2]
                        elif x[2][i] < y[2][i]:
                            return self.RESULT[0]
                        i -= 1
                    return self.RESULT[1]
                else:
                    return self.RESULT[1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
