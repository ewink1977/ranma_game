from character import *

def choose_character(choice):
    player = None
    if choice == 1:
        player = RanmaBoy()
    if choice == 2:
        player = RanmaGirl()
    if choice == 3:
        player = Akane()
    return player