import character, functions

start_message = ("Welcome to ewink's Funkdafied Ranma 1/2 RPG!\n")
start_message += ("Start off by choosing your character from the following list:\n")
start_message += ("1) Ranma (Boy-Type), 2) Ranma (Girl-Type), 3) Akane")
print(start_message)

player_choice = input(">> ")
choice = int(player_choice)
player = functions.choose_character(choice)

print(player.name)

player.dodge_roll()
