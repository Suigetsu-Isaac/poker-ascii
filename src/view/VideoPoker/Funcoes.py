import sistema
from poker import Poker
import random

p = Poker()

poker_deck = p.get_deck()
play_deck = poker_deck.copy()


class fichas():
    ''' Classe responsavel pela contabilidade das fichas do usuário '''

    def __init__(self, nome):
        self.nome = nome
        self.fichas = 1000
        self.aposta = 0

    def listar_combos(self):
        listagem = p.Combo()
        listagem.pop('pair')

        if self.aposta == 0:
            return None
        print('as apostas da mesa são essas: \n')
        for e in listagem.values():

            print(f'Combo: {e[0]} -> {e[1]*self.aposta} Fichas')

    def add_ficha(self, combo):
        print(p.combo[combo][0])
        self.fichas += p.combo[combo][1]*self.aposta

    def apostas(self, quantidade):
        print(quantidade)
        self.fichas -= quantidade

        if self.fichas < 0:
            self.fichas = 0
            print('Você está sem fichas')
            return None
        self.aposta = int(quantidade/20)


def Mesa(mesa=[], quais=['1', '2', '3', '4', '5']):
    ''' Função responsavel pelas 5 cartas que irão aparecer na tela'''
    card_break = [[], [], [], [], [], [], []]
    if not mesa:
        ''' A 1ª execução da função nela irá tirar as 5 cartas aleatoria do baralho '''
        for i in range(5):
            r = random.randint(0, len(play_deck)-1)

            for cb in range(7):
                card_break[cb].append(play_deck[r]['card'][cb])

            mesa.append(play_deck.pop(r))
        return mesa, card_break
    ''' A 2ª execução da função nela as cartas que o usuário deseja retirar 
        serão substituidas por novas cartas do baralho'''
    total = ['1', '2', '3', '4', '5']
    sobras = set(total).difference(set(quais))
    sobras = list(sobras)
    for e in sobras:
        r = random.randint(0, len(play_deck)-1)
        mesa[int(e) - 1] = play_deck.pop(r)

    for card in mesa:
        for cb in range(7):
            card_break[cb].append(card['card'][cb])

    return mesa, card_break
