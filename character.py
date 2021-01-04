import random

# BASE CLASS ===
class Character():
    def __init__(self, name, hp, str, int, dex, per, level, xp = 0):
        self.name = name
        self.hp = hp
        self.str = str
        self.int = int
        self.dex = dex
        self.per = per
        self.level = level
        self.xp = xp
    
    def dodge_roll(self):
        dodge_roll = random.randrange(1, 20, 1)
        print(dodge_roll)
        if dodge_roll >= self.dex:
            return print(f'{self.name} was hit!')
        else:
            return print(f'Woot! {self.name} managed to dodge!')

# PLAYER CHARACTER CLASSES ===
class RanmaGirl(Character):
    def __init__(self):
        super().__init__(name = 'Ranma-Chan', hp = 250, str = 7, int = 7, dex = 15, per = 11, level = 1)
        self.ki = 10

class RanmaBoy(Character):
    def __init__(self):
        super().__init__(name = 'Ranma', hp = 300, str = 12, int = 8, dex = 8, per = 12, level = 1)
        self.ki = 10

class Akane(Character):
    def __init__(self):
        super().__init__(name = 'Akane', hp = 225, str = 10, int = 9, dex = 9, per = 12, level = 1)
        self.ki = 0

# NPC CHARACTER CLASSES ===
class Tatewaki(Character):
    def __init__(self):
        super().__init__(name = 'Kuno', hp = 250, str = 11, int = 6, dex = 11, per = 12, level = 1)
        self.ki = 10



