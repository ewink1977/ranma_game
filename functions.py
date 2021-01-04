from character import *

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
            attack_roll = random.randrange(1, 20, 1)
            if attack_roll > player.dex and battleactive == True:
                print(f"{npc.name}'s turn now!")
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