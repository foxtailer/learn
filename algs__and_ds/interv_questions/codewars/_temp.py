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

    CARD_RANKS = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')

    def __init__(self, hand):
        Card = namedtuple('Card', ['rank', 'suit'])
        hand = hand.split()
        hand = [Card(card[0], card[1]) for card in hand]
        hand.sort(key=lambda card: self.CARD_RANKS.index(card.rank))
        self.hand = hand
    
    @staticmethod
    def straight(parent_array, child_array):
        """
        >>> PokerHand.straight(('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'), ['3', '4', '5', '6', '7'])
        True
        >>> PokerHand.straight(('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'), ['9', 'T', 'J', 'Q', 'K'])
        True
        >>> PokerHand.straight(('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'), ['3', '3', '5', '6', '7'])
        False
        """
        parent_array = list(parent_array)
        parent_len = len(parent_array)
        child_len = len(child_array)
        
        for i in range(parent_len - child_len + 1):
            if parent_array[i:i + child_len] == child_array:
                return True
        return False
    
    @staticmethod
    def flush(suits_array):
        """
        >>> PokerHand.flush(['H', 'H', 'H', 'H', 'H'])
        True
        >>> PokerHand.flush(['D', 'D', 'D', 'D', 'D'])
        True
        >>> PokerHand.flush(['D', 'D', 'H', 'S', 'C'])
        False
        """
        return suits_array.count(suits_array[0]) == 5
    
    @staticmethod
    def kare(rank_array):
        """
        >>> PokerHand.kare(['Q', 'Q', 'Q', 'Q', 'K'])
        True
        >>> PokerHand.kare(['3', '7', '7', '7', '7'])
        True
        >>> PokerHand.kare(['3', '4', '5', '6', '7'])
        False
        """
        for i in range(2):
            if rank_array.count(rank_array[i]) == 4:
                return True
        return False
    
    @staticmethod
    def full_house(rank_array):
        """
        >>> PokerHand.full_house(['Q', 'Q', 'Q', 'K', 'K'])
        True
        >>> PokerHand.full_house(['3', '3', '7', '7', '7'])
        True
        >>> PokerHand.full_house(['3', '4', '5', '6', '7'])
        False
        """
        match rank_array:
            case [a, b, c, d, e] if a == b == c and d == e: return True
            case [a, b, c, d, e] if c == d == e and a == b: return True
            case _: return False

    @staticmethod
    def _set(rank_array):
        """
        >>> PokerHand._set(['Q', 'Q', 'Q', 'K', 'K'])
        False
        >>> PokerHand._set(['3', '3', '7', '7', '7'])
        False
        >>> PokerHand._set(['3', '4', '5', '6', '7'])
        False
        >>> PokerHand._set(['3', '3', '3', '6', '7'])
        True
        >>> PokerHand._set(['3', '4', 'K', 'K', 'K'])
        True
        >>> PokerHand._set(['3', 'K', 'K', 'K', 'Q'])
        True
        """
        match rank_array:
            case [a, b, c, d, e] if a == b == c and d != e: return True
            case [a, b, c, d, e] if c == d == e and a != b: return True
            case [a, b, c, d, e] if b == c == d and a != e: return True
            case _: return False

    @staticmethod
    def two_pairs(rank_array):
        """
        >>> PokerHand.two_pairs(['Q', 'Q', 'Q', 'K', 'K'])
        False
        >>> PokerHand.two_pairs(['3', '3', '7', '7', '7'])
        False
        >>> PokerHand.two_pairs(['3', '4', '5', '6', '7'])
        False
        >>> PokerHand.two_pairs(['3', '3', '4', '6', '6'])
        True
        >>> PokerHand.two_pairs(['3', '4', '4', 'K', 'K'])
        True
        >>> PokerHand.two_pairs(['3', '3', 'K', 'K', 'Q'])
        True
        """
        match rank_array:
            case [a, b, c, d, e] if a == b != c and d == e != c and e != a: return True
            case [a, b, c, d, e] if a == b != c and c == d != e: return True
            case [a, b, c, d, e] if a != b == c and d == e != c: return True
            case _: return False
            
    @staticmethod
    def pair(rank_array):
        """
        >>> PokerHand.pair(['Q', 'Q', 'Q', 'K', 'K'])
        False
        >>> PokerHand.pair(['3', '3', '7', '7', '7'])
        False
        >>> PokerHand.pair(['3', '4', '5', '6', '7'])
        False
        >>> PokerHand.pair(['3', '3', '3', '6', '7'])
        False
        >>> PokerHand.pair(['3', '3', '4', '5', '6'])
        True
        >>> PokerHand.pair(['3', '4', '4', 'Q', 'K'])
        True
        >>> PokerHand.pair(['3', '5', 'K', 'K', 'Q'])
        True
        """
        pair_count = 0
        card_count = 0
        
        for i in range(len(rank_array)-1):
            if rank_array[i] == rank_array[i+1]:
                card_count += 1
                pair_count += 1
            else:
                card_count = 0
            
            if pair_count > 1 or card_count > 1:
                return False
        else:
            return card_count == 1 or pair_count == 1
    
    @staticmethod
    def high_card(hand):
        """
        >>> hand = PokerHand("2S 3S 5S QS KS")
        >>> PokerHand.high_card(hand.hand)
        False
        >>> hand = PokerHand("2S 2H 5D QS KC")
        >>> PokerHand.high_card(hand.hand)
        False
        >>> hand = PokerHand("2S 3H 5D QS KC")
        >>> PokerHand.high_card(hand.hand)
        True
        """
        match hand:
            case [a, b, c, d, e] if (a.rank != b.rank != c.rank != d.rank != e.rank) and\
                            not PokerHand.flush([card.suit for card in hand]): return True
            case _: return False

    def highest_card(self, hand) -> int:
        return 0
    
    def hand_name(self, hand) -> int:
        match hand:
            case hand if self.straight(self.CARD_RANKS, [card.rank for card in hand]) and self.flush([card.suit for card in hand]): 
                return self.HAND_VALUES['Straight_flush']
            
            case hand if self.straight(self.CARD_RANKS, [card.rank for card in hand]) and  not self.flush([card.suit for card in hand]): 
                return self.HAND_VALUES['Straight']
            
            case hand if not self.straight(self.CARD_RANKS, [card.rank for card in hand]) and self.flush([card.suit for card in hand]): 
                return self.HAND_VALUES['Flush']
            
            case hand if self.kare([card.rank for card in hand]): 
                return self.HAND_VALUES['Kare']
            
            case hand if self.full_house([card.rank for card in hand]):
                return self.HAND_VALUES['Full_house']
            
            case hand if self._set([card.rank for card in hand]):
                return self.HAND_VALUES['Set']
            
            case hand if self.two_pairs([card.rank for card in hand]):
                return self.HAND_VALUES['Two_pairs']
            
            case hand if self.pair([card.rank for card in hand]):
                return self.HAND_VALUES['Pair']
            
            case hand if self.high_card(hand):
                return self.HAND_VALUES['High_card']
    
    def compare_with(self, other):
        x = self.hand_name(self.hand)
        y = other.hand_name(other.hand)

        if x > y:
            return self.RESULT[2]
        elif x < y:
            return self.RESULT[0]
        else:
            return self.RESULT[1]


hand = PokerHand("KS 2H 5C JD TD")
hand2 = PokerHand("KS KH 5C JD TD")
print(hand.compare_with(hand2))


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
