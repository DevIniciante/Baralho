from random import shuffle

class Card:
    suits = ["Espadas", "Coração", "Diamantes", "Clubes"]
    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, v, s):
        """Suit + values são números inteiros"""
        self.value = v
        self.suits = s

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suits < c2.suits:
                return True
            else:
                return False
        return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suits > c2.suits:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v = Card.values[self.value] + " de " + Card.suits[self.suits]
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
        name1 = input("Nome do player 1: ")
        name2 = input("Nome do player 2: ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def print_winner(self, winner):
        w = "{} Ganhou o round"
        w = w.format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = "{} jogou {} e {} jogou {}"
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)

    def play_game(self):
        cards = self.deck.cards
        print("Começando a Guerra!!")
        while len(cards) >= 2:
            m = "Pressione Q para sair. Qualquer outra tecla para jogar."
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
                self.print_winner(self.p1.name)
            else:
                self.p2.wins += 1
                self.print_winner(self.p2.name)

        win = self.winner(self.p1, self.p2)
        print("A guerra acabou. {} wins".format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "Houve um empate"

game = Game()
game.play_game()
