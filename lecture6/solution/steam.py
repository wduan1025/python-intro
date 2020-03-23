from game1.fight import *
game = game1.fight

class user:
    playlist = []
    money = 50
    def __int__(name,age):
        self.name = name
        self.age = age
    def play(self, game):
        python(game)
    def buy_game(self,a):
        if user.age < a.limit:
            print("limitation was set for this game.")
        elif user.money < a.price:
            print("Not enough money left")
        else:
            self.playlist.append[a]

class game:
    def __int__(price,limit):
        self.price = price
        self.limit = limit

GTA = game(100,18)
Jack = user("Jack",17)
