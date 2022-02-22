from deck import Deck


class Poker(Deck):
    ''' Classe Designada a criação das cartas do poker '''

    def get_deck(self):
        deck = self.criar_deck()
        poderes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        power = deck.copy()
        poder, contador = 0, 0
        for carta in deck:
            if contador % 4 == 0:
                poder += 1
            carta["poder"] = poderes[poder]
            deck = [carta]
            contador += 1
        self.deck = power
        return power

    def Combo_check(self, cards):
        return None

    def Combo(self, combo_name=''):

        c = {
            "pair": ["Pair", 20],
            "two_pair": ["Two Pair", 40],
            "three_of_a_kind": ["Three-of-a-Kind", 70],
            "straight": ["Straight", 100],
            "flush": ["Flush", 100],
            "full_house": ["Full House", 150],
            "four_of_a_kind": ["Four-of-a-Kind", 200],
            "straight_flush": ["Straight Flush", 300],
            "royal_straight_flush": ["Royal Straight Flush", 500]
        }
        if combo_name == '':
            return c
        for k in c:
            if combo_name == k:
                return {f"{k}": {"name": c[k][0], "poder": c[k][1]}}

        return None


if __name__ == '__main__':
    p = Poker()
    poker_deck = p.get_deck()
    for card in poker_deck:
        print(card)
