#-------------------------------------------------------------------------------
# Name:        Deck
# Purpose:     simulate a deck of 52 cards
#
# Author:      cnys
#
# Created:     23/09/2020
# Copyright:   (c) cnys 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random #needed for shuffle mode
from cardstock import Card

class Deck:
    #simulates a hand of cards with a defined maxsize
    def __init__(self):
        """make a FULL constructor method for the deck of cards
        start by declaring an empty list, which will have a defined size of 52
        >>Deck()
        Deck object which holds all 52 cards
        """
        self.cards  = []
        self.numberDrawn = 0

        #at this point we will creat all 52 cards automatically, and append them to the deck
        value = 0;
        for i in range (0, 13):
            value = value + 1
            card = Card("Default", "Clubs", value, True)
            #start by using default for the rank, we will work this out from "value"
            if value == 11:
                card.setRank("Jack")
                card.setValue(10)
            elif value == 12:
                card.setRank("Queen")
                card.setValue(10)
            elif value == 13:
                card.setRank("King")
                card.setValue(10)
            elif value == 1:
                card.setRank("Ace")
            else:
                card.setRank(str(value))
            self.cards.append(card)

        value = 0
        for i in range (0, 13):
            value = value + 1
            card = Card("Default", "Diamonds", value, True)
            #start by using default for the rank, we will work this out from "value"
            if value == 11:
                card.setRank("Jack")
                card.setValue(10)
            elif value == 12:
                card.setRank("Queen")
                card.setValue(10)
            elif value == 13:
                card.setRank("King")
                card.setValue(10)
            elif value == 1:
                card.setRank("Ace")
            else:
                card.setRank(str(value))
            self.cards.append(card)

    def getCards (self):
        return self.cards


    def toString(self):
        info = ""
        if self.isEmpty():
            info = "No cards left in the deck!"
        else:
            for card in self.cards:
                info = info + card.toString() + "\n"
        return info

    def isEmpty(self):
        if len(self.cards) == 0:
            return True
        else:
            return False

    def isFull(self):
        if len(self.cards) == self.maxsize:
            return True
        else:
            return False

    def shuffle(self):
        #use the list shuffle to shuffle the deck
        random.shuffle(self.cards)

    def drawNext(self):
        #this method removes the first card and returns it
        #you might want to think about calling isEmpty() before attempting to draw
        #a new card as you cannot draw from an empty list
        next = self.cards.pop(0)
        return next



