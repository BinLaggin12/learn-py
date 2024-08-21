import random
x = random.randint(1, 6)
y = random.randint(1, 6)
class Dice:
    def roll_one(self):
        print(f"The die shows {x}")
    def roll_two(self):
        print(f"The dice show ({x},{y})")


dice = Dice()
dice.roll_one()
