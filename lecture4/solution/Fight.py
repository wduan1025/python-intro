class Player():
    name = "unknown"
    HP = 100
    power = 100
    score = 3
    med_list = [0]
    def set_name(self, new_name):
        self.name = new_name
    def get_name(self):
        return self.name
    def attack(self,a):
        a.HP -= 10
        self.score += 20
        return a.HP
        return self.score
    def big_attack(self,a):
        a.HP -= 25
        self.power -= 10
        self.score += 30
        return a.HP
        return self.power, self.score
    def take_med(self):
        if s in self.med_list:
            self.HP += SL
            self.med_list.remove(s)
            return self.med_list
        elif l in self.med_list:
            self.HP += LL
            self.med_list.remove(l)
            return self.med_list
        else:
            print("No Med Left")
    def buy_med(self):
        if self.score > 30:
            self.med_list.append(s)
            self.score -= SP
            return self.med_list
            return self.score
        elif self.score > 50:
            self.med_list.append(l)
            self.score -= LP
            return self.med_list
            return self.score
        else:
            print ("Not enough score")
    if HP >= 100:gi
        return 100
    if power <= 0:
        return 0
class Med():
    def _int_(self, life, price):
        self.life = life
        self.price = price
        

red= Player()
red.set_name("red player")
blue= Player()
blue.set_name("blue player")
S_Med = Med(10, 30)
L_Med = Med(30, 50)
SL = S_Med.life
LL = L_Med.life
SP = S_Med.price
LP = L_Med.price
s = S_Med
l = L_Med

if med_size == s

if red.HP <= 0:
    print("Died, blue win")
if blue.HP <= 0:
    print("Died, red win")

red.attack(blue)
red.big_attack(blue)
red.big_attack(blue)
blue.attack(red)
blue.attack(red)
blue.attack(red)
blue.buy_med()
blue.take_med()
red.buy_med()
red.buy_med()
red.take_med()
red.take_med()
blue.attack(red)
blue.attack(red)
blue.attack(red)
blue.attack(red)
blue.big_attack(red)
blue.big_attack(red)
blue.big_attack(red)
blue.big_attack(red)
blue.big_attack(red)