import random

class Deck:
    def __init__(self):
        # Kart destesi: 1'den 13'e kadar (As, 2, 3 ... Papaz)
        self.cards = list(range(1, 14)) * 4  # 4 farklı tür (kupa, karo, vs)
        random.shuffle(self.cards)

    def draw_card(self):
        if len(self.cards) == 0:
            # Deste boşsa yeniden kar
            self.__init__()
        return self.cards.pop()
