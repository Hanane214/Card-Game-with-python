from card import Card
from random import shuffle

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(4):
            for j in range(13):
                self.cards.append(Card(i,j))
        
    def __str__(self):
        str_card = ''
        for i in self.cards:
            str_card += '|' + str(i)
        str_card += '|'
        return str_card

    def __len__(self):
        return len(self.cards) 

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        shuffle(self.cards)

    def pop_card(self):
        if len(self.cards):
            return self.cards.pop(0)
