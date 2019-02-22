#############################################################################################################################################################################################################################
#                                       Project Euler Problem 54 Solution -- Poker Hands
#                                                       By Mike Kane
#
#
#  In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:
#
#  High Card: Highest value card.
#  One Pair: Two cards of the same value.
#  Two Pairs: Two different pairs.
#  Three of a Kind: Three cards of the same value.
#  Straight: All cards are consecutive values.
#  Flush: All cards of the same suit.
#  Full House: Three of a kind and a pair.
#  Four of a Kind: Four cards of the same value.
#  Straight Flush: All cards are consecutive values of same suit.
#  Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
#  The cards are valued in the order:
#  2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
#
#  If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below).
#  But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.
#
#  Consider the following five hands dealt to two players:
#
#  Hand	 	Player 1	 	Player 2	 	Winner
#  1	 	5H 5C 6S 7S KD
#  Pair of Fives
# 	2C 3S 8S 8D TD
#  Pair of Eights
#       	Player 2
#  2	 	5D 8C 9S JS AC
#  Highest card Ace
# 	2C 5C 7D 8S QH
#Highest card Queen
# 	Player 1
#3	 	2D 9C AS AH AC
#Three Aces
# 	3D 6D 7D TD QD
#Flush with Diamonds
# 	Player 2
#4	 	4D 6S 9H QH QC
#Pair of Queens
#Highest card Nine
# 	3D 6D 7H QD QS
#Pair of Queens
#Highest card Seven
# 	Player 1
#5	 	2H 2D 4C 4D 4S
#Full House
#With Three Fours
# 	3C 3D 3S 9S 9D
#Full House
#with Three Threes
# 	Player 1
#  The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. 
#  You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.
#
#  How many hands does Player 1 win?

################################################################################################################################################################################################################################################


def flushChecker(hand):
    hand = list(hand.split())
    hand.sort()
    suit = hand[0][1]
    for card in hand:
        if card[1] != suit:
            return False
    return True 

def straightChecker(hand):
    hand = list(hand.split())
    hand.sort()
    cardValues = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    card1 = cardValues.index(hand[0][0])
    card2 = cardValues.index(hand[1][0])
    card3 = cardValues.index(hand[2][0])
    card4 = cardValues.index(hand[3][0])
    card5 = cardValues.index(hand[4][0])
    if card2 == card1 + 1:
        if card3 == card1 + 2:
            if card4 == card1 + 3:
                if card5 == card1 + 4:
                    return True
    return False

def royalFlushChecker(hand):
    if flushChecker(hand) == False:
        return False
    if straightChecker(hand) == True:
        hand = list(hand.split())
        hand.sort()
        if hand[0][0] == 'T':
            return True
        else:
            return False
    else:
        return False

def fullHouseChecker(hand):
    hand = list(hand.split())
    hand.sort()
    print hand
    if hand[0][0] == hand[1][0] and (hand[2][0] ==hand[1][0] or hand[2][0] == hand[3][0]) and hand[3][0] == hand[4][0]:
        return True
    else:
        return False
        
def fourOfAKindChecker(hand):
    hand = list(hand.split())
    hand.sort()
    print hand
    if hand[0][0] != hand[1][0] and hand[1][0] == hand[2][0] and hand[2][0] == hand[3][0] and hand[3][0] == hand[4][0]:
        return True
    elif hand[0][0] == hand[1][0] and hand[1][0] == hand[2][0] and hand[2][0] == hand[3][0] and hand[3][0] != hand[4][0]:
        return True
    else:
        return False

def threeOfAKindChecker(hand):
    hand = list(hand.split())
    hand.sort()
    print hand
    if hand[0][0] == hand[1][0] and hand[1][0] == hand[2][0] and hand[2][0] != hand[3][0] and hand[3][0] != hand[4][0]:
        return True
    elif hand[0 ][0] != hand[1][0] and hand[1][0] ==hand[2][0] and hand[2][0] == hand[3][0] and hand[3][0] != hand[4][0]:
        return True
    elif hand[0][0] != hand [1][0] and hand[1][0] !=  hand[2][0] and hand[2][0] == hand[3][0] and hand[3][0] == hand[4][0]:
        return True
    else:
        return False
        
def twoPairChecker(hand):
    hand = list(hand.split())
    hand.sort()
    print hand
    if hand[0][0] == hand[1][0] and hand [1][0] != hand[2][0] and hand[2][0] == hand[3][0] and (hand[4][0] != hand[0][0] and hand[4][0] != hand[3][0]):
        return True
    elif hand[0][0] == hand[1][0] and hand [1][0] != hand[2][0] and hand[3][0] == hand[4][0] and (hand[2][0] != hand[0][0] and hand[2][0] != hand[3][0]):
        return True
    elif hand[1][0] == hand[2][0] and hand [2][0] != hand[3][0] and hand[3][0] == hand[4][0] and (hand[1][0] != hand[0][0] and hand[0][0] != hand[3][0]):
        return True
    else:
        return False
        
def pairChecker(hand):
    hand = list(hand.split())
    hand.sort()
    print hand
    if hand[0][0] == hand[1][0] and (hand[1][0] != hand[2][0] and hand[1][0] != hand[3][0] and hand[1][0] != hand[4][0]) and (hand[2][0] != hand[3][0] and hand[2][0] != hand[4][0]) and (hand[3][0] != hand[4][0]):
        return True
    elif hand[1][0] == hand[2][0] and (hand[1][0] != hand[0][0] and hand[1][0] != hand[3][0] and hand[1][0] != hand[4][0]) and (hand[0][0] != hand[3][0] and hand[0][0] != hand[4][0]) and (hand[3][0] != hand[4][0]):
        return True
    elif hand[2][0] == hand[3][0] and (hand[3][0] != hand[0][0] and hand[3][0] != hand[1][0] and hand[3][0] != hand[4][0]) and (hand[0][0] != hand[1][0] and hand[0][0] != hand[4][0]) and (hand[1][0] != hand[4][0]):
        return True
    elif hand[3][0] == hand[4][0] and (hand[3][0] != hand[0][0] and hand[3][0] != hand[1][0] and hand[3][0] != hand[2][0]) and (hand[0][0] != hand[1][0] and hand[0][0] != hand[2][0]) and (hand[1][0] != hand[2][0]):
        return True
    else:
        return False



        
            
        
    

    
            
    
    
        

