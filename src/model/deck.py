
class Deck:
    ''' Essa Classe Cria um baralho em simples '''

    def __init__(self):

        self.suit = ['♥', '♦', '♣', '♠']

        self.numeracao = ['2', '3', '4', '5', '6',
                          '7', '8', '9', 'J', 'Q', 'K', 'A']

    def criar_deck(self):
        deck = []
        carta = []

        for numero in self.numeracao:
            for naipes in self.suit:
                carta += ['_________']
                carta += [f'|      {naipes}|']
                carta += [f'|       |']
                carta += [f'|   {numero}   |']
                carta += [f'|       |']
                carta += [f'|{naipes}      |']
                carta += ['¯¯¯¯¯¯¯¯¯']
                np = naipes
                nm = numero

                deck.append({'card': carta, 'suit': np, 'number': nm})
                carta = []
        return deck


if __name__ == '__main__':

    d = Deck()
    deck = d.criar_deck()

    c = 0
    lista = [[], [], [], [], [], [], []]
    for dic in deck:
        card = dic['card']

        c += 1
        lista[0].append(card[0])
        lista[1].append(card[1])
        lista[2].append(card[2])
        lista[3].append(card[3])
        lista[4].append(card[4])
        lista[5].append(card[5])
        lista[6].append(card[6])

        if c == 5:
            break

    print(lista)

    for carta in lista:
        for elemento in carta:
            print(elemento, end='\t')
        print()
