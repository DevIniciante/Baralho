from random import shuffle

c = ('\033[m',             #0- SEM CORES
     '\033[0;30;41m',      #1- Vermelho
     '\033[0;30;42m',      #2- VERDE
     '\033[0;30;43m',      #3- AMARELO
     '\033[0;30;44m',      #4- AZUL
     '\033[0;30;45m',      #5- ROXO
     '\033[7;30m'          #6- BRANCO
    );

class Card:
    suits = ["Espadas", "Coração", "Diamantes", "Clubes"]
    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, v, s):
        """Suit + values são números inteiros"""
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v = Card.values[self.value] + " de " + Card.suits[self.suit]
        return v

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name

class Game:
    def __init__(self):
        name1 = input(c[2], 'Nome do player 1: ', c[2])
        name2 = input(c[2], 'Nome do player 2: ', c[2])
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def print_winner(self, winner):
        w = (c[4], '{} Ganhou o round', c[4])
        w = w.format(winner.name)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = (c[5], '{} jogou {} e {} jogou {}', c[0])  # Alterado para c[0] para evitar formatação de cor
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)

    def play_game(self):
        cards = self.deck.cards
        print('Começando a Guerra!!')
        while len(cards) >= 2:
            m = (c[6], 'Pressione Q para sair. Qualquer outra tecla para jogar.', c[6])
            response = input(m)
            if response.lower() == 'q':
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.print_winner(self.p1)
            else:
                self.p2.wins += 1
                self.print_winner(self.p2)

        win = self.winner(self.p1, self.p2)
        print(c[1], 'A guerra acabou. {} ganhou'.format(win))  # Alterado de 'A guerra acabou. {} wins',c[1].format(win) para 'A guerra acabou. {} ganhou'.format(win)

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return (c[1], 'Houve um empate', c[1])

game = Game()
game.play_game()
