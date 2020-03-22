class Player():
    def __init__(self, name):
        self.name = name
        self.HP = 100
        self.power = 100
        self.score = 3
        self.med_list = []

    def set_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return self.name

    def attack(self,a):
        ATTACK_DAMAGE = 10
        if a.HP < ATTACK_DAMAGE:
            self.die(a)
        a.HP -= ATTACK_DAMAGE
        self.score += 20
        print(self.name, "hits", a.name, "causing ", ATTACK_DAMAGE, "damage")

    def big_attack(self,a):
        BIG_ATTACK_POWER_COST = 10
        if self.power < BIG_ATTACK_POWER_COST:
            print("Not enough power, failt to use big attack")
            return
        BIG_ATTACK_DAMAGE = 25
        if a.HP < BIG_ATTACK_DAMAGE:
            self.die(a)
        a.HP -= BIG_ATTACK_DAMAGE
        self.power -= BIG_ATTACK_POWER_COST
        self.score += 30
        print(self.name, "hits", a.name, "causing ", BIG_ATTACK_DAMAGE, "damage")

    # As long as valid MedType is passed in as argument
    # No matter what it is, just find the first item
    # that is instance of this class, drop it, and 
    # increase HP accordingly
    def take_med(self, MedType):
        first_small_med_index = -1  
        for i in range(len(self.med_list)):
            if isinstance(self.med_list[i], MedType):
                first_small_med_index = i
                break
        if first_small_med_index == -1:
            return
        self.HP += MedType.life
        self.med_list.pop(first_small_med_index)
    
    def buy_med(self, MedType):
        if self.score < MedType.price:
            print("Not enough score to buy med")
            return
        self.score -= MedType.price
        self.med_list.append(MedType())
    # Called in attack() and big_attack() when opponent HP
    # is lower than damage
    def die(self, a):
        exit("Player "+a.name+" died")

class SmallMed:    
    life = 10
    price = 30

class BigMed:
    life = 30
    price = 50

if __name__ == "__main__":
    red= Player("Ned Stark")
    blue= Player("Arthur Dayne")

    red.attack(blue)
    red.big_attack(blue)
    red.big_attack(blue)
    blue.attack(red)
    blue.attack(red)
    blue.attack(red)
    blue.buy_med(BigMed)
    blue.take_med(BigMed)
    red.buy_med(SmallMed)
    red.buy_med(SmallMed)
    red.take_med(SmallMed)
    red.take_med(SmallMed)
    blue.attack(red)
    blue.attack(red)
    blue.attack(red)
    blue.attack(red)
    blue.big_attack(red)
    blue.big_attack(red)
    blue.big_attack(red)
    blue.big_attack(red)
    blue.big_attack(red)