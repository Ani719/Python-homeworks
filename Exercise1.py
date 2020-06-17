import random
class Game:
    def __init__(self, player1, player2, score=49):
        self.player1 = player1
        self.player2 = player2
        self.score = score


class Player:
    def __init__(self, name, surname, point=0):
        self.name = name

        self.surname = surname

        self.point = point

    def to_play(self):
        self.point += 1


game = Game(Player("Ani", "Manukyan"), Player("Ararat", "Hovhannisyan"))

while game.player1.point < game.score and game.player2.point < game.score:

    number = random.randint(1, 2)
    if number == 1:
        game.player1.to_play()
        print("player1 get point", game.player1.point)
    else:
        game.player2.to_play()
        print("player2 get point", game.player2.point)

if game.player1.point > game.player2.point:

    print("player1 win!")
else:
    print("player2 win!")