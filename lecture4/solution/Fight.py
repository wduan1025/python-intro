SL = 10
LL = 30
SP = 30
LP = 50
S_Med = Med(SL, SP)
L_Med = Med(LL, LP)

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
        return a.HP, self.score
    def big_attack(self,a):
        a.HP -= 25
        self.power -= 10
        self.score += 30
        return a.HP
        return self.power, self.score

    def take_med(self, target_med):
        if compare(target_med, S_Med):
        # if med_size == s:
            first_small_med_index = -1  
            for i in range(len(self.med_list)):
                if self.med_list[i].life == SL:
                    first_small_med_index = i
                    break
            if first_small_med_index == -1:
                return
            self.med_list = self.med_list[:first_small_med_index] + self.med_list[first_small_med_index+1:]
            self.HP += SL
        # self.med_list.remove(m)
        # break
        # if s in self.med_list:
        #     self.HP += SL
        #     self.med_list.remove(s)
        #     return self.med_list
        # elif l in self.med_list:
        #     self.HP += LL
        #     self.med_list.remove(l)
        #     return self.med_list
        # else:
        #     print("No Med Left")
    
    # med_size should be "s" or "l"
    def buy_med(self, med_size):
        if med_size == "s":
            if self.score < SP:
                return
            med = Med(SL, SP)
            self.score -= SP
            self.med_list.append(s)
        
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
    if HP >= 100:
        return 100
    if power <= 0:
        return 0

class Med:
    def _int_(self, life, price):
        self.life = life
        self.price = price
        

red= Player()
red.set_name("red player")
blue= Player()
blue.set_name("blue player")


def compare_med(m1, m2):
    return m1.life == m2.life and m1.price == m2.price

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