#!/usr/bin/env python

print "Content-Type: text/html"
print

class Card:
	def __init__(self, value, name, cardImage):
		self.value = value
		self.name = name
		self.cardImage = cardImage

S2 =  Card(1, "Two Spades", "2S.png")
S3 =  Card(2, "Three Spades", "3S.png")
S4 =  Card(3, "Four Spades", "4S.png")
S5 =  Card(4, "Five Spades", "5S.png") 
S6 =  Card(5, "Six Spades", "6S.png")
S7 =  Card(6, "Seven Spades", "7S.png")
S8 =  Card(7, "Eight Spades", "8S.png") 
S9 =  Card(8, "Nine Spades", "9S.png")
S10 =  Card(9, "Ten Spades", "10S.png")
SJ =  Card(10, "Jack Spades", "JS.png")
SQ =  Card(11, "Queen Spades", "QS.png") 
SK =  Card(12, "King Spades", "KS.png")
SA = Card(13, "Ace Spades", "AS.png")

D2 = Card(1, "Two Diamonds", "2D.png");
D3 = Card(2, "Three Diamonds", "3D.png");
D4 = Card(3, "Four Diamonds", "4D.png");
D5 = Card(4, "Five Diamonds", "5D.png");
D6 = Card(5, "Six Diamonds", "6D.png");
D7 = Card(6, "Seven Diamonds", "7D.png");
D8 = Card(7, "Eight Diamonds", "8D.png");
D9 = Card(8, "Nine Diamonds", "9D.png");
D10 = Card(9, "Ten Diamonds", "10D.png");
DJ = Card(10, "Jack Diamonds", "JD.png");
DQ= Card(11, "Queen Diamonds", "QD.png");
DK = Card(12, "King Diamonds", "KD.png");
DA = Card(13, "Ace Diamonds", "AD.png");

C2 = Card(1, "Two Clubs", "2C.png")
C3 = Card(2, "Three Clubs", "3C.png")
C4 = Card(3,  "Four Clubs", "4C.png")
C5 = Card(4, "Five Clubs", "5C.png")
C6 = Card(5, "Six Clubs", "6C.png")
C7 = Card(6, "Seven Clubs", "7C.png")
C8 = Card(7, "Eight Clubs", "8C.png")
C9 = Card(8, "Nine Clubs", "9C.png")
C10 =  Card(9, "Ten Clubs", "10C.png")
CJ = Card(10, "Jack Clubs", "JC.png")
CQ = Card(11, "Queen Clubs", "QC.png")
CK = Card(12, "King Clubs", "KC.png")
CA = Card(13, "Ace Clubs", "AC.png")

H2 = Card(1, "Two Hearts", "2H.png")
H3 = Card(2, "Three Hearts", "3H.png")
H4 = Card(3,  "Four Hearts", "4H.png")
H5 = Card(4, "Five Hearts", "5H.png")
H6 = Card(5, "Six Hearts", "6H.png")
H7 = Card(6, "Seven Hearts", "7H.png")
H8 = Card(7, "Eight Hearts", "8H.png")
H9 = Card(8, "Nine Hearts", "9H.png")
H10 = Card(9, "Ten Hearts", "10H.png")
HJ = Card(10, "Jack Hearts", "JH.png")
HQ = Card(11, "Queen Hearts", "QH.png")
HK = Card(12, "King Hearts", "KH.png")
HA = Card(13, "Ace Hearts", "AH.png")

cards = []
cards.append(S2)
cards.append(S3)
cards.append(S4)
cards.append(S5)
cards.append(S6)
cards.append(S7)
cards.append(S8)
cards.append(S9)
cards.append(S10)
cards.append(SJ)
cards.append(SQ)
cards.append(SK)
cards.append(SA)
cards.append(D2)
cards.append(D3)
cards.append(D4)
cards.append(D5)
cards.append(D6)
cards.append(D7)
cards.append(D8)
cards.append(D9)
cards.append(D10)
cards.append(DJ)
cards.append(DQ)
cards.append(DK)
cards.append(DA)
cards.append(C2)
cards.append(C3)
cards.append(C4)
cards.append(C5)
cards.append(C6)
cards.append(C7)
cards.append(C8)
cards.append(C9)
cards.append(C10)
cards.append(CJ)
cards.append(CQ)
cards.append(CK)
cards.append(CA)
cards.append(H2)
cards.append(H3)
cards.append(H4)
cards.append(H5)
cards.append(H6)
cards.append(H7)
cards.append(H8)
cards.append(H9)
cards.append(H10)
cards.append(HJ)
cards.append(HQ)
cards.append(HK)
cards.append(HA)

