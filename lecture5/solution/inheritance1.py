#  def __str__(self):
#         return '{' + ','.join([str(i) for i in self.items]) + '}'

class food:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "Food Name: {food_name}".format(food_name = self.name)
class meat(food):
    def __init__(self, name):
        super().__init__(name)
    def introduce(self):
        print("I am", self.name, "considering as meat.")
class vegetable(food):
    def __init__(self, name):
        super().__init__(name)
    def introduce(self):
        print("my name is", self.name, "considering as vegetable.")
class delicious(food):
    def taste(self):
        print(self.name, "is delicious.")
class awful(food):
    def taste2(self):
        print(self.name, "tastes awful")

class Beef(meat, delicious):
    pass
class GBeans(vegetable, delicious):
    pass
class Bat(meat, awful):
    pass

beef = Beef("A5 Beef")
greenbeans = GBeans("Green Beans")
Beef.introduce()