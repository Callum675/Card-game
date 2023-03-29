#-------------------------------------------------------------------------------
# Name:        Hand
# Purpose:     hold cards for player
#
# Author:      Callm Mcintosh
#
#-------------------------------------------------------------------------------

#imports
from Cardclass import Card

class Hand:

    #simulates a hand of cards with a maxsize

    def __init__(self, maxsize):
        """make a FULL constructor method for the hand of cards
        start by declaring maxsize for the hand of cards
	>>Hand(5)
	hand object that can hold a max of 5
	"""
        self.cards = []
        self.maxsize = maxsize


    #accessor methods next ("getters")

    def getCards(self):
        return self.cards

    def getMaxsize(self):
        return self.maxsize


    #transformer/modifier methods next ("setters")

    def setCards(self, cards):
        self.cards = cards

    def setMaxsize(self, maxsize):
        self.maxsize = maxsize

    #special method

    def toString(self):
        info = ""
        if self.isEmpty():
            info = "No cards in hand"
        else:
            for cards in self.cards:
                info = info + Card.toString() + "\n"
        return info

    def isEmpty(self):
        if len(self.cards) == 0:
            return True
        else:
            return False

    def isFull(self):
        if lem(self.cards) == self.maxsize:
            return True
        else:
            return False

    def addCard(self, card):
        self.cards.append(card)

    def getTotal(self):
        return sum(self.cards)

    def elvenorone(self):
        #Ace 11 or 1
        pass

    def sortbysuit(self):
        pass

    def findPairs(self):
        pass

    def findPrial(self):
        #three of a kind
        pass

    def findMisere(self):
        #lowest scoring card
        pass
    