player1Cards = []
player2Cards = []

from random import randint

print "<html><body>"
print "<head>"
print "<style>"
print """
#column { 
float:left; 
}"""
print "</style>"
print "</head>"
print "<h1>War</h1>"
print "<h2>Here are the results of the deal:</h2>"
print "<hr>"
i = 52
print "<br>"
for x in range(0, 52):
	if (len(player2Cards) == 26):
		break
		
	else:
		
		randomCard =  randint(0, len(cards) - 1)
		print "<div id=\"column\">"
		print "<strong> Player 1:</strong> %s" %cards[randomCard].name
		player1Cards.append(cards[randomCard])
		del cards[randomCard]
		randomCard =  randint(0, len(cards) - 1)
		print " <strong> Player 2:</strong> %s  " %cards[randomCard].name
		print "</div>"
		print "<br><br>"
		player2Cards.append(cards[randomCard])
		del cards[randomCard]
		


print "<hr>"
print "<h2>Let's Play!</h2>"
print "<hr>"
for x in range(1, 21):
	
	print "<p><h3>Round %s</h3></p>" %x
	randomPlayer1Card = randint(0, len(player1Cards) - 1)
	print "<strong>Player 1 Card: </strong>%s" %player1Cards[randomPlayer1Card].name
	
	randomPlayer2Card = randint(0, len(player2Cards) - 1)
	print "<strong> Player 2 Card: </strong>%s" %player2Cards[randomPlayer2Card].name
	
	if (player1Cards[randomPlayer1Card].value == player2Cards[randomPlayer2Card].value):
		print "<h3>**********************WAR********************</h3>"
		randomPlayer1WarCard = randint(0, len(player1Cards) - 1)
		randomPlayer2WarCard = randint(0, len(player2Cards) - 1)
		print "<p><strong>Player 1 War Card: </strong>%s" %player1Cards[randomPlayer1WarCard].name
		print "<strong>Player 2 War Card: </strong>%s</p>" %player2Cards[randomPlayer2WarCard].name

		if (player1Cards[randomPlayer1WarCard].value == 
			player2Cards[randomPlayer2WarCard].value):
			print "<p>This War is a draw...</p>"
			print "<p>**************************************************************</p>"
		
		elif (player1Cards[randomPlayer1WarCard].value > player2Cards[randomPlayer2WarCard].value):
			player1Cards.append(player2Cards[randomPlayer2Card])
			player1Cards.append(player2Cards[randomPlayer2WarCard])			
			del player2Cards[randomPlayer2Card]			
			del player2Cards[randomPlayer2WarCard]
			print "<p><strong>Player 1 wins!</strong></p>"
			
		elif (player2Cards[randomPlayer2WarCard].value > player1Cards[randomPlayer1WarCard].value):
			player2Cards.append(player1Cards[randomPlayer1Card])
			player2Cards.append(player1Cards[randomPlayer1WarCard])			
			del player1Cards[randomPlayer1Card]			
			del player1Cards[randomPlayer1WarCard]
			print "<p><strong>Player 2 wins!</strong></p>"

		else: print "<p>Something went wrong...</p>"
		
	else:
		if (player1Cards[randomPlayer1Card].value > player2Cards[randomPlayer2Card].value):
			player1Cards.append(player2Cards[randomPlayer2Card])
			del player2Cards[randomPlayer2Card]
			print "<p><strong>Player 1 wins!</strong></p>"
		elif (player2Cards[randomPlayer2Card].value > player1Cards[randomPlayer1Card].value):
			player2Cards.append(player1Cards[randomPlayer1Card])
			del player1Cards[randomPlayer1Card]
			print "<p><strong>Player 2 wins!</strong></p>"


	print "<hr>"
	print "<p><strong>Player 1 card count: %s</p></strong>" %len(player1Cards)
	print "<p><strong>Player 2 card count: %s</p></strong>" %len(player2Cards)
	print "<hr>"

print "<hr>"
print "<h3>Player 1 final card count: %s cards</h3>" %len(player1Cards)
print "<h3>Player 2 final card count: %s cards</h3>" %len(player2Cards)
print "<hr>"
print "<hr>"
if(len(player1Cards) > len(player2Cards)): print "<p><h2>Player 1 Wins!</h2></p>"
elif (len(player2Cards) > len(player1Cards)): print "<p><h2>Player 2 Wins!</h2></p>"
elif (len(player2Cards) == len(player1Cards)): print "<p><h2>THIS GAME IS A DRAW!</h2></p>"
else: print "<p>Something went wrong....</p>"
print "<hr>"
print "</html></body>"
