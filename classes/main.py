from card import Card
from deck import Deck
from hand import Hand


d = Deck()

h1 = Hand('Player1')
h2 = Hand('Player2')
h3 = Hand('Player3')
h4 = Hand('Player4')

players = [h1, h2, h3, h4]


d.shuffle()

while len(d)
    h1.add_card(d.pop_card())
    h2.add_card(d.pop_card())
    h3.add_card(d.pop_card())
    h4.add_card(d.pop_card())

print(h1)
print(h2)
print(h3)
print(h4)

for i in 