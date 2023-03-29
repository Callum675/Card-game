#Written By Callum Mcintosh 16/09/2020 v1.00
#
#-------------------------------------------

#imports
from Cardclass import Card
from Hand import Hand
        
#main program



card1 = Card("Nine", "Diamonds", 9, False)          
print (card1.toString())

card2 = Card("Ace", "Spades", 1, False) 
print (card2.toString())

card1.turn()
card2.turn()
print (card1.toString())
print (card2.toString())

total = (card1.getValue() + card2.getValue())
print ("You have a total of " + str(total) + " in your hand")

if (total < 16):
    choice = input("Would you like another card? Hit y if Yes >>")
    if (choice == "y" or choice == "Y"):
        card3 = Card("Six", "Clubs", 6, True)
        total = total + card3.getValue()
        print (card3.toString())
        print ("You have a new total of " + str(total) + " in your hand")
    else:
        print ("You have finished with a total of " + str(total))

hand = Hand(5)
print(hand)
print (hand.toString())
Hand.addCard(card1)
Hand.addCard(card2)
Hand.addCard(card3)
print (Hand.toString())
print(Hand.getTotal())
