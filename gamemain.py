import character, functions, ui

# Act One 
print(ui.start_message)

player_choice = input(">> ")
choice = int(player_choice)
player = functions.choose_character(choice)

a1_1 = ("\n")
a1_1 += (f"Awesome! You have chosen {player.name} as your character.\n")
a1_1 += (f"{player.pronoun.capitalize()} will be you as you work your way through Nerima\n")
a1_1 += ("and to the hidden Spring of Drowned McGuffin which will neutralize your curse.\n")
a1_1 += ("\n")
a1_1 += ("Be warned, though, many people will try to stop you. Some will want to kill you,\n")
a1_1 += ("others will simply want to molest you or take your underpants. Regardless, be ready to\n")
a1_1 += ("fight them off!\n")
print(a1_1)
input("Hit ENTER once you've read that nonsense and are ready to continue!")

a1_2 = ("\n")
a1_2 += (f"{player.name}, you have many stats which will help you in your journey. I (being the AI)\n")
a1_2 += ("will explain them to you now.\n")
a1_2 += ("\n")
a1_2 += ("HP - Before each action, I will tell you what your HP is. HP does NOT recover on it's own.\n")
a1_2 += ("I don't know how to do that.\n")
a1_2 += (f"Right now your HP is {player.hp}. \n")
print(a1_2)
input("Hit ENTER once you've read that nonsense and are ready to continue!")

a1_3 = ("\n")
a1_3 += ("Characters have four basic stats that will help determine how successful or failful they are at\n")
a1_3 += ("attacking, fleeing, dodging, and investigating. STR, INT, DEX, and PER.\n")
a1_3 += (f"Your strength is {player.str}. The higher the number, the harder you will hit. As well, the less it will\n")
a1_3 += ("hurt when you get hit.\n")
a1_3 += (f"Your intellegence is {player.int}. This probably does nothing. I'm not that good at programming yet.\n")
a1_3 += (f"Your dexterity is {player.dex}. This helps you dodge and run away. The higher it is, the faster you are\n")
a1_3 += ("which will result in your opponent missing more often.\n")
a1_3 += (f"Your perception is {player.per}. Like intellegence, this probably doesn't do anything yet, but hopefully it\n")
a1_3 += ("will help you get loads and loads of loot in the future!\n")
a1_3 += ("\n")
print(a1_3)
input("Hit ENTER once you've read that nonsense and are ready to continue!")

print(ui.a1_4)
input("Hit ENTER once you've read that nonsense and are ready to continue!")

functions.battle(player, character.Henchman())

a1_5 = ("\n")
a1_5 += (f"I hope you won. Let's see, your HP is at {player.hp}\n")
a1_5 += ("Since we just completed a quasi tutorial, we'll go ahead and reset your HP to full.\n")
a1_5 += ("Thanks to a delicious meal from Kasumi!\n")
print(a1_5)
input("Hit ENTER once you've read that nonsense and are ready to continue!")

player.hp = player.maxhp
a1_6 = ("\n")
a1_6 += (f"Now you're all filled up and your HP is {player.hp}!\n")
a1_6 += ("When you're ready, let's go on with the story!")
print(a1_6)
input("Hit ENTER when you're ready to move on!")

# ACT TWO
print(ui.a2_1)
input("Hit ENTER when you're ready.")

print(ui.a2_2)
input("Hit ENTER to continue.")

# KUNO RESPONDS DIFFERENTLY TO EACH PLAYER CHARACTER.
functions.kuno_confrontation(player.name)

functions.battle(player, character.Tatewaki())

print("GREAT SUCCESS!")
