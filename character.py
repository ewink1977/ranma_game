import random

# BASE CLASS ===
class Character():
    def __init__(self, name, hp, str, int, dex, per):
        self.name = name
        self.hp = hp
        self.str = str
        self.int = int
        self.dex = dex
        self.per = per
    
    # def attack_roll(self, oppdex):
    #     attackroll = random.randrange(1, 20, 1)
    #     print(attackroll)
    #     if attackroll > oppdex:
    #         hp_hit = 

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
        super().__init__(name = 'Ranma-Chan', hp = 250, str = 7, int = 7, dex = 15, per = 11)
        self.ki = 10
        self.kawaii = 2
        self.pronoun = 'she'

class RanmaBoy(Character):
    def __init__(self):
        super().__init__(name = 'Ranma', hp = 300, str = 12, int = 8, dex = 8, per = 12)
        self.ki = 10
        self.pronoun = 'he'

class Akane(Character):
    def __init__(self):
        super().__init__(name = 'Akane', hp = 225, str = 10, int = 9, dex = 9, per = 12)
        self.ki = 0
        self.pronoun = 'she'

class Shampoo(Character):
    def __init__(self):
        super().__init__(name = 'Shampoo', hp = 250, str = 10, int = 8, dex = 11, per = 11)
        self.ki = 0
        self.kawaii = 5
        self.pronoun = 'she'

# NPC CHARACTER CLASSES ===
class Tatewaki(Character):
    def __init__(self):
        super().__init__(name = 'Kuno', hp = 250, str = 11, int = 6, dex = 11, per = 12)
        self.ki = 0
        self.pronoun = 'he'

class Happosai(Character):
    def __init__(self):
        super().__init__(name = 'Happosai', hp = 400, str = 15, int = 8, dex = 13, per = 4)
        self.ki = 20
        self.pronoun = 'he'

class Ryouga(Character):
    def __init__(self):
        super().__init__(name = 'Ryouga', hp = 500, str = 20, int = 4, dex = 8, per = 10)
        self.ki = 10
        self.pronoun = 'he'

class Mousse(Character):
    def __init__(self):
        super().__init__(name = 'Mousse', hp = 200, str = 5, int = 5, dex = 15, per = 15)
        self.ki = 0
        self.pronoun = 'he'

class Henchman(Character):
    def __init__(self):
        super().__init__(name = 'Random Henchman', hp = 150, str = 10, int = 10, dex = 10, per = 10)
        self.ki = 0
        self.pronoun = 'he'
