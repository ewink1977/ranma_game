# BASE CLASS ===
class Character():
    def __init__(self, name, hp, str, int, dex, per):
        self.name = name
        self.hp = hp
        self.str = str
        self.int = int
        self.dex = dex
        self.per = per
    
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
