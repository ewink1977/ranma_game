from character import *
import random

def choose_character(choice):
    player = None
    if choice == 1:
        player = RanmaBoy()
    if choice == 2:
        player = RanmaGirl()
    if choice == 3:
        player = Akane()
    if choice == 4:
        player = Shampoo()
    return player

# BATTLE FUNCTION!
def battle(player, npc):
    battleactive = True
    may_flee = True
    while battleactive == True:
        print("\n")
        print(f"{player.name}, your HP is {player.hp}.\n")
        print(f"{npc.name}'s HP is at {npc.hp} \n")
        print("What do you want to do?\n")
        action = input(" A-Attack\n R-Run Away\n >>")
        if action.capitalize() == 'A':
            attack_roll = random.randrange(1, 20, 1)
            if attack_roll > npc.dex:
                hp_hit = attack_roll + player.str
                npc.hp -= hp_hit
                print(f"DEBUG: ROLL {attack_roll} - HP HIT {hp_hit} - NPC HP {npc.hp}")
                if npc.hp > 0:
                    print(f'YEOWCH! {npc.name} was just whomped for {hp_hit}!')
                if npc.hp <= 0:
                    print(f'Welp, you killed {npc.name}. I guess that makes you a good guy...')
                    battleactive = False
            else:
                print(f"{npc.name} dodged your attack! Holy smokes!")
            # IF NPC IS DEAD, WE DON'T WANT TO RUN THIS PART, CHECKING BATTLEACTIVE.
            if battleactive == True: 
                print(f"{npc.name}'s turn now!")
                attack_roll = random.randrange(1, 20, 1)
                if attack_roll > player.dex:
                    hp_hit = attack_roll + npc.str
                    player.hp -= hp_hit
                    print(f"DEBUG: ROLL {attack_roll} - HP HIT {hp_hit} - PLAYER HP {player.hp}")
                    if player.hp > 0:
                        print(f"KASPLOOSH!!! {npc.name} just clocked you for {hp_hit}!!")
                    if player.hp <= 0:
                        print("Well, you're dead. Kind of sad. Bye bye.")
                        battleactive = False
                else:
                    print(f"You managed to dodge {npc.name}'s attack! Nice work!")
        elif action.capitalize() == 'R':
            if may_flee == True:
                flee_roll = random.randrange(1, 20, 1)
                if flee_roll <= player.dex:
                    print(f"You managed to escape from {npc.name}!")
                    battleactive = False
                else:
                    print("Flee failed. You have to fight.")
                    may_flee = False
            if may_flee == False:
                print("YOU MAY NOT FLEE!")
        else:
            print('I gave you two freaking options...')

# KUNO CONFRONTATION FUNCTION!
def kuno_confrontation(opp):
    # DIFFERENT DIALOGUE FOR DIFFERENT PLAYER CHARACTERS.
    if opp == "Ranma":
        kuno_dialogue = ("\n")
        kuno_dialogue += ("Ranma Saotome! You enemy of women! I will smite you and end your reign of terror\n")
        kuno_dialogue += ("and your oppression of the beautiful Akane Tendo and the busty and naive\n")
        kuno_dialogue += ("Pig-Tailed girl!\n")
        kuno_dialogue += ("Prepare yourself for battle!\n")
        kuno_dialogue += ("\n")
        return print(kuno_dialogue)
    if opp == "Ranma-Chan":
        kuno_dialogue = ("\n")
        kuno_dialogue += ("OH MY GOD! The beautiful and voluptuous Pig-Tailed Girl! My love for you knows no bounds! I\n")
        kuno_dialogue += ("am so happy that you have found me in this inconspicuous alley. Because of this, I will grant\n")
        kuno_dialogue += ("you one wonderful wish, which I know will be the embrace and the love of me, the Blue Thunder\n")
        kuno_dialogue += ("of Furinkin High!\n")
        kuno_dialogue += ("++ Kuno glomps on to you and tries to kiss you. ++\n")
        kuno_dialogue += ("\n")
        return print(kuno_dialogue)
    if opp == "Akane":
        kuno_dialogue = ("\n")
        kuno_dialogue += ("Is that... AKANE TENDO! My Goddess! I find it wonderful that you have sought\n")
        kuno_dialogue += ("I, the Blue Thunder of Furinkin High out. Very well, thanks to your hard work,\n")
        kuno_dialogue += ("I find you worthy. Yes, very well, I shall date with you!\n")
        kuno_dialogue += ("++ Kuno jumps at you to try and glomp on, but you send him into the\n")
        kuno_dialogue += ("stratosphere. Once he lands, the battle will begin. ++\n")
        kuno_dialogue += ("\n")
        return print(kuno_dialogue)
    if opp == "Shampoo":
        kuno_dialogue = ("\n")
        kuno_dialogue += ("Greetings. I see you have come into my alleyway. I assume that means that you\n")
        kuno_dialogue += ("wish to date with me. You are a friend of the vile enemy of women, Ranma\n")
        kuno_dialogue += ("Saotome, so I would usually not give you my company. However, you have both\n")
        kuno_dialogue += ("beauty and brains, having sought me out. Very well, if you can defeat me, I\n")
        kuno_dialogue += ("shall date with you!\n")
        kuno_dialogue += ("\n")
        return print(kuno_dialogue)