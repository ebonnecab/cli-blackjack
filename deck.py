from card import Card
import random

class Deck:
    def __init__(self):
        self.cards = []
    
    def fill_deck(self):
        suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

        self.cards = [Card(suit, val) for suit in suits for val in values]
        return self.cards
    
    def shuffle(self):
        if self.cards:
            random.shuffle(self.cards)
        
    def deal(self):
        if self.cards:
            return self.cards.pop(0)