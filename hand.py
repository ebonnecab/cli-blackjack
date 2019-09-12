class Hand:
    def __init__(self, dealer=False):
        self.dealer = dealer
        self.cards = []
        self.value = 0

    def add_card(self, card):
        self.cards.append(card)
    
    def get_value(self):
        self.value = 0

        for card in self.cards:
            if card.value.isnumeric():
                self.value += int(card.value)
            elif card.value == "A" and self.value > 21:
                self.value -= 10
            elif card.value == "A":
                self.value += 11
        return self.value
    
        def show_hand(self):
            if self.dealer:
                print("Dealer")
                print(self.cards[1])
            else:
                for card in self.cards:
                    print(card)
                print("Total: {}".format(self.get_value()))