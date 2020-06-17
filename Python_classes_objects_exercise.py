import random

class Soldier:
    health = 100
    hit = 20

    def to_fight(self):

        self.health -= self.hit
        return self.health


unit1 = Soldier()

unit2 = Soldier()

while unit1.health > 0 and unit2.health > 0:

    random_hit = random.randint(1, 2)

    if random_hit == 1:

        unit1.to_fight()

        print("Unit1 to attack Unit2: ", unit2.health)

    else:

        unit2.to_fight()

        print("Unit2 to attack Unit1: ", unit1.health)

if unit1.health == 0:

    print("Unit2 win!")

else:

    print('Unit1 win!')