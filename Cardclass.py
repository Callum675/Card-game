#-------------------------------------------------------------------------------
# Name:        Card
# Purpose:     simulate a simple card
#
# Author:      Callm Mcintosh
#
#-------------------------------------------------------------------------------

class Card:

#simulates a simple card

    def __init__(self, rank, suit, value, faceup):
        """make a FULL constructor method for the card
        start by declaring any attributes you will need, e.g. suit, rank, value, faceup
	>>Card("Nine", "Diamonds", 9, True)
	card object
	>>Card("Ace", "Spades", 11, False)
	card object"""
        self.rank = rank
        self.suit = suit
        self.value = value
        self.faceup = faceup
		
    #accessor methods next ("getters")
    def getRank(self):
        """a RETURN method to return the value of the attribute
        >>>card.getRank()
        Jack"""
        return self.rank

    def getSuit(self):
         """a RETURN method to return the value of the attribute
        >>>card.getSuit()
        Hearts"""
         return self.suit

    def getValue(self):
         """a RETURN method to return the value of the attribute
        >>>card.getValue()
        9"""
         return self.value

    def getFaceup(self):
         """a RETURN method to return the value of the attribute
        >>>card.getFaceup()
        False"""
         return self.faceup
   
    #transformer/modifier methods next ("setters")

    def setValue(self, newval):
        """sets the value of the attribute to the new value passed in
        >>>setValue(10)
           None"""
        self.theValue = newval

    def setSuit(self, newval):
        """sets the value of the attribute to the new value passed in
        >>>setRank("Ace")
           None"""
        self.theRank = newval

    def setRank(self, newval):
        """sets the value of the attribute to the new value passed in
        >>>setRank("Ace")
           None"""
        self.theRank = newval

    def setFaceup(self, newval):
        """sets the value of the attribute to the new value passed in
        >>>setVisible(True)
           None"""
        self.isVisible = newval

    #special method
    def turn(self):
        """the turn method turns the card over
        >>card.turn()
        faceup == False
        """
        if self.faceup == True:
            self.faceup = False
        else:
            self.faceup = True

    def toString(self):
        """a method to return ALL attribute values to string
        >>>toString()
        This card is the Jack of Clubs and is worth 10."""
        if self.faceup == False:
            info = "This card is hidden"

        else:
            info = "This card is the " + self.rank + " of " + self.suit + " and is worth " + str(self .value)
        return info
        









